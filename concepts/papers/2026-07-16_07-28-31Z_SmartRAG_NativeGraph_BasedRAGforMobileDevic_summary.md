# Summary: 2026-07-16_07-28-31Z_SmartRAG_NativeGraph_BasedRAGforMobileDevice.md
Saved: 2026-07-23 23:45
Source: 2026-07-16_07-28-31Z_SmartRAG_NativeGraph_BasedRAGforMobileDevice.md
Model: None

---

## Summary  
The paper proposes SmartRAG, a native graph‑based Retrieval‑Augmented Generation framework designed for mobile devices that must balance privacy, low latency, offline availability, and strict hardware budgets while keeping LLM inference costs manageable. It decomposes on‑device intelligence into four coordinated modules—Perception, Memory, Focus, and Thinking—and introduces EvoNER, a continually learnable named‑entity recognizer, together with MRGraph, a three‑layer provenance‑preserving knowledge graph. Knowledge is retrieved via a hybrid pipeline that combines graph traversal, lexical matching, and dense semantic search, and the LLM is invoked only for high‑value tasks such as labeling, planning, and answer synthesis.

## Semantic links
- [[concepts/papers/2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningw_summary.md|Summary: 2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningwithEner.md]] — 3 title terms overlap; 8 backlinks; 14 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 10 summary/topic terms overlap
- [[concepts/papers/2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMult_summary.md|Summary: 2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMulti_Agent.md]] — 3 title terms overlap; 17 backlinks; 11 summary/topic terms overlap

## Key Contributions  
- SmartRAG integrates continual named‑entity recognition with a three‑layer knowledge graph to enable offline, low‑cost reasoning on smartphones.  
- The framework reduces LLM inference to essential semantic operations while preserving multi‑hop reasoning performance comparable to models up to 18× larger.  
- Experiments demonstrate that a quantized 1.7B‑parameter backbone achieves results competitive with much larger models under practical memory and latency constraints.

## Methodology  
The authors address the tension between model size and edge hardware by decomposing intelligence into modules; EvoNER uses teacher‑distilled updates to expand its label inventory without retraining the backbone LLM, thereby allowing continual learning of unseen entity types. Extracted knowledge is stored in MRGraph—a three‑layer graph that preserves provenance across perception, memory, focus, and thinking layers. Retrieval at query time combines graph traversal (to follow provenance), lexical matching (to find syntactically similar patterns), and dense semantic search (to capture meaning similarity). The on‑device LLM is only called for labeling, planning, and answer synthesis, keeping inference costs bounded.

## Results  
On four QA benchmarks—TriviaQA, Natural Questions, HotpotQA, MultiHopQA—the SmartRAG system with a quantized 1.7B‑parameter backbone matches or exceeds the performance of models up to 18× larger while running entirely on commodity smartphones within practical memory and latency envelopes.

## Significance  
This work enables truly private, offline personal assistants that can perform complex multi‑hop reasoning without cloud reliance, expanding LLM applicability to resource‑constrained devices and addressing longstanding trade‑offs between model size and edge hardware limits.

## Related Concepts  
Retrieval‑Augmented Generation (RAG), continual learning, knowledge graphs, graph traversal, semantic search, model quantization, edge AI, provenance preservation.
