# Summary: 2026-08-07_16-45-39Z_FinRank_AnEvidence_GroundedBenchmarkforFinancialQu.md
Saved: 2026-08-09 23:15
Source: 2026-08-07_16-45-39Z_FinRank_AnEvidence_GroundedBenchmarkforFinancialQu.md
Model: None

---

## Summary  
FinRank introduces an evidence‑grounded benchmark for answering questions in SEC filings, recognizing that a numerically correct answer may be supported by the wrong passage. The authors create a curated dataset of 1 185 question–answer pairs drawn from 22 companies’ 10‑K and 10‑Q reports, each paired with gold passages and hard negatives that are confusable across sections, reporting periods, or comparable firms. By evaluating retrieval, reranking, and discrimination separately, FinRank quantifies how difficult it is to retrieve the correct evidence even for large language models. The benchmark demonstrates that state‑of‑the‑art 7B instruction‑tuned embedders still achieve only modest recall (44.8 @10) and that finance‑adapted encoders lag behind BM25, highlighting a gap between model size and performance in this domain.

## Key Contributions  
- [Finding 1] FinRank tackles provenance‑sensitive retrieval by demanding that evidence be tied to the correct entity, reporting period, and disclosure context within SEC filings.  
- [Finding 2] The benchmark comprises 1 185 manually authored records with gold passages and hard negatives curated from confusable passages across sections, periods, and firms.  
- [Finding 3] Experimental results show that even a 7B instruction‑tuned embedder reaches only 44.8 % Recall@10 on the pooled corpus, while sub‑billion‑parameter encoders gain at most 3.5 points over BM25 and finance‑adapted models trail by 9.7 points.

## Methodology  
The authors assembled a dataset of 10‑K and 10‑Q filings for 22 publicly traded companies, extracting question–answer pairs that are manually verified. For each record they selected the reference answer as gold evidence and generated hard negatives by selecting passages that share similar factual content but belong to different sections, reporting periods, or comparable firms. The evaluation splits focus on three tasks: (1) passage retrieval via embedding similarity, (2) reranking of retrieved candidates, and (3) discrimination between true positives and hard negatives. Baselines include BM25, a 7B instruction‑tuned language model, and a finance‑adapted encoder.

## Results  
On the pooled evidence corpus, the best 7B instruction‑tuned embedder attains 44.8 % Recall@10. Sub‑billion‑parameter encoders improve only marginally, gaining at most 3.5 points over BM25. A finance‑adapted encoder lags behind BM25 by 9.7 points. When random negatives are replaced with the curated hard negatives, pairwise accuracy drops between 13.0 and 20.5 percentage points, underscoring the impact of provenance constraints.

## Significance  
FinRank provides an evidence‑first benchmark that forces financial QA systems to retrieve not only correct answers but also the right supporting disclosure. By exposing the difficulty of provenance‑sensitive retrieval, it guides research toward models that can ground responses in appropriate SEC filings, improving both accuracy and interpretability.

## Related Concepts  
- Provenance‑sensitive retrieval  
- Evidence grounding  
- SEC filing QA  
- Benchmarking for financial NLP  
- Embedding similarity (e.g., BM25)  
- Instruction‑tuned language models
