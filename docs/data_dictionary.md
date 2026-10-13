# Data dictionary

## `data/records/*.json`

One derived analytical record per video.

| Field | Type | Meaning |
|---|---|---|
| `playlist_position` | integer | Original source order. It does not reveal the playlist URL. |
| `video_id` | string | YouTube video identifier. |
| `url` | string | Canonical URL for the individual public video. |
| `official_title` | string | Title captured from YouTube metadata. |
| `transcript.file` | string | Provenance pointer used in the private working dataset. The transcript is not included here. |
| `objects` | array | Locally identified objects with IDs and labels. |
| `objects[].id` | string | Identifier valid only inside that record. |
| `objects[].label` | string | Human-readable extracted object label. |
| `relations` | array | Directed object–relation–object statements. |
| `relations[].subject` | string | Local object ID at the source end. |
| `relations[].relation` | string | Extracted relation wording. |
| `relations[].object` | string | Local object ID at the target end. |

## `data/object_frequencies.csv`

| Column | Type | Meaning |
|---|---|---|
| `rank` | integer | Descending rank by total corpus frequency. |
| `object` | string | Normalized object label. |
| `frequency` | integer | Number of extracted object entries with this normalized label. Labels are unique within each published video record, so this also equals the number of analysed videos in which the label was extracted. |
| `analysis_group` | boolean | `True` for ranks 1–115, the objects before the selected cutoff. |

The analysis-group cutoff is after rank 115. Every object in the group has frequency 15 or greater.

## `data/semantic_network.json`

This is a compact, dashboard-ready reconstruction of the public records.

| Section | Meaning |
|---|---|
| `meta` | Corpus and network counts. |
| `frequencies` | Ranked normalized object-frequency records. |
| `nodes` | Objects in the analysis group or its first two relational neighbourhoods. |
| `edges` | Unordered object pairs with total pair frequency. |
| `relations` | Directed relation statements, their frequency, and supporting video IDs. |
| `videos` | Individual video IDs, official titles, and canonical video URLs. |

Node groups:

- **Analysis group:** the 115 objects before the frequency cutoff.
- **First order:** objects directly related to at least one analysis-group object.
- **Second order:** additional objects directly related to a first-order object.

An edge frequency counts how many extracted relation instances connected the pair, regardless of direction or exact relation wording. The `relations` section retains those distinctions.

## `data/videos.csv`

A flat public manifest of the 382 analysed videos: source position, video ID, official title, individual video URL, object count, and relation count.
