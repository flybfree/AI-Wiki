# Summary: 2026-07-23_12-51-55Z_AComparativeEvaluationofEmbeddingsandLLMsinaGreekB.md
Saved: 2026-07-24 02:59
Source: 2026-07-23_12-51-55Z_AComparativeEvaluationofEmbeddingsandLLMsinaGreekB.md
Model: None

---

## Summary  
The authors introduce CUP, a Greek book‑catalog retrieval benchmark that contains 868 catalog records and 104 expert‑annotated queries graded for relevance. Their goal is to compare sparse BM25, dense sentence‑transformer embeddings, hybrid approaches, and LLM‑assisted methods in this real‑world publishing context. They find that multilingual embeddings outperform Greek‑specific models, while a hybrid retrieval strategy yields the highest overall performance. The study also reveals query‑level effects of each method on different types of queries.  

## Key Contributions  
- Multilingual dense embeddings surpass Greek‑specific models in retrieval quality.  
- Hybrid retrieval methods achieve the best overall performance across the CUP dataset.  
- BM25 excels at named‑entity queries, whereas dense and hybrid approaches improve natural‑language, noisy, cross‑lingual, and concept queries; field‑aware prompting has model‑specific effects, and LLM TOC summarization boosts TOC‑only retrieval while post‑filtering improves early‑stage retrieval at a high cost.  

## Methodology  
The authors construct the CUP dataset, which comprises 868 catalog records and 104 expert‑annotated queries with graded relevance judgments. They evaluate four retrieval strategies: (1) sparse BM25, (2) dense sentence‑transformer embeddings, (3) hybrid (BM25 + dense), and (4) LLM‑assisted retrieval that includes TOC summarization and post‑filtering. Multilingual embeddings are compared with Greek‑specific models, and field‑aware prompting is applied to the LLM component for TOC tasks.  

## Results  
Multilingual dense embeddings consistently outperform Greek‑specific models across all query types. The hybrid approach (BM25 + dense) yields the highest average relevance score. BM25 performs best on queries that contain explicit named entities, while dense and hybrid methods improve performance on natural‑language, noisy, cross‑lingual, and concept queries. Field‑aware prompting shows that LLM TOC summarization benefits TOC‑only retrieval but does not help general queries; conversely, LLM post‑filtering enhances early‑stage recall at the expense of higher computational cost.  

## Significance  
CUP provides a comprehensive benchmark for evaluating Greek book‑catalog retrieval systems, covering lexical, semantic, noisy, and cross‑lingual query patterns. By quantifying the trade‑offs between sparse, dense, hybrid, and LLM methods, CUP guides publishers in selecting or combining techniques that best serve their specific catalog needs.  

## Related Concepts  
Embeddings (dense sentence‑transformers), BM25, hybrid retrieval, Large Language Models (LLMs), field‑aware prompting, TOC summarization, multilingual vs domain‑specific models, relevance judgments, query‑level analysis, and cross‑lingual search.
