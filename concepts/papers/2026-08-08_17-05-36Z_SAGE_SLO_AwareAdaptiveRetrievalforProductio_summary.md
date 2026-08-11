# Summary: 2026-08-08_17-05-36Z_SAGE_SLO_AwareAdaptiveRetrievalforProductionRAGSys.md
Saved: 2026-08-10 23:04
Source: 2026-08-08_17-05-36Z_SAGE_SLO_AwareAdaptiveRetrievalforProductionRAGSys.md
Model: None

---

## Summary  
The paper tackles the problem of balancing answer quality with strict service‑level objectives (SLOs) in production Retrieval‑Augmented Generation (RAG) systems by introducing a learned, SLO‑aware adaptive retrieval policy called SAGE. Instead of using a fixed number of passages per query, SAGE dynamically selects *k* based on query difficulty and latency constraints to stay within the 5 seconds P95 SLO. The approach is trained offline via imitation learning from an oracle that approximates optimal latency‑quality trade‑offs, and it incurs no additional LLM calls at inference time. Experiments show that SAGE can meet the SLO while dramatically reducing retrieval cost and latency compared with static baselines.

## Key Contributions  
- [Dynamic retrieval budget selection based on SLO constraints]  
- [Offline imitation learning using an oracle that approximates optimal latency‑quality trade‑offs]  
- [Generalization of a single policy across multiple datasets and LLM families with minimal inference overhead]

## Methodology  
SAGE extracts lightweight features from the initial retrieval stage, such as score distributions, rank gaps, and lexical signals, to capture query difficulty. These features are fed into an imitation‑learning framework where an oracle—trained offline on a held‑out set of queries—provides the ideal *k* for each query that balances latency and answer quality. At inference, SAGE simply selects the passage count recommended by its learned policy; no additional LLM calls or heavy computation are required, keeping overhead minimal.

## Results  
On Natural Questions under a 5 seconds P95 SLO, SAGE achieves 95 % SLO compliance versus only 30 % for the best static baseline (k=20). It reduces P95 latency by 36 %, cuts retrieval cost by 51 %, and incurs just a 2‑point Exact Match loss. A single policy trained on Natural Questions generalizes to HotpotQA, UnSeenTimeQA, and four LLM families (Llama, Qwen, Mistral, Gemma), delivering +45–52 point SLO improvements without any degradation in quality.

## Significance  
By aligning retrieval budget decisions with real‑world SLOs, SAGE resolves a core trade‑off between answer relevance and operational constraints. The method enables cost‑effective scaling of RAG systems, lowers infrastructure spend, and improves user experience across heterogeneous datasets and language models without sacrificing performance.

## Related Concepts  
Retrieval‑Augmented Generation (RAG), Service Level Objectives (SLO), Adaptive Retrieval, Imitation Learning, Latency‑Quality Trade‑off, Exact Match (EM) metric, Offline Training, Lightweight Features.
