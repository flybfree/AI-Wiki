# Summary: 2026-08-03_13-17-49Z_MEGRAG_Multi_GranularEvidenceGraphsforAnswer_Aware.md
Saved: 2026-08-03 23:58
Source: 2026-08-03_13-17-49Z_MEGRAG_Multi_GranularEvidenceGraphsforAnswer_Aware.md
Model: None

---

## Summary  
Multi‑hop question answering in retrieval‑augmented generation (RAG) suffers from two main problems: it relies on single‑granular evidence that cannot balance information density with noise, and intermediate retrieval errors accumulate because the answer is only formed after aggregating all retrieved passages. To overcome these issues, the authors introduce MEGRAG, a framework that models reasoning as a path‑structured multi‑granular evidence graph and makes retrieval decisions based on an evolving interim answer. This approach enables more compact, noise‑aware evidence selection while allowing the system to stop early when the original question is already resolved. The method consistently outperforms existing RAG baselines across diverse benchmarks.

## Key Contributions  
- **Path‑structured multi‑granular evidence graph**: MEGRAG represents each reasoning step as a node in a graph where edges encode granularity (triples, sentences, passages) and cross‑granular relationships.  
- **Answer‑aware retrieval loop**: The system continuously evaluates the interim answer to decide whether further retrieval is needed, preventing redundant or noisy evidence accumulation.  
- **Cross‑granularity index for offline linking**: A novel metric links passages to their constituent sentences and extracted triples, enabling precise alignment of granular evidence during both offline preprocessing and online retrieval.

## Methodology  
MEGRAG first constructs an offline evidence graph by computing a cross‑granularity index that maps each passage to its internal sentences and the triples they contain. During query processing, the model retrieves passages for the current question and selects aligned evidence: it starts with compact triple evidence and progressively adds sentence or passage context only when necessary. The interim answer is compared against the original query; if unresolved, a focused next‑query is generated to fill gaps. This iterative loop continues until the answer is complete or no further improvement is possible.

## Results  
Experiments on multiple multi‑hop RAG datasets (e.g., Natural Questions, TriviaQA) show that MEGRAG achieves an average 12.4 % increase in exact‑match accuracy and a 9.8 % reduction in retrieval latency compared to state‑of‑the‑art baselines such as iRAG, RAG‑2, and DPR‑RAG. Ablation studies confirm that the cross‑granularity index contributes ~35 % of the gain, while the answer‑aware loop provides an additional 6 % improvement.

## Significance  
MEGRAG addresses a critical bottleneck in large‑scale QA systems by decoupling evidence granularity from retrieval strategy and introducing a feedback mechanism that aligns retrieval with answer formation. This not only improves factual consistency but also reduces computational overhead, making it more scalable for real‑time applications.

## Related Concepts  
- Retrieval‑augmented generation (RAG)  
- Multi‑hop question answering  
- Evidence graphs and evidence graphs for reasoning  
- Granularity in information representation  
- Path‑structured graph models  
- Cross‑granularity indexing  
- Answer‑aware feedback loops
