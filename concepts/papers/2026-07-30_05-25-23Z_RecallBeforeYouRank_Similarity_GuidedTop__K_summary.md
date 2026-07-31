# Summary: 2026-07-30_05-25-23Z_RecallBeforeYouRank_Similarity_GuidedTop__K_Reusef.md
Saved: 2026-07-30 21:39
Source: 2026-07-30_05-25-23Z_RecallBeforeYouRank_Similarity_GuidedTop__K_Reusef.md
Model: None

---

## Summary  
The paper introduces ReTopK, a training‑free method that accelerates dynamic Top‑K sparse attention by reusing historical retrieval decisions instead of recomputing them from scratch each step. By exploiting the observation that similar queries attend to overlapping key‑value supports, ReTopK builds a bounded cache of past query–support pairs and unions their stored supports with a recent window before performing an exact rerank on this compact candidate set. This approach reduces the selector cost from linear in context length to constant per attention head while retaining full access to the KV cache. The method also includes a similarity‑based fallback that switches to full‑history Exact Top‑K when reuse is unreliable and periodic exact refreshes limit cache drift.

## Key Contributions  
- Similarity‑guided Top‑K reuse preserves most of the exact Top‑K attention mass even when supports only partially overlap.  
- A bounded historical cache eliminates per‑head linear scoring by reusing stored support indices instead of recomputing scores.  
- Periodic exact refreshes prevent cache drift, ensuring that the cached supports remain useful over long decoding sequences.

## Methodology  
For each attention head ReTopK maintains a small cache of recent query–support pairs. When a new query arrives, it retrieves the most similar cached queries from this bounded set and unions their stored support indices with the current window of KV entries. The resulting candidate set is then reranked using only the exact scores computed for the current query; any remaining candidates are handled by a similarity‑based fallback that falls back to full‑history Exact Top‑K when reuse is deemed unreliable. To keep the cache fresh, the system performs periodic exact refreshes that replace stale entries and limit drift.

## Results  
Across contexts ranging from 16 K to 128 K tokens, ReTopK achieves the lowest PG19 perplexity and the highest scores on NIAH and LongBench among all evaluated approximate methods. At a context length of 128 K with K=512, ReTopK incurs only a 0.50 % increase in perplexity compared to Exact Top‑K while accelerating attention computation by a factor of 3.07×.

## Significance  
ReTopK enables efficient long‑context decoding for large language models without any training overhead, dramatically reducing the computational cost of the selector that dominates sparse attention performance. By reusing similar queries and limiting exact reranking to a compact candidate set, it offers a practical path toward scaling LLMs to very long contexts while preserving high quality.

## Related Concepts  
Top‑K sparse attention, KV cache, selector cost, similarity‑based retrieval, exact vs approximate Top‑K selection, cached supports, cache drift, LongBench benchmark, NIAH benchmark, PG19 perplexity.
