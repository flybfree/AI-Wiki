# Summary: 2026-07-23_14-39-46Z_PersistentComputationalState_ASession_CentricRunti.md
Saved: 2026-07-27 00:03
Source: 2026-07-23_14-39-46Z_PersistentComputationalState_ASession_CentricRunti.md
Model: None

---

## Summary  
The paper challenges the assumption that generative world models can be treated like language‑model servers, where every request recomputes its state from scratch. It argues that a small amount of non‑recomputable information — called Persistent Computational State (PCS) — must survive across requests to reproduce continuations identically. By defining PCS and building a session‑centric runtime around it, the authors demonstrate that checkpointing and restoring this state incurs negligible cost while preserving exact byte‑level continuity. The work thus provides a principled view of what truly persists in world‑model simulations and how to serve them efficiently.

## Semantic links
- [[concepts/papers/2026-07-23_21-59-56Z_QwenAgentWorld_LanguageWorldModelsforGeneralAgents_summary.md|Summary: Qwen-AgentWorld: Language World Models for General Agents]] — 4 title terms overlap; 29 backlinks; 10 summary/topic terms overlap
- [[concepts/2026-07-27_FoundationModelsStateOfTheArt.md|Foundation Models State of the Art — 2026-07-27]] — 4 title terms overlap; 13 backlinks; 4 summary/topic terms overlap
- [[concepts/llm-models/OpenSourceModelsStateOfTheArt.md|Open-Source Models State of the Art — 2026-07-10]] — 4 title terms overlap; 12 backlinks; 4 summary/topic terms overlap

## Key Contributions  
- [Finding 1] The attribution of video‑world‑model failures to model architecture is incomplete; for many architectures the failure stems from missing persistent state rather than architectural flaws.  
- [Finding 2] Persistent Computational State exists as a minimal non‑recomputable kernel that includes observation, random‑number generator (RNG) state, and either a memory bank or windowed KV context, which must be restored after each excursion to reproduce the continuation byte‑identically.  
- [Finding 3] A session‑centric runtime can be constructed around PCS with zero‑cost checkpoint/restore operations, yielding host‑bound sessions that are far larger than device‑bound ones.

## Methodology  
The authors measured the runtime state of three popular video world models by comparing outputs after genuine excursions and after restoring only the RNG. They observed that restoring observation plus RNG reproduced continuations perfectly while any alteration to RNG corrupted them, indicating a non‑recomputable kernel. By instrumenting these models with lightweight checkpoint/restore hooks, they built a session‑centric runtime that stores PCS between requests and evicts world memory based on relevance rather than recency.

## Results  
Checkpoint/restore operations cost 0.012 ms against the 1.85 s generation step, representing negligible overhead. Resident sessions can grow to 1,024 instances, bounded by host resources instead of GPU memory. World‑memory eviction follows relevance to the return point, reversing the typical LLM recency policy.

## Significance  
This work clarifies a hidden bottleneck in generative world modeling and enables scalable, low‑latency serving that is not limited by device capacity. By treating PCS as a first‑class concern, future systems can maintain continuity without costly recomputation, improving realism and efficiency across simulations.

## Related Concepts  
Persistent computational state, session‑centric runtime, non‑recomputable kernel, checkpoint/restore, RNG persistence, LLM serving assumptions, relevance‑based memory eviction.
