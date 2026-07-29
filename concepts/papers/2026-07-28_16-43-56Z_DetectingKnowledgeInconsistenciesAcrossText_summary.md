# Summary: 2026-07-28_16-43-56Z_DetectingKnowledgeInconsistenciesAcrossText_Tables.md
Saved: 2026-07-28 23:00
Source: 2026-07-28_16-43-56Z_DetectingKnowledgeInconsistenciesAcrossText_Tables.md
Model: None

---

## Summary  
The paper tackles the practical problem of detecting knowledge inconsistencies that arise when information is stored in three different modalities—text, tables, and knowledge graphs (KGs)—such as Wikipedia and Wikidata. By framing this challenge as *modality‑level inconsistency detection*, it proposes a taxonomy of four types of cross‑modal conflicts and introduces **Kontrast**, an automatic framework that translates table answers into SPARQL queries and leverages large language model reasoning to compare them against KG evidence, thereby categorizing the resulting disagreements.

## Key Contributions  
- [Finding 1] A comprehensive taxonomy of cross‑modal knowledge inconsistencies covering information granularity differences, direct conflicts, temporal changes, and KG incompleteness.  
- [Finding 2] The **Kontrast** framework that automatically detects these inconsistencies by converting text to SPARQL queries and using LLM reasoning for comparison with KG data.  
- [Finding 3] Empirical evidence from multiple Table‑QA datasets showing that cross‑modal inconsistencies are common, informative, and reveal missing KG structure or temporal mismatches.

## Methodology  
The authors adopt a two‑stage pipeline: first, they employ **Text‑to‑SPARQL** to transform natural‑language answers into graph queries; second, an LLM is invoked to reason about the query results. The generated SPARQL output is then compared with the underlying knowledge base (Wikidata or a curated KG). Discrepancies are classified according to the taxonomy and reported with human‑readable explanations, enabling systematic auditing of knowledge sources.

## Results  
Experiments on several Table‑QA benchmarks reveal that cross‑modal inconsistencies occur in roughly 30–40 % of answer‑question pairs. The framework consistently identifies missing triples, outdated facts, and granularity mismatches with high precision. Compared to a baseline that only checks for direct contradictions, **Kontrast** provides richer categorization, improving interpretability and guiding data curation.

## Significance  
By offering an automated tool for large‑scale knowledge auditing, the work helps improve the quality of LLM pre‑training corpora and retrieval‑augmented generation pipelines. It also establishes a benchmark for future research on cross‑modal consistency detection, encouraging systematic comparison among heterogeneous data sources.

## Related Concepts  
Cross‑modal knowledge inconsistency, Text‑to‑SPARQL conversion, SPARQL queries, Knowledge Graph (KG), taxonomy of inconsistencies, Retrieval‑Augmented Generation (RAG), Table‑QA datasets.
