# Summary: 2026-08-03_17-43-36Z_StructuredMemoryforEdgeLanguageModels_PersistentCo.md
Saved: 2026-08-04 00:09
Source: 2026-08-03_17-43-36Z_StructuredMemoryforEdgeLanguageModels_PersistentCo.md
Model: None

---

## Summary  
The paper proposes a method to eliminate the prefill cost of retrieval‑augmented generation for edge language models by leveraging state‑space models’ fixed hidden states. It introduces PRECOG, which injects pre‑computed SSM hidden states at query time, making context retrieval O(1). Additionally, it adds SMC, a hierarchical persistent memory that consolidates short‑term episodic states into long‑term semantic memory. Together these mechanisms enable interactive RAG on resource‑constrained devices.

## Key Contributions  
- [Finding 1] The fixed‑size recurrent hidden state of SSMs encodes the entire document, allowing O(1) prefill retrieval.  
- [Finding 2] PRECOG injects the best‑matching pre‑computed SSM state at query time, bypassing in‑context re‑ingestion and reducing latency to <6 ms on a 1.2B‑parameter gated‑SSM.  
- [Finding 3] SMC provides O(1) session initialization and hierarchical consolidation of episodic states into long‑term memory with adjustable fidelity.

## Methodology  
The authors address the two cost components of RAG: prefill proportional to context length and KV‑cache growth. By exploiting SSMs’ position‑agnostic hidden state, they design PRECOG that stores document corpora as static SSM vectors offline. At inference, the system selects the nearest vector via a lightweight similarity metric and injects it directly into the model’s recurrent state, eliminating per‑token KV‑cache updates. SMC is built on top of this injection mechanism: short‑term episodic states are clustered hierarchically, stored with a fidelity‑vs‑storage trade‑off, and merged at query time to enrich the retrieved context.

## Results  
Experimental evaluation on TENNs‑LLM shows that PRECOG matches in‑context RAG answer quality while reducing prefill latency from ~27 seconds to under 6 ms—a >4500× speedup. SMC enables O(1) session startup and maintains coherence across sessions, preserving recall of prior interactions without recomputing embeddings.

## Significance  
This work bridges the gap between transformer‑based KV caches and edge deployment, making RAG feasible on devices with limited memory and compute. By achieving interactive latency under a minute, it crosses the usability threshold for real‑time applications such as voice assistants or offline tutoring tools.

## Related Concepts  
SSM (State‑Space Model), KV‑cache, Retrieval‑Augmented Generation (RAG), PRECOG (Pre‑Computed Context Injection), SMC (Structured Memory Consolidation), gated SSMs, O(1) latency, hierarchical memory consolidation.
