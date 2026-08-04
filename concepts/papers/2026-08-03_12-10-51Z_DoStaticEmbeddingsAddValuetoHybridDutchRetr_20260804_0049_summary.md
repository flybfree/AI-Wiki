# Summary: 2026-08-03_12-10-51Z_DoStaticEmbeddingsAddValuetoHybridDutchRetrieval.md
Saved: 2026-08-04 00:49
Source: 2026-08-03_12-10-51Z_DoStaticEmbeddingsAddValuetoHybridDutchRetrieval.md
Model: None

---

## Summary  
The paper investigates whether static embeddings can provide marginal ranking benefit when combined with a low‑cost retriever in hybrid Dutch retrieval. It evaluates this question on the Massive Text Embedding Benchmark for Dutch (MTEB‑NL) using five diverse datasets and performs exhaustive weighted reciprocal rank fusion of BM25, Qwen/Qwen3‑Embedding‑0.6B, and two multilingual static models. The study uses a simplex search across 0.1 increments and ten‑fold query‑level cross‑validation to select optimal weights while quantifying significance with paired bootstrap confidence intervals and sign‑randomisation tests.  

## Key Contributions
- [Finding 1] Adding a static retriever improves mean reciprocal rank (MRR) by 0.061 on Dutch News, 0.029 on VABB, 0.004 on WebFAQ NL and 0.025 on Wikipedia NL, all statistically significant after Holm correction.  
- [Finding 2] No unrestricted weight selection yields a positive contribution from the static retriever; all 50 simplex selections lie on the BM25‑Qwen edge, indicating that forcing a static component can reduce effectiveness.  
- [Finding 3] Leave‑one‑dataset‑out selection with equal BM25‑Qwen weighting outperforms cross‑domain‑selected individual retrievers on every held‑out task.  

## Methodology  
The authors adopt a controlled experimental design across the MTEB‑NL corpus, which contains 14 500 queries and 786 573 documents. They implement weighted reciprocal rank fusion (RRF) that merges BM25, Qwen/Qwen3‑Embedding‑0.6B, and two static embedding models. Fusion weights are explored on a simplex in increments of 0.1; ten‑fold cross‑validation selects weights per query set while the held‑out fold is evaluated. To assess significance, paired bootstrap confidence intervals and sign‑randomisation tests quantify differences between training‑selected versus optimal weight configurations.  

## Results  
The fusion consistently raises MRR compared with the best individual retriever on four of the five datasets; all positive gains survive multiple statistical corrections. However, when unrestricted weights are allowed, no selection assigns a non‑zero weight to either static model, and any forced static contribution diminishes performance. The leave‑one‑dataset‑out strategy, which equally weights BM25 and Qwen across folds, yields the highest held‑out MRR on every task, outperforming the cross‑domain‑selected individual retriever.  

## Significance  
These findings demonstrate that standalone benchmark scores are insufficient to detect marginal value in hybrid retrieval systems. The results support a two‑retriever lexical‑transformer architecture as a robust default for Dutch tasks and highlight the importance of evaluating incremental improvements rather than absolute performance. This work contributes to more nuanced evaluation frameworks that can guide practical deployment decisions.  

## Related Concepts  
embedding benchmarks, lexical retrieval (BM25), transformer‑based retrieval (Qwen/Qwen3‑Embedding‑0.6B), static embeddings, weighted reciprocal rank fusion, MTEB‑NL dataset, mean reciprocal rank (MRR), hybrid architecture, retrieval weighting, cross‑domain selection, simplex search, bootstrap confidence intervals, sign‑randomisation tests.
