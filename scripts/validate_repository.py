#!/usr/bin/env python3
"""Validate the published records, aggregates, and privacy boundary."""

from __future__ import annotations

import csv
import json
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = REPOSITORY_ROOT / "data"
RECORDS_DIR = DATA_DIR / "records"
EXPECTED_RECORDS = 382
EXPECTED_UNIQUE_OBJECTS = 18_254
EXPECTED_NETWORK_OBJECTS = 7_342
EXPECTED_NETWORK_PAIRS = 11_018

# The source playlist identifier is intentionally not repeated here. This
# fragment is sufficient to detect an accidental publication of its URL.
PRIVATE_PLAYLIST_FRAGMENT = "PL_iBoDmbefrB" + "XWzE6vxKkBNwMIadV5fgP"


def validate_records() -> None:
    record_paths = sorted(RECORDS_DIR.glob("*.json"))
    assert len(record_paths) == EXPECTED_RECORDS, len(record_paths)
    video_ids: set[str] = set()

    for path in record_paths:
        record = json.loads(path.read_text(encoding="utf-8-sig"))
        video_id = str(record["video_id"])
        assert video_id not in video_ids, f"Duplicate video ID: {video_id}"
        video_ids.add(video_id)
        assert video_id in record["url"], f"URL mismatch: {path.name}"
        assert record["official_title"].strip(), f"Missing title: {path.name}"

        objects = record.get("objects", [])
        object_ids = [str(item["id"]) for item in objects]
        assert len(object_ids) == len(set(object_ids)), f"Duplicate object ID: {path.name}"
        assert all(str(item["label"]).strip() for item in objects), path.name

        object_id_set = set(object_ids)
        for relation in record.get("relations", []):
            assert str(relation["subject"]) in object_id_set, path.name
            assert str(relation["object"]) in object_id_set, path.name
            assert str(relation["relation"]).strip(), path.name


def validate_aggregates() -> None:
    with (DATA_DIR / "object_frequencies.csv").open(
        "r", encoding="utf-8-sig", newline=""
    ) as handle:
        reader = csv.DictReader(handle)
        assert reader.fieldnames == ["rank", "object", "frequency", "analysis_group"]
        frequency_rows = list(reader)
    assert len(frequency_rows) == EXPECTED_UNIQUE_OBJECTS, len(frequency_rows)
    assert int(frequency_rows[114]["rank"]) == 115
    assert int(frequency_rows[114]["frequency"]) == 15
    assert frequency_rows[114]["analysis_group"] == "True"
    assert frequency_rows[115]["analysis_group"] == "False"

    network = json.loads((DATA_DIR / "semantic_network.json").read_text(encoding="utf-8"))
    meta = network["meta"]
    assert meta["videos"] == EXPECTED_RECORDS
    assert meta["uniqueObjects"] == EXPECTED_UNIQUE_OBJECTS
    assert meta["networkObjects"] == EXPECTED_NETWORK_OBJECTS
    assert meta["networkPairs"] == EXPECTED_NETWORK_PAIRS
    assert len(network["videos"]) == EXPECTED_RECORDS


def validate_privacy() -> None:
    for path in REPOSITORY_ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() not in {".md", ".py", ".json", ".csv", ".ipynb", ".txt"}:
            continue
        text = path.read_text(encoding="utf-8-sig", errors="ignore")
        assert PRIVATE_PLAYLIST_FRAGMENT not in text, f"Private playlist leaked in {path}"
        lowered = text.lower()
        credential_variable = "openai" + "_api_key"
        credential_prefix = "sk" + "-proj-"
        assert credential_variable not in lowered, f"Possible credential name in {path}"
        assert credential_prefix not in lowered, f"Possible API credential in {path}"


def main() -> None:
    validate_records()
    validate_aggregates()
    validate_privacy()
    print("Validated 382 records, aggregate counts, relation endpoints, and privacy boundary.")


if __name__ == "__main__":
    main()
