# Summary: 2026-08-08_15-16-51Z_AGroundedandDecomposedFrameworkforRelation_LevelHa.md
Saved: 2026-08-10 22:57
Source: 2026-08-08_15-16-51Z_AGroundedandDecomposedFrameworkforRelation_LevelHa.md
Model: None

---

## Summary  
Abstractive text summarization often produces fluent yet unfaithful outputs by fabricating or distorting relationships between entities and events. Such relation‑level hallucinations can compromise the reliability of generated summaries, especially in high‑stakes domains such as medical or legal information extraction. This paper introduces a refined, grounded framework that evaluates these hallucinations systematically. The core contribution is a normalized Relation Hallucination Index (RHI) that decomposes and aggregates relation‑specific errors into a single, interpretable faithfulness score.

## Key Contributions  
- [Finding 1] A dependency‑aware relation extraction algorithm that incorporates lemmatization‑based normalization, named entity grounding, passive agent recovery, negation‑aware verb modeling, reporting‑verb filtering, nominal relation fallback, clausal propagation, and systematic deduplication.  
- [Finding 2] A normalized formulation of RHI that ensures scale‑invariant comparison across datasets and models by aggregating the extracted triples into a faithfulness score.  
- [Finding 3] Decomposition of hallucination into interpretable components (e.g., entity grounding errors, verb mis‑alignment) to enable granular analysis.

## Methodology  
The authors approached relation hallucination evaluation as a multi‑stage extraction problem. First, they parse the source text with dependency parsing to identify candidate triples. Lemmatization normalizes forms and aligns entities across sentences. Named entities are resolved using external knowledge bases to ground subjects. Passive constructions are converted into active voice for clearer subject‑predicate alignment. Reporting verbs (e.g., “states that…”) are filtered out, while nominal relations are back‑filled when missing. Clausal propagation propagates relation information through subordinate clauses, and deduplication removes duplicate triples. The final set of normalized triples is fed to RHI, which computes a faithfulness score.

## Results  
Extensive experiments across multiple state‑of‑the‑art abstractive summarization models (e.g., BART, T5, ROUGE‑based baselines) demonstrate that the grounded extraction yields more stable and discriminative hallucination measurements. The normalized RHI correlates strongly with human judgments of relation fidelity, showing a reduction in spurious matches compared to prior metrics. Across datasets such as MSMARCS and CNN/DailyMail, the proposed framework provides comparable or better performance than existing evaluation tools.

## Significance  
This work advances automated relation‑level faithfulness evaluation, offering a transparent metric that can guide model improvement without human annotation. By decomposing hallucination into interpretable components, it supports coherence‑aware analysis of summarization systems, which is crucial for applications where factual consistency is paramount.

## Related Concepts  
abstractive summarization, relation extraction, hallucination, dependency parsing, lemmatization, named entity resolution, passive voice recovery, reporting verbs, nominal relations, normalization, RHI metric.
