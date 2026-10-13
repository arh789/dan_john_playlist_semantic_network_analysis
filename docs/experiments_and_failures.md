# Experiments, failures, and what endured

## Rich per-video analysis

The first analytical design requested an alternative title, summary, semantic map, objects, and relations for each transcript. It produced good individual summaries and useful examples, but it was too slow and too interpretive for the corpus-scale question. The summaries and semantic maps did not become the main analytical substrate.

What endured: source identity, official title, objects, and relations.

## API model comparison

GPT-4.1 and GPT-4.1 mini were tested on early transcripts.

- GPT-4.1 mini was unsuitable: its extraction quality was too weak for this use.
- GPT-4.1 found useful relations and often included more objects, but its output needed pruning.
- Prompts that asked the API to analyse, classify, prune, or construct higher-order relations inflated a simple collection task.

What endured: a minimal instruction to collect many grounded objects and many grounded relations. Higher-order structure would be computed after collection.

## Corpus-scale direct extraction

The final 382-record run was completed directly with Codex 5.6 Sol at extra-high reasoning. The recurring operational failure was continuity: long work was prone to stalling and required explicit batching and progress checks.

What endured: one JSON record per video, stable local object IDs, and relation endpoints constrained to the local object list.

## First cutoff attempt

An early elbow calculation selected rank 2,533 because the long tail of singleton objects dominated the geometry. It was mathematically reproducible and analytically useless.

What endured: exclude the singleton plateau before applying the normalized curve-distance method. That produced the defensible cutoff after rank 115, with frequency 15 as the minimum included frequency.

## One giant network

The 7,342-object relation graph proved that a network could be built, but the unfiltered view was a hairball. Visual styling alone could not rescue it.

What endured: frequency-scaled nodes, transparent edges, selectable neighbourhoods, text search, object-scope controls, and a pair-frequency threshold slider.

## Pair frequency and relation meaning

Object frequency identified what kept appearing. Pair frequency identified which things kept being discussed together. It substantially simplified network construction because relation wording could vary while a stable unordered pair accumulated evidence.

That simplification also erased meaning. Returning to directed relation wording was necessary to distinguish progression, substitution, programme composition, exercise sequencing, functional equivalence, and comparison.

What endured: pair frequency for discovering structure; directed relations for interpreting why the structure exists.
