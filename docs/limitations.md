# Limitations

- The source material is automatic-caption text. Names, numbers, punctuation, and speaker boundaries can be wrong.
- Two source entries did not have usable transcripts and are absent from the analytical records. One unrelated transcript was identified and removed, leaving 382 records.
- Object and relation extraction involves judgement. It is systematic, not infallible.
- Normalized labels are useful aliases, not a finished ontology. Some synonyms remain separate; some superficially similar labels may refer to different things.
- Singular and plural labels were deliberately kept separate because they may participate in different relations.
- Relation wording varies. Pair frequency is robust to that variation, but it also discards direction and meaning unless the underlying directed statements are inspected.
- Frequency measures recurrence, not truth, endorsement, causal force, or training effectiveness.
- Thresholds simplify the network. The pair-frequency-3 view reveals strong repeated structures but fragments weaker bridges into separate components.
- Community names and the inferred programme grammar are interpretations of computed structures, not categories already present in the extracted data.
- Some relation directions are inconsistent, especially where a speaker describes exercises as interchangeable or as context-dependent progressions.
- The notebook's graph layout is a navigational device. Distance on the canvas is not itself an analytical result.
- The final corpus extraction was performed with Codex 5.6 Sol at extra-high reasoning. Earlier GPT-4.1 and GPT-4.1 mini experiments are documented separately and are not mixed into the final dataset.
- Raw transcripts are excluded from this repository for privacy, copyright, and repository-size reasons. Claims should ultimately be checked against the linked public video where necessary.
