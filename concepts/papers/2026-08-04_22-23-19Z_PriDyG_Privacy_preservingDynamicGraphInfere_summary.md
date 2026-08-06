# Summary: 2026-08-04_22-23-19Z_PriDyG_Privacy_preservingDynamicGraphInferencewith.md
Saved: 2026-08-05 20:27
Source: 2026-08-04_22-23-19Z_PriDyG_Privacy_preservingDynamicGraphInferencewith.md
Model: None

---

## Summary  
The paper tackles the privacy leakage that accumulates in dynamic graph inference, where repeated model updates can expose sensitive edge information. It introduces PriDyG, a framework that merges GNN‑based structural learning with LLM‑driven semantic reasoning to achieve edge‑level differential privacy. By buffering newly arrived edges and processing each edge exactly once through incremental private multi‑hop aggregation, the total privacy cost remains constant regardless of update frequency. The approach also leverages node text for LLM predictions without incurring any additional edge‑level privacy cost.

## Key Contributions  
- [Finding 1] Introduces Edge-level Differentially Private Dynamic Graph Inference (EDG) as a formal problem statement.  
- [Finding 2] Designs an incremental private multi‑hop aggregation that buffers edges and processes each exactly once, yielding a constant total privacy cost independent of the number or schedule of updates.  
- [Finding 3] Combines GNN outputs with LLM predictions derived solely from node text, incurring no extra edge‑level privacy overhead.

## Methodology  
The authors formulate dynamic inference as a sequence of edge releases over time and develop a buffering mechanism that stores new edges until they are aggregated in private batches. Each batch is processed by a graph neural network to extract one‑hop signals; two‑hop transfers are approximated with at least half accuracy. The LLM component reads node text independently, generating semantic predictions without touching edge data, thus preserving privacy.

## Results  
Experiments on four benchmarks—node classification and link prediction—demonstrate that PriDyG outperforms geometrically decaying baselines under identical privacy budgets while matching the utility of naive per‑update retraining. The framework reduces cumulative privacy cost by up to three orders of magnitude, maintains exact one‑hop signals, and preserves at least half of two‑hop information.

## Significance  
This work provides a scalable solution for privacy‑preserving dynamic graph inference in real‑time applications such as social networks and IoT systems. By decoupling structural learning from semantic reasoning, PriDyG enables high utility while keeping the privacy overhead minimal, addressing a critical challenge as relational data evolves continuously.

## Related Concepts  
- Differential Privacy  
- Graph Neural Network (GNN)  
- Large Language Model (LLM)  
- Multi‑hop Aggregation  
- Edge‑level Privacy  
- Dynamic Graph Inference  
- Buffering Mechanism  
- Parallel Composition of Privacy Costs
