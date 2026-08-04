# Summary: 2026-08-02_00-08-44Z_PracticalOnlineKVCacheCompactionforLLMAgents_AnEmp.md
Saved: 2026-08-03 20:32
Source: 2026-08-02_00-08-44Z_PracticalOnlineKVCacheCompactionforLLMAgents_AnEmp.md
Model: None

---

## Summary  
The paper tackles the KV‑cache bottleneck that arises in LLM agents by proposing online compaction techniques that compress intermediate reasoning steps without requiring offline knowledge of future queries. It evaluates two primary strategies—token eviction (TE) and attention matching (AM)—using cheap proxy queries such as boundary, repeat‑prefill, and delayed‑future‑generation queries. Experiments on benchmark datasets show that immediate compaction often harms performance, whereas delaying compaction to leverage the agent’s own future queries recovers most of the cost reduction. TE is found to be more robust than AM under imperfect proxy conditions.

## Key Contributions  
- [Finding 1] Online compaction can reduce KV‑cache size while preserving accuracy when compaction is delayed until future queries are available.  
- [Finding 2] Token eviction (TE) outperforms attention matching (AM) under cheap proxy queries and imperfect conditions.  
- [Finding 3] Delaying compaction to use the agent’s own future queries recovers most of the performance gap lost by immediate compaction.

## Methodology  
The authors adapt TE and AM to compress agent turns by selecting inexpensive proxy queries that approximate relevance without knowing the exact future content. They evaluate these proxies—boundary, repeat‑prefill, delayed‑future‑generation—across multiple model scales on the BrowseComp‑Plus and WideSearch datasets. The study measures KV‑cache reduction, accuracy loss, and throughput, comparing immediate versus delayed compaction strategies to establish their relative effectiveness.

## Results  
Immediate TE reduces the KV‑cache by roughly 80 % with only a minimal drop in accuracy, and it improves inference throughput over the no‑compaction baseline. Delayed compaction restores most of the performance gap that immediate compaction creates, whereas AM suffers higher cost and lower robustness under proxy constraints.

## Significance  
This work establishes a practical design principle for online KV compaction: selecting the right proxy query is essential for balancing memory savings with accuracy. By demonstrating that TE can achieve substantial cache compression while remaining robust, the study enables scalable LLM agents that operate efficiently in long‑running reasoning environments.

## Related Concepts  
KV cache, token eviction, attention matching, proxy queries, online compression, LLM agents, inference bottleneck, benchmark datasets (BrowseComp‑Plus, WideSearch).
