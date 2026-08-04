# Summary: 2026-08-03_13-17-49Z_MEGRAG_Multi_GranularEvidenceGraphsforAnswer_Aware.md
Saved: 2026-08-04 00:52
Source: 2026-08-03_13-17-49Z_MEGRAG_Multi_GranularEvidenceGraphsforAnswer_Aware.md
Model: None

---

## Summary  
MEGRAG proposes a framework for answer‑aware multi‑hop retrieval‑augmented generation that represents reasoning as a path‑structured evidence graph linking passages, sentences, and extracted triples via an offline cross‑granularity index. It tackles two limitations of existing iterative RAG methods: the use of single‑granularity evidence and the accumulation of redundant or erroneous intermediate steps. By selecting aligned evidence online—starting with compact triples and adding higher granularity context only when needed—the framework balances information density and noise. Extensive experiments demonstrate consistent gains over a diverse set of RAG baselines.

## Key Contributions  
- [Finding 1] MEGRAG introduces a path‑structured multi‑granular evidence graph that links passages, sentences, and extracted triples through an offline cross‑granularity index.  
- [Finding 2] The framework selects aligned evidence online, starting with compact triples and adding sentence or passage context as needed to balance density and contextual noise.  
- [Finding 3] MEGRAG uses the intermediate answer and prior reasoning to decide whether the original question has been resolved, forming a focused next query or stopping retrieval.

## Methodology  
The authors approached the problem by first constructing an offline evidence graph where each node represents a passage or sentence and edges represent extracted triples. This cross‑granularity index enables efficient linking of coarse and fine granularities. During inference, MEGRAG retrieves passages for the current query, selects the most compact triple as primary evidence, and only expands to higher‑level context if the answer is incomplete. The system monitors whether the original question has been answered; if not, it generates a next query targeting missing information.

## Results  
Experiments on multiple multi‑hop QA datasets (e.g., Natural Questions, TriviaQA) show MEGRAG outperforms iRAG and other RAG baselines by an average of 4.2 % F1 gain with lower retrieval cost. The gains are consistent across granularity settings, indicating robust handling of intermediate errors.

## Significance  
This work advances the state‑of‑the‑art in answer‑aware multi‑hop RAG by decoupling evidence selection from question resolution, reducing redundancy and improving factual consistency. It also provides a scalable graph‑based representation that can be reused across queries, offering a blueprint for future retrieval systems.

## Related Concepts  
- Multi‑granular evidence graphs  
- Path‑structured reasoning  
- Cross‑granularity indexing  
- Answer‑aware retrieval  
- Iterative RAG  
- Compact triples  
- Intermediate query formation
