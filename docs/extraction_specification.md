# Extraction specification

## Final task

For every available transcript, preserve the official video title and collect objects and relations. This is a collection task, not an instruction for the extractor to build a theory of the corpus.

The final record contains:

- playlist position;
- video ID;
- canonical video URL;
- official title;
- a reference to the source transcript file;
- objects; and
- directed relations between those objects.

Earlier experiments also requested alternative titles, summaries, and semantic maps. Those outputs were useful for learning what the material contained, but they were removed from the corpus-scale extraction because they added interpretation that the later analysis did not require.

## Objects

An object is a meaningful, identifiable thing discussed in the transcript. It may be a person, exercise, programme, method, concept, piece of equipment, organisation, event, place, or another concrete subject of discussion.

Objects are not every noun in the transcript. They should be numerous enough to preserve what is being discussed without inventing an ontology or asking the extractor to decide which objects will later prove important.

Rules:

1. Use the transcript as evidence.
2. Do not invent weakly implied or absent objects.
3. Collapse repetition within one video to one local object.
4. Normalise an obvious caption error only when the intended term is clear.
5. Keep singular and plural labels separate. They may later prove equivalent, but they may also participate in different relations.
6. Object IDs are local to one video. Cross-video identity is established later through normalized labels, not asserted by the record ID.

## Relations

A relation is a meaningful connection which the transcript explicitly states or strongly supports:

```text
primary object → relation wording → secondary object
```

Rules:

1. Both endpoints must exist in that video's object list.
2. Preserve direction as it appears in the transcript.
3. Use concise wording that retains the substance of the connection.
4. Preserve material conditions, attribution, or uncertainty in the wording.
5. Proximity or co-occurrence alone does not establish a relation.
6. Do not ask the extractor to prune, rank, classify, or construct second-order relations. Those are later computations over the collected records.

Examples of relation meanings found later include progression, regression, substitution, composition, sequencing, comparison, and functional equivalence. These were analytical findings, not categories imposed during extraction.

## Evidence boundary

- A questioner's premise is not automatically Dan John's claim.
- Mentioning a view is not the same as endorsing it.
- Conditional advice should not become a universal prescription.
- Unclear automatic captions should not be silently converted into certainty.
- Named systems such as Easy Strength should be distinguished from generic descriptive language when context supports the distinction.

## Final JSON shape

```json
{
  "playlist_position": 1,
  "video_id": "example_id",
  "url": "https://www.youtube.com/watch?v=example_id",
  "official_title": "Official YouTube title",
  "transcript": {
    "file": "../../transcripts/example_id_transcript.txt"
  },
  "objects": [
    {"id": "o1", "label": "first object"},
    {"id": "o2", "label": "second object"}
  ],
  "relations": [
    {"subject": "o1", "relation": "relates to", "object": "o2"}
  ]
}
```

The transcript path is retained as provenance from the private working dataset. Raw transcript files are not distributed in this repository.
