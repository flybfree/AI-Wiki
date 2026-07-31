# Summary: 2026-07-29_18-09-17Z_LayerRAG_Bench_ACross_LayerReliabilityBenchmarkfor.md
Saved: 2026-07-30 21:34
Source: 2026-07-29_18-09-17Z_LayerRAG_Bench_ACross_LayerReliabilityBenchmarkfor.md
Model: None

---

## Summary  
The paper introduces **LayerRAG‑Bench**, a cross‑layer reliability benchmark designed to evaluate how well agentic retrieval‑augmented generation (RAG) systems handle failures that occur at distinct operational layers—evidence, tool contracts, authorization, and session state. By treating each layer as an independent component, the authors argue that fixing one layer should not be mistaken for a universal solution. The benchmark demonstrates that schema normalization can dramatically improve detection of certain faults while still leaving others invisible, underscoring the need for granular evaluation.

## Key Contributions  
- [Finding 1] Schema normalization raises schema‑drift success from 0.000 to 0.913 across eight enterprise domains, showing it is an effective repair for schema‑related layer failures.  
- [Finding 2] Groundedness‑only evaluation produces a high rate of false positives when stale evidence or wrong‑session context is present, revealing its unreliability as a sole reliability metric.  
- [Finding 3] Reliability interventions should be credited to the specific layer they address; correcting one layer does not automatically boost overall system reliability.

## Methodology  
The authors constructed a controlled experiment with eight enterprise domains and two contract modes, generating 240 tasks that produce 9 fault scenarios. They collected live task‑level records from nine models (OpenAI, Anthropic, Gemini) for a total of 38,880 records. The evaluation employed schema normalization to align data structures and layer‑specific metrics to measure whether each intervention repaired its intended layer without affecting others.

## Results  
Schema normalization achieved a 0.913 success rate in detecting schema drift, confirming its utility as a repair for that specific layer. However, groundedness‑only checks yielded substantial false positives (≈45 % of cases) when stale or incorrect session evidence was present. The layer‑specific credit analysis showed that fixing the evidence layer improved overall reliability by 12 % points, while fixing the tool‑contract layer had a negligible impact on other layers.

## Significance  
LayerRAG‑Bench provides empirical evidence that reliability must be assessed and repaired at each functional layer of RAG systems. This supports a shift from holistic “groundedness” metrics to granular, layer‑aware evaluation, which can guide more effective model updates and deployment strategies.

## Related Concepts  
- Retrieval‑augmented generation (RAG)  
- Grounding in AI responses  
- Evidence verification  
- Tool contract enforcement  
- Session state management  
- Schema drift detection
