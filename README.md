# Dan John YouTube corpus semantic network analysis

This repository contains the data, notebook, and reconstruction code behind a semantic network analysis of 382 Dan John YouTube videos.

The central question is:

> What does the complete corpus reveal about how Dan John communicates and structures strength training?

The project is not an attempt to convert hundreds of transcripts into one rigid programme. It uses repeated objects and relations to expose the programmes, exercise families, progressions, substitutions, combinations, and recurring design principles that hold the corpus together.

Read the full case study: [I watched 382 Dan John Strength Coach YouTube videos so that you don't have to](https://decrepitfilth.art/dan-john-youtube-playlist-semantic-network-analysis)

## Headline results

| Measure | Result |
|---|---:|
| Analysed videos | 382 |
| Object occurrences | 28,186 |
| Unique normalized object labels | 18,254 |
| Analysis-group cutoff | rank 115 / frequency 15 |
| First-order objects | 3,168 |
| Additional second-order objects | 4,059 |
| Objects in the relation network | 7,342 |
| Object pairs in the relation network | 11,018 |
| Directed relation statements | 11,486 |

The strongest repeated structures preserve familiar Dan John programmes and training systems, but the more interesting result is the grammar beneath them:

```text
Choose the objective
    ↓
Select fundamental movement categories
    ↓
Choose suitable variations
    ↓
Apply progressions, regressions or substitutions
    ↓
Combine and dose them simply
    ↓
Preserve recovery and repeatability
```

In plainer language, the corpus appears to optimise for useful, sustainable results per unit of time, effort, complexity, and recovery cost.

## General method

```text
Large unstructured corpus
    ↓
Acquire and preserve sources
    ↓
Extract objects and relations
    ↓
Count recurring objects
    ↓
Identify persistent object pairs
    ↓
Construct relational neighbourhoods
    ↓
Recognise larger structures
    ↓
Return to individual sources for interpretation
```

This is the larger point of the project: to demonstrate a general method for discovering meaningful structure in a large, unstructured corpus.

## Repository contents

```text
data/
├── object_frequencies.csv       Ranked frequency of every normalized object label
├── semantic_network.json        Dashboard-ready network and video metadata
├── videos.csv                   Public per-video manifest
└── records/                     382 per-video object–relation records
docs/
├── data_dictionary.md
├── experiments_and_failures.md
├── extraction_specification.md
├── findings.md
├── limitations.md
└── methodology.md
notebooks/
└── dan_john_playlist_analysis.ipynb
scripts/
├── build_dashboard_data.py
├── build_video_manifest.py
└── validate_repository.py
```

Raw transcripts are deliberately not published. The records contain derived objects and relations plus public metadata for individual videos. The source playlist URL is also excluded so that the account which assembled it is not exposed.

## Reproduce the analysis

Python 3.11 or later is recommended.

```bash
python -m venv .venv
python -m pip install -r requirements.txt
jupyter lab notebooks/dan_john_playlist_analysis.ipynb
```

Rebuild the dashboard JSON from the public records:

```bash
python scripts/build_dashboard_data.py --dataset-root . --output data/semantic_network.rebuilt.json
```

Rebuild the video manifest and validate the repository:

```bash
python scripts/build_video_manifest.py
python scripts/validate_repository.py
```

The notebook contains the object-frequency plot, cutoff calculation, first- and second-order expansion, repeated exercise-pair analysis, and an interactive searchable relation browser.

## Extraction provenance

The final corpus-scale object and relation extraction was performed directly with Codex 5.6 Sol at extra-high reasoning. It was not produced by a local language model or by a bulk API pipeline. GPT-4.1 and GPT-4.1 mini were tested during earlier experiments; those experiments informed the final specification but are not mixed into the published 382-record dataset.

See [methodology](docs/methodology.md), [extraction specification](docs/extraction_specification.md), and [limitations](docs/limitations.md) before treating recurrence as endorsement, truth, or causal evidence.
