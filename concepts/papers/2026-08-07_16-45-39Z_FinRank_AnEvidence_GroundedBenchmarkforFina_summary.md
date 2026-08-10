# Summary: 2026-08-07_16-45-39Z_FinRank_AnEvidence_GroundedBenchmarkforFinancialQu.md
Saved: 2026-08-09 23:09
Source: 2026-08-07_16-45-39Z_FinRank_AnEvidence_GroundedBenchmarkforFinancialQu.md
Model: None

---

## Summary  
FinRank introduces an evidence‑grounded benchmark for financial question answering and retrieval over SEC filings, addressing the problem that a numerically correct answer may be grounded in the wrong passage. The dataset comprises 1 185 manually authored question‑answer records from 22 firms’ 10‑K and 10‑Q filings, each paired with gold supporting passages and hand‑curated hard negatives that span entities, reporting periods, and comparable firms. It evaluates three tasks: passage retrieval, reranking, and hard‑negative discrimination. Baseline experiments show even a 7B instruction‑tuned model reaches only modest recall, highlighting the difficulty of provenance‑sensitive financial QA.

## Key Contributions  
- FinRank introduces a provenance‑sensitive evidence benchmark that requires correct entity, reporting period, and disclosure context for each answer.  
- It creates manually curated hard negatives from confusable passages across reporting periods and comparable firms to test retrieval quality beyond random noise.  
- Experimental results demonstrate the limited performance of large language models: 7B models achieve 44.8% Recall@10; finance‑adapted embedders gain at most 3.5 points over BM25, while hard negatives degrade accuracy by 13–20.5%.

## Methodology  
The authors assembled a dataset of 1 185 records from SEC filings, each containing a reference answer, gold passages, and hand‑curated hard negatives. They evaluate passage retrieval using ranking scores, reranking outputs, and discrimination metrics with both random and hard negatives to isolate the impact of provenance constraints.

## Results  
Main experimental results include a 7B instruction‑tuned embedder achieving Recall@10 of 44.8%, BM25 improving up to 3.5 points over it, a finance‑adapted embedder lagging by 9.7 points, and pairwise accuracy dropping 13–20.5% when hard negatives replace random ones.

## Significance  
This matters because financial QA systems must not only answer correctly but also cite the right disclosure; FinRank provides an evidence‑first benchmark that exposes provenance issues, guiding research toward robust, context‑aware models that respect filing structure and comparability.

## Related Concepts  
- Provenance‑sensitive retrieval  
- Evidence grounding  
- SEC filings (10‑K/10‑Q)  
- Hard negatives  
- Recall@k metric  
- BM25 baseline  
- Large language model embeddings
