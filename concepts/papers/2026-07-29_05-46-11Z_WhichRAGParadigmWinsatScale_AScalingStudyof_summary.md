# Summary: 2026-07-29_05-46-11Z_WhichRAGParadigmWinsatScale_AScalingStudyofRetriev.md
Saved: 2026-07-29 22:18
Source: 2026-07-29_05-46-11Z_WhichRAGParadigmWinsatScale_AScalingStudyofRetriev.md
Model: None

---

## Summary  
The paper investigates which retrieval‑augmented generation (RAG) paradigm remains most effective as the corpus size grows, a question that has remained unresolved because prior studies compare models on isolated benchmarks. By constructing a strictly nested ladder of 28 document tiers ranging from ~1 000 to 512 000 items while keeping questions and a fixed set of relevant/adversarial documents constant, the authors provide a controlled view of accuracy‑cost trade‑offs across four RAG approaches: lexical BM25, file‑system agentic search, graph‑based indexing, and native LLM construction. Their study reveals that BM25 defines the low‑cost Pareto frontier at every scale and drives performance forward without relying on generative tokens, while other methods either consume excessive query or generation tokens or plateau early.

## Key Contributions  
- **Finding 1:** BM25 scales best in this controlled setting: it remains the most cost‑effective method across all tiers and its accuracy improves from mid‑scale onward without using LLM‑generated construction.  
- **Finding 2:** The file‑system agent matches or slightly exceeds BM25 at the smallest tiers but consumes roughly 39 times more query tokens per answer at the full scale, falling ~20 points behind native BM25 on the same questions.  
- **Finding 3:** Graph‑based RAG exhibits a construction wall: its heaviest builders use up to 24.6 generative LLM tokens per indexed corpus token yet stop improving within only the first 2 % of the full corpus, leaving scalable variants less accurate than BM25 at shared tiers.

## Methodology  
The authors built a ladder of 28 strictly nested document tiers (≈1 000 → 512 000 documents) while preserving a fixed set of 150 questions and a constant pool of relevant and adversarial documents. For each tier they measured three metrics under a single reader‑judging protocol: official accuracy, total construction tokens, query tokens per answer, and latency. This design isolates the effect of corpus size from question difficulty or data quality.

## Results  
BM25 consistently achieved the lowest cost (construction + query) and defined the Pareto frontier at every tier; its accuracy rose steadily as scale increased. The file‑system agent performed comparably only on the smallest tiers, then sharply degraded due to token inefficiency. Graph‑based RAG’s construction tokens were extremely high (up to 24.6 per corpus token), yet improvements plateaued after a tiny fraction of the full index, leaving its final scores below those of BM25 at comparable scales.

## Significance  
Understanding which RAG paradigm scales reliably is crucial for deploying cost‑effective, high‑quality systems in production. The study clarifies that simple lexical retrieval (BM25) often outperforms complex, token‑heavy approaches when scaling to large corpora, guiding practitioners away from over‑engineered solutions.

## Related Concepts  
Retrieval‑Augmented Generation (RAG), lexical retrieval (BM25), dense retrieval, graph indexing, agentic search, LLM construction tokens, query tokens per answer, latency, Pareto frontier, nested scaling studies.
