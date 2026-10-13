# Methodology

The project moved from maximum extraction toward minimum sufficient explanation. Its unit of analysis changed several times; those changes define ten epochs.

## 1. Corpus acquisition

**Question:** What videos exist, and can their transcripts be obtained?

The source set was enumerated, a dedicated project directory was created, transcripts were downloaded, and collection failures were checked. Raw source material was preserved separately from analysis.

## 2. Record definition

**Question:** What should be stored for each video?

The proposed record included URL, official title, alternative title, summary, transcript, semantic map, objects, and relations. Discussion at this stage exposed where premature database and ontology design was making claims the material could not yet support.

## 3. Rich-analysis experiment

**Question:** Can each video immediately be interpreted in depth?

Initial records attempted titles, summaries, semantic maps, objects, and relations. Some summaries were useful, but the process was slow and produced more interpretation than the developing corpus analysis required.

## 4. Model comparison

**Question:** Could API models perform equivalent extraction faster?

GPT-4.1 and GPT-4.1 mini were tested against the original direct Codex work. GPT-4.1 mini was rejected as unsuitable. GPT-4.1 produced useful relations but required pruning.

## 5. Minimal collection specification

**Question:** What is the smallest useful extraction task?

The final task was reduced to official title, objects, and relations. Attempts to make the extractor analyse, prune, rank, or construct higher-order relations were unnecessary. This was data collection; the corpus-level analysis would happen afterwards.

## 6. Corpus-scale direct extraction

**Question:** Can the complete corpus be processed consistently?

Codex 5.6 Sol at extra-high reasoning extracted objects and relations directly from every available transcript, in batches. One unrelated transcript was removed, and a rapid error check followed completion. The published set contains 382 records.

## 7. Object-frequency analysis

**Question:** Which extracted objects warrant attention first?

The records contained 28,186 object occurrences and 18,254 normalized labels. A normalized curve-distance calculation, applied after excluding the singleton plateau, found an elbow after rank 115. Frequency 15 is the lowest frequency in this analysis group.

Frequency counted extracted object entries. Because normalized labels are unique within each video record, this is also the number of analysed videos in which an object was extracted. The question was deliberately simple: what things keep coming up in discussion?

## 8. Relational expansion and visualisation

**Question:** What surrounds the analysis group?

The 115 analysis-group objects connected to 3,168 first-order objects and 4,059 additional second-order objects. The resulting network contains 7,342 objects and 11,018 pairs.

The notebook added frequency plots, cutoff calculation, interactive network navigation, node scaling, edge-opacity control, text search, neighbourhood isolation, and a pair-frequency slider.

## 9. Repeated-pair and community analysis

**Question:** Which connections persist across the corpus?

Unordered object-pair frequency became the principal simplification mechanism. At pair frequency 3 or greater, the network revealed programmes, exercise systems, hubs, bridges, and coherent communities rather than an arbitrary collection of repeated words.

Pair frequency counts all extracted relation instances connecting two objects, not only the number of supporting videos. The directed relation table separately preserves wording, direction, frequency, and supporting-video IDs.

The stricter threshold revealed the strongest structures. The pair-frequency-2 network remained useful for investigating weaker connections between them.

## 10. Programme-grammar synthesis

**Question:** What does the network imply about Dan John's underlying method?

Directed exercise relations distinguished progressions, regressions, substitutions, combinations, sequencing, comparisons, and functional equivalents. Reading these findings in reverse—from programmes, to exercise systems, to repeated pairs, to object frequency, to individual transcripts—revealed a programme-generating grammar:

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

The corpus does not collapse into one compulsory programme. It does preserve an essence: maximise useful, sustainable improvement while minimising unnecessary time, effort, complexity, and recovery cost.

## Overall progression

```text
Playlist-sized source collection
    ↓
Transcripts
    ↓
Per-video objects and relations
    ↓
Corpus-wide object frequencies
    ↓
Repeated object pairs
    ↓
Relation network
    ↓
Exercise and programme structures
    ↓
Implicit programme-design methodology
    ↓
Minimum representative video set
```

The analysis returns to individual sources at the end. Five videos were the smallest set found to cover the seven recurring exercise systems identified in the relation network. That is a compression of the corpus, not a claim that the remaining videos contain nothing useful.
