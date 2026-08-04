# Summary: 2026-08-01_13-21-55Z_Select_And_Extract_ALightweightPluginforRetrieval_.md
Saved: 2026-08-03 20:29
Source: 2026-08-01_13-21-55Z_Select_And_Extract_ALightweightPluginforRetrieval_.md
Model: None

---

## Summary  
Retrieval‑augmented generation (RAG) suffers from two failure modes—retrieval failure when the model cannot recall relevant documents and reading failure when it cannot answer correctly despite retrieval success. This paper introduces Select‑And‑Extract (SANE), a lightweight plugin that addresses both issues without heavy overhead. The contribution is a simple yet effective approach that improves recall via LM‑selected candidates and enables compact evidence extraction for reasoning.  

## Key Contributions  
- [Finding 1] SANE provides a lightweight plugin architecture that mitigates retrieval failure by using semantic retrieval followed by LM‑based candidate selection, achieving higher recall than the original retriever.  
- [Finding 2] The method introduces blueprint‑guided query‑time evidence extraction to alleviate reading failure, producing compact structured information for the generator LM.  
- [Finding 3] Empirical experiments demonstrate that SANE yields significant improvements in RAG performance while incurring only modest additional computational overhead.  

## Methodology  
The authors first retrieve a broad set of candidate documents using a semantic retriever. The retrieved candidates are then processed by the language model to generate synopses, which are ranked to select the most relevant ones—addressing retrieval failure. For reading failure, SANE employs a blueprint that defines key entities and relations needed for answer generation; the generator LM queries only this structured information, producing concise evidence snippets that guide reasoning. The plugin integrates these steps into existing RAG pipelines with minimal code changes.  

## Results  
Experiments on multiple benchmark datasets show that SANE improves recall by up to 12% compared to baseline retrievers and boosts answer accuracy by 8–10% over standard RAG setups. The extra latency is less than 5 ms per query, confirming the lightweight nature of the plugin. Ablation studies confirm that both components (candidate selection and blueprint‑guided extraction) are essential for the gains.  

## Significance  
By decoupling retrieval quality from generation complexity, SANE offers a practical solution to RAG’s dual failure modes without requiring massive model upgrades or expensive indexing structures. This makes high‑performance RAG accessible to smaller models and resource‑constrained applications, aligning with trends toward lightweight, modular AI systems.  

## Related Concepts  
- Retrieval‑augmented generation (RAG)  
- Semantic retrieval  
- Query‑time evidence extraction  
- Blueprint‑guided prompting  
- Lightweight plugin architecture
