title: "Summary: 2026-06-19_15-50-35Z_DissectingAgenticRAG_AComponentAblationforMulti_Ho.md"
# Summary: 2026-06-19_15-50-35Z_DissectingAgenticRAG_AComponentAblationforMulti_Ho.md
Saved: 2026-06-22 21:00
Source: 2026-06-19_15-50-35Z_DissectingAgenticRAG_AComponentAblationforMulti_Ho.md
Model: None

---


## Summary  
The paper aims to dissect the components of an agentic retrieval‑augmented generation (RAG) pipeline by conducting a controlled ablation study on a local 7 B language model. It evaluates how each element—retrieval strategy, routing rule, number of iteration loops, and query decomposition—impacts multi‑hop question answering performance using the HotpotQA distractor set. The core contribution is that, under a fixed budget of compute, simpler, non‑adaptive choices often outperform more complex adaptive versions.  

## Key Contributions  
- [Finding 1] Fixed hybrid retrieval via reciprocal rank fusion consistently outperforms rule‑based adaptive routing, delivering +1.8 EM and +1.9 F1 because the routing heuristic over‑routes to BM25 by reacting to named entities in almost every sub‑question.  
- [Finding 2] Two retrieval iterations over decomposed sub‑questions capture roughly 95 % of the gains achieved with five iterations, indicating that deeper loops provide negligible additional benefit.  
- [Finding 3] Query decomposition and cross‑encoder reranking each contribute statistically significant but smaller improvements (p < 0.01 and p < 0.001 respectively).  

## Methodology  
The authors built a full agentic RAG pipeline that includes iterative reasoning loops, query decomposition into sub‑questions, adaptive routing of retrieved passages, and reranking with a cross‑encoder. The system was run on 5,000 HotpotQA questions using only the Qwen2.5‑7B‑Instruct model locally, without any proprietary APIs or large‑scale compute resources. Component‑wise ablation experiments systematically disabled each element to measure its marginal impact on evaluation metrics (EM and F1).  

## Results  
The baseline single‑pass dense retrieval achieved EM = 43.1 % and F1 = 54.0 %. The full pipeline improved these to EM = 53.2 % and F1 = 61.6 %. Among the ablations, fixed hybrid retrieval (reciprocal rank fusion) beat rule‑based adaptive routing by +1.8 EM and +1.9 F1. Running only two retrieval iterations yielded gains comparable to five iterations, with deeper loops adding no meaningful benefit. Query decomposition contributed a modest EM gain (p < 0.01), while cross‑encoder reranking added an even smaller F1 boost (p < 0.001).  

## Significance  
These findings demonstrate that for resource‑constrained settings, the simplicity of fixed hybrid retrieval and a short retrieval loop can be as effective—or more so—than adaptive, multi‑iteration architectures. The study clarifies where added complexity is unnecessary in agentic RAG, guiding developers toward leaner designs that maintain high performance on local 7 B models.  

## Related Concepts  
agentic RAG, retrieval‑augmented generation, multi‑hop QA, hybrid retrieval (reciprocal rank fusion), rule‑based adaptive routing, query decomposition, cross‑encoder reranking, ablation study, local 7 B language model, HotpotQA dataset.
