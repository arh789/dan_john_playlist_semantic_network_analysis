#!/usr/bin/env python3
"""Build a flat public video manifest from the per-video JSON records."""

from __future__ import annotations

import csv
import json
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
RECORDS_DIR = REPOSITORY_ROOT / "data" / "records"
OUTPUT_PATH = REPOSITORY_ROOT / "data" / "videos.csv"


def main() -> None:
    rows = []
    for record_path in RECORDS_DIR.glob("*.json"):
        record = json.loads(record_path.read_text(encoding="utf-8-sig"))
        rows.append(
            {
                "playlist_position": int(record["playlist_position"]),
                "video_id": record["video_id"],
                "official_title": record["official_title"],
                "url": record["url"],
                "object_count": len(record.get("objects", [])),
                "relation_count": len(record.get("relations", [])),
            }
        )

    rows.sort(key=lambda row: row["playlist_position"])
    with OUTPUT_PATH.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows):,} videos to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
