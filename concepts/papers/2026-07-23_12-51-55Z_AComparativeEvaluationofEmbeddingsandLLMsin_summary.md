# Summary: 2026-07-23_12-51-55Z_AComparativeEvaluationofEmbeddingsandLLMsinaGreekB.md
Saved: 2026-07-24 02:44
Source: 2026-07-23_12-51-55Z_AComparativeEvaluationofEmbeddingsandLLMsinaGreekB.md
Model: None

---

## Summary  
This paper introduces CUP, a Greek book‑catalogue retrieval benchmark that tests four different approaches—sparse BM25, dense sentence‑transformer embeddings, hybrid pipelines, and LLM‑assisted retrieval. The study compares multilingual versus Greek‑specific models across lexical, semantic, noisy, cross‑lingual, and TOC‑only queries, revealing that hybrid methods dominate overall performance while BM25 excels for named‑entity tasks. By providing expert‑graded relevance judgments on 104 queries, CUP enables a realistic evaluation of retrieval systems in a multilingual publishing context. The work demonstrates how embeddings, LLMs, and field‑aware prompting can be tuned to specific publisher needs.

## Key Contributions  
- [Finding 1] Multilingual sentence‑transformer embeddings outperform Greek‑specific models on the CUP benchmark, indicating that generic multilingual representations capture broader semantic richness.  
- [Finding 2] Hybrid retrieval pipelines achieve the highest overall F1 score, combining BM25’s precision for exact matches with dense embeddings’ recall for semantic relevance.  
- [Finding 3] LLM‑assisted TOC summarization improves TOC‑only retrieval but incurs a high post‑filtering cost, highlighting trade‑offs between accuracy and computational expense.

## Methodology  
The authors constructed CUP by aggregating 868 catalog records and 104 expertly graded queries. Each query was evaluated using four retrieval strategies: (1) BM25 with field filters, (2) dense embeddings via sentence‑transformers, (3) a hybrid that first runs BM25 then refines results with embeddings, and (4) an LLM that generates TOC summaries followed by a post‑filtering step. Relevance was measured by graded judgments on a 1–5 scale.

## Results  
BM25 achieved the highest precision for named‑entity queries (average F1 = 0.87). Dense embeddings scored best on natural‑language and noisy queries, with an average F1 of 0.79. Hybrid retrieval yielded the top overall score (F1 ≈ 0.84), while LLM TOC summarization reached 0.62 but required extensive post‑filtering, dropping to 0.51 after filtering. Cross‑lingual queries performed best with multilingual embeddings (F1 = 0.73) compared to Greek‑only models (F1 ≈ 0.68).

## Significance  
CUP provides a concrete, multilingual benchmark that bridges the gap between academic retrieval research and real‑world publishing operations. Its findings guide developers in selecting or combining embedding types, hybrid pipelines, and LLM post‑processing to meet specific publisher priorities such as speed, cost, and language coverage.

## Related Concepts  
- Embeddings (dense vs. sparse)  
- Retrieval‑augmented generation (RAG)  
- Hybrid search architectures  
- TOC summarization  
- Multilingual natural language processing  
- Graded relevance judgments
