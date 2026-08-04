# Summary: 2026-08-03_12-10-51Z_DoStaticEmbeddingsAddValuetoHybridDutchRetrieval.md
Saved: 2026-08-03 23:53
Source: 2026-08-03_12-10-51Z_DoStaticEmbeddingsAddValuetoHybridDutchRetrieval.md
Model: None

---

## Summary  
The paper investigates whether static embedding models can provide marginal ranking improvements when combined with lexical BM25 and a large‑scale transformer (Qwen) in hybrid Dutch retrieval. By evaluating the Massive Text Embedding Benchmark for Dutch (MTEB‑NL), the authors show that adding two multilingual static embeddings to the best‑matching 25 (BM25‑Qwen) pair yields measurable gains on four of five datasets, while leaving one dataset unchanged. Their controlled experiments demonstrate that the value of static embeddings is context‑dependent and cannot be inferred from standalone benchmark scores alone.

## Key Contributions  
- [Finding 1] Adding two multilingual static embedding models to BM25‑Qwen improves mean reciprocal rank (MRR) by 0.061 on Dutch News, 0.029 on VABB, 0.004 on WebFAQ NL, and 0.025 on Wikipedia NL, all statistically significant after Holm correction.  
- [Finding 2] No unrestricted selection of fusion weights assigns positive weight to either static retriever; optimal performance occurs when both static models are excluded, indicating that forcing their contribution degrades results.  
- [Finding 3] Leave‑one‑dataset‑out (LOOD) selection yields equal BM25‑Qwen weighting across all tasks and outperforms the cross‑domain‑selected individual retriever on every held‑out task.

## Methodology  
The authors conduct a controlled exhaustive search over five Dutch retrieval datasets, each containing 14,500 queries and 786,573 documents. They use weighted reciprocal rank fusion (RRF) to combine BM25, Qwen’s 0.6B embedding model, and two static multilingual embeddings. Fusion weights are varied on a simplex in increments of 0.1, and ten‑fold query‑level cross‑validation selects weights on nine folds while evaluating the tenth held‑out fold. Pairwise bootstrap confidence intervals and sign‑randomisation tests quantify differences between fusion and individual retrievers. The LOOD strategy forces equal BM25‑Qwen weighting in each iteration.

## Results  
Fusion consistently improves over the training‑selected individual retriever on Dutch News (+0.061 MRR), VABB (+0.029 MRR), WebFAQ NL (+0.004 MRR) and Wikipedia NL (+0.025 MRR). On Open Tender, fusion matches BM25 alone. All positive differences survive Holm correction (p < 0.05). LOOD selection never assigns a positive weight to static embeddings; the best weights lie on the BM25‑Qwen edge. The mean reciprocal rank gains are modest but statistically reliable.

## Significance  
These findings challenge the assumption that standalone embedding benchmarks can predict hybrid retrieval performance, highlighting the importance of empirical evaluation across domain‑specific tasks. They support a default two‑retriever architecture (BM25 + Qwen) for Dutch queries while cautioning against unnecessary static embeddings when they do not add value.

## Related Concepts  
- Hybrid Retrieval: Combining lexical and neural models.  
- Reciprocal Rank (MRR): Ranking metric for retrieval.  
- Weighted Fusion: Optimizing combination of retriever scores.  
- Static Embeddings: Pre‑computed vector representations without fine‑tuning.  
- Leave‑One‑Dataset‑Out (LOOD) Evaluation: Cross‑domain validation strategy.
