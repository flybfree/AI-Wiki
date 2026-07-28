# Summary: 2026-07-27_10-51-38Z_KAP_BridgingtheKnowledgeSelection_RuntimeConsumpti.md
Saved: 2026-07-27 21:36
Source: 2026-07-27_10-51-38Z_KAP_BridgingtheKnowledgeSelection_RuntimeConsumpti.md
Model: None

---

## Summary  
The paper identifies an architectural mismatch between the richly structured knowledge priors selected during prompt construction and the flat, token‑by‑token consumption of those priors at runtime in large language model (LLM) serving systems. This Knowledge Selection‑Runtime Consumption (KSRC) gap inflates KV memory traffic and latency even when only a small fraction of context is needed for reasoning. The authors propose Knowledge Access Planning (KAP), an execution abstraction that treats structured knowledge as first‑class physical artifacts, thereby decoupling logical prompt semantics from dense KV consumption. Their compiler‑executor realization GraphSpec demonstrates a phase‑boundary model that yields positive speed‑ups and dramatically reduces the proportion of KV state accessed at inference time.

## Key Contributions  
- [Finding 1] The KSRC gap is formally characterized as an architectural mismatch where high‑value structured priors (ranked evidence, graph topology, multimodal alignment) are serialized into a prompt but then consumed uniformly across all tokens.  
- [Finding 2] Knowledge Access Planning (KAP) introduces a universal intermediate representation that maps these priors to concrete KV access plans without modifying model weights or training pipelines.  
- [Finding 3] GraphSpec, the KAP implementation, reduces proposal‑time KV consumption to only 5.5 % of the full source KV state at 128K token length while preserving answer quality.

## Methodology  
The authors first modeled the logical prompt as a sequence of knowledge signals and derived an IR that encodes which parts of the KV state should be accessed when. This IR is compiled into GraphSpec, a dual‑purpose artifact: it serves as both a runtime plan and a compiler target for the serving backend. The implementation leverages a phase‑boundary model to predict when each knowledge block becomes active during decoding, allowing early termination of unnecessary KV reads.

## Results  
Experiments on 4K–128K long‑context QA workloads show that GraphSpec maintains answer quality comparable to full‑context decoding. Crucially, the proportion of KV state accessed at inference drops from ~100 % (full prompt) to 5.5 % at 128K tokens, yielding a 94.5 % reduction in proposal‑time memory traffic and measurable latency improvements.

## Significance  
By decoupling logical knowledge selection from dense KV consumption, KAP shifts LLM serving from token‑aware to plan‑driven execution, opening the path for truly scalable long‑context generation where only relevant knowledge is physically touched.

## Related Concepts  
KSRC gap, Knowledge Access Planning (KAP), intermediate representation (IR), GraphSpec compiler‑executor, KV footprint reduction, phase‑boundary model, plan‑guided execution.
