# Summary: 2026-07-31_18-06-58Z_Evidence_UnitFairnessandtheLimitsofQuery_AdaptiveS.md
Saved: 2026-08-03 23:48
Source: 2026-07-31_18-06-58Z_Evidence_UnitFairnessandtheLimitsofQuery_AdaptiveS.md
Model: None

---

## Summary  
The paper tackles evidence‑unit fairness in financial document retrieval, where short, acronym‑laden queries must locate dense answers hidden inside long, table‑rich 10‑K filings. It investigates a sparse‑dense hybrid system on the FinDER benchmark and discovers that using encoder windows larger than the evidence units biases results because the dense model never sees most of the labeled text. The authors also explore query‑adaptive fusion weights, finding theoretical headroom but no reliable practical gain from lightweight adaptive routers.

## Key Contributions  
- [Finding 1] If the retrieval unit exceeds the dense encoder’s input window, the dense model receives only a small fraction of the evidence, skewing comparisons against a full‑text sparse baseline.  
- [Finding 2] Segmenting the corpus into encoder‑sized windows removes this bias and boosts reference‑level Hit@10 by roughly 28 % over either component alone.  
- [Finding 3] An oracle interpolation‑weight grid suggests up to a 21.8 % improvement, yet three lightweight adaptive routers (score‑confidence heuristic, random forest on query features, ridge regressor on embeddings) do not achieve statistically significant gains under cluster‑robust cross‑validation.

## Methodology  
The authors construct a sparse retriever using BM25 and a compact dense encoder trained on 10‑K filings. They evaluate reciprocal rank fusion of the two outputs and test three query‑adaptive routing strategies across the FinDER benchmark, employing company‑grouped cross‑validation with cluster‑robust inference to assess statistical reliability.

## Results  
After correcting for evidence‑unit bias, Hit@10 improves by about 28 % relative to either component. The theoretical maximum improvement from adaptive fusion is 21.8 %, but none of the three proposed adapters yields a statistically reliable gain; the fixed blend remains the most dependable approach.

## Significance  
Understanding evidence‑unit fairness clarifies why naïve per‑query weighting does not unlock extra performance, guiding researchers toward more robust baseline designs and preventing misleading comparisons in financial document retrieval systems.

## Related Concepts  
evidence‑unit fairness, sparse‑dense fusion, query‑adaptive routing, reciprocal rank fusion, 10‑K filings, FinDER benchmark, dense encoder input window, headroom, statistical reliability.
