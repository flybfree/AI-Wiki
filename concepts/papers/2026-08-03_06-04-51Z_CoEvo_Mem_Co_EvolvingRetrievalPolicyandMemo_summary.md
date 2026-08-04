# Summary: 2026-08-03_06-04-51Z_CoEvo_Mem_Co_EvolvingRetrievalPolicyandMemoryBankf.md
Saved: 2026-08-03 23:37
Source: 2026-08-03_06-04-51Z_CoEvo_Mem_Co_EvolvingRetrievalPolicyandMemoryBankf.md
Model: None

---

## Summary  
The paper proposes CoEvo‑Mem, a closed‑loop framework that jointly evolves the retrieval policy and memory bank of long‑term LLM agents. By coupling query rewrites with routing decisions and feeding task outcomes back to both components, it creates a feedback loop where memory updates reshape future retrieval. This co‑evolutional approach addresses the limitation of existing methods that treat retrieval or memory evolution in isolation.

## Key Contributions  
- [Finding 1] CoEvo‑Mem introduces a closed‑loop mechanism where the retrieval policy and memory bank are updated alternately, forming a feedback loop between them.  
- [Finding 2] The framework uses frozen LLM‑generated route‑specific query rewrites and routing priors corrected by a lightweight residual router to improve retrieval relevance.  
- [Finding 3] Alternating updates (router with fixed memory vs. memory with fixed policy) mitigate non‑stationarity induced by coupling.

## Methodology  
CoEvo‑Mem treats the agent’s memory bank as a graph of task trajectories and their outcomes, assigning credit to routing decisions. For each query, a frozen LLM produces rewrites and a routing prior; a residual router refines these online. The retrieved context is combined with task feedback that updates both memory values (e.g., relevance scores) and relational links between memories. Updates are applied in alternating phases: first the router is fine‑tuned while the memory bank remains static, then the memory bank is updated based on the fixed retrieval policy. This alternation stabilizes learning.

## Results  
Across seven benchmarks—including multi‑turn dialogue, knowledge‑graph QA, and chain‑of‑thought reasoning—the CoEvo‑Mem system outperforms prior state‑of‑the‑art methods by an average of 4.2 % F1 gain. Notably, it achieves the highest performance on tasks requiring long‑term memory consistency, where earlier findings often degrade due to stale retrieval.

## Significance  
By demonstrating that retrieval and memory evolution are interdependent, CoEvo‑Mem reshapes how we design agents for continual learning. The alternating update strategy offers a practical way to handle non‑stationarity in real‑world deployments, paving the way toward more robust and adaptive LLM systems.

## Related Concepts  
- Retrieval‑augmented generation (RAG)  
- Memory banks / external memory  
- Reinforcement learning for retrieval  
- Closed‑loop reinforcement learning  
- Non‑stationary optimization
