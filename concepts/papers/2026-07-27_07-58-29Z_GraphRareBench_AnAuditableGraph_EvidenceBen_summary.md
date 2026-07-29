# Summary: 2026-07-27_07-58-29Z_GraphRareBench_AnAuditableGraph_EvidenceBenchmarkf.md
Saved: 2026-07-28 20:17
Source: 2026-07-27_07-58-29Z_GraphRareBench_AnAuditableGraph_EvidenceBenchmarkf.md
Model: None

---

## Summary  
The paper introduces GraphRareBench, an auditable benchmark for phenotype‑driven rare‑disease diagnosis that preserves provenance and explicitly tracks which plausible alternatives are ranked above the target disease. It provides a data set of 2,365 ontology‑derived cases with 18,093 target‑confounder pairs, each containing hard confounders defined by graph structures and source‑linked evidence records. The goal is to evaluate how diagnostic models access and interpret this evidence beyond simple ranking scores. This work establishes a foundation for more transparent and evidence‑aware evaluation of rare‑disease diagnostic systems.

## Key Contributions  
- GraphRareBench constructs an auditable benchmark with 2,365 ontology‑derived cases and 18,093 target‑confounder pairs.  
- The benchmark demonstrates that full‑pool retrieval, hard‑confounder discrimination, and evidence access each capture distinct aspects of model behavior.  
- Experimental results show MRRs between 0.64–0.74 for supervised rankers and comparable performance for large language models like DeepSeek‑V4‑Flash, with a notable evidence‑coverage gap of 0.561.

## Methodology  
The authors designed a provenance‑preserving dataset where each case includes a coarsened HPO query, a fixed candidate pool, graph‑defined hard confounders, and source‑linked evidence records; they split the data into a 237‑case gene‑component‑disjoint test set and used a shared 21‑feature interface for supervised rankers.

## Results  
Supervised rankers achieved MRR values of 0.640–0.740 and target‑over‑confounder accuracy ranging from 0.898 to 0.916; DeepSeek‑V4‑Flash reached an MRR of 0.718 while Agents‑A1 obtained 0.746, the difference not statistically significant but highlighting a 0.561 disparity in evidence coverage.

## Significance  
This work moves beyond rank‑only reporting to reveal which plausible alternatives are ranked above the target and what evidence is examined, enabling transparent evaluation of diagnostic models and guiding improvements in evidence‑aware reasoning for rare‑disease diagnosis.

## Related Concepts  
Ontology‑derived case generation, provenance preservation, graph‑defined hard confounders, source‑linked evidence records, MRR (Mean Reciprocal Rank), target‑over‑confounder accuracy, full‑pool retrieval, evidence coverage.
