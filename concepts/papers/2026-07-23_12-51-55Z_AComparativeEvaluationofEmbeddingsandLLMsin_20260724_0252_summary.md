# Summary: 2026-07-23_12-51-55Z_AComparativeEvaluationofEmbeddingsandLLMsinaGreekB.md
Saved: 2026-07-24 02:52
Source: 2026-07-23_12-51-55Z_AComparativeEvaluationofEmbeddingsandLLMsinaGreekB.md
Model: None

---

## Summary  
The paper introduces the CUP dataset—a Greek book‑catalog benchmark with 868 records and 104 expert‑graded queries—and compares four retrieval approaches (BM25, dense sentence‑transformer embeddings, hybrid retrieval, and LLM‑assisted methods) to evaluate their performance across lexical, semantic, noisy, cross‑lingual, and concept queries. Its main contribution is a systematic, multilingual evaluation that reveals which techniques best suit real‑world Greek publishing needs while highlighting trade‑offs such as cost versus accuracy.

## Key Contributions  
- Multilingual sentence‑transformer embeddings outperform Greek‑specific models on the CUP dataset.  
- Hybrid retrieval (dense + BM25) yields the highest overall performance across varied query styles.  
- LLM post‑filtering improves early‑stage retrieval but incurs a high cost, whereas field‑aware prompting has model‑specific effects.

## Methodology  
The authors constructed CUP containing 868 catalog records and 104 expert‑annotated queries with graded relevance judgments. They evaluated four methods: (1) BM25 (sparse), (2) sentence‑transformer dense embeddings, (3) a hybrid system that combines both, and (4) LLM‑assisted retrieval that includes TOC summarization and post‑filtering. Queries span lexical, semantic, noisy, cross‑lingual, and concept types to capture real‑world diversity.

## Results  
Multilingual embeddings achieve the best average recall (~0.82), while Greek‑specific models lag behind. The hybrid method scores highest overall (average recall ≈ 0.84). BM25 excels for named‑entity queries, reaching 71 % recall. LLM post‑filtering boosts early‑stage retrieval but reduces final recall due to its high computational cost. Field‑aware prompting shows mixed effects: LLM TOC summarization improves TOC‑only retrieval, whereas dense embeddings with field tags enhance concept queries.

## Significance  
This work provides a realistic benchmark for Greek book publishing, enabling practitioners to compare traditional and modern NLP techniques in multilingual settings. By quantifying speed, cost, and accuracy trade‑offs, it guides the selection of retrieval strategies that balance performance with operational constraints.

## Related Concepts  
- Retrieval ranking  
- BM25 (BM25)  
- Sentence‑transformers (dense embeddings)  
- Hybrid retrieval  
- Large language models (LLMs)  
- TOC summarization  
- Field‑aware prompting  
- Dense embeddings  
- Cross‑lingual queries  
- Noisy queries  
- Concept queries
