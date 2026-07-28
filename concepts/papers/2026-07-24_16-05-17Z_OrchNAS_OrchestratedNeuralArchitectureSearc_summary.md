# Summary: 2026-07-24_16-05-17Z_OrchNAS_OrchestratedNeuralArchitectureSearchServic.md
Saved: 2026-07-27 23:23
Source: 2026-07-24_16-05-17Z_OrchNAS_OrchestratedNeuralArchitectureSearchServic.md
Model: None

---

## Summary  
OrchNAS proposes an energy‑aware, personalized federated edge intelligence framework that leverages a neural architecture search service to automatically design service‑adaptive models for heterogeneous edge devices. It orchestrates a global NAS on a server while each edge service selects a subnet via a progressive, greedy pruning strategy that respects its local energy, computation, and memory constraints. The system updates service‑adaptive parameters with primal‑dual optimisation, preserving the compact global representation and enforcing strict energy budgets. Experiments show that OrchNAS delivers up to 23 % lower energy consumption while maintaining >95 % accuracy compared with static models.

## Key Contributions  
- Energy‑aware global architecture representation learned from heterogeneous services.  
- Progressive, greedy, energy‑aware subnet selection per service.  
- Primal‑dual optimisation for personalised model updates within strict energy budgets.  

## Methodology  
The authors approached the problem by first constructing a server‑side NAS that generates a compact global architecture representation capturing trade‑offs across devices; then they introduced an edge‑local pruning algorithm that iteratively removes layers while respecting local energy, compute and memory budgets; finally they employed primal‑dual optimisation to adjust service‑adaptive parameters ensuring the global representation remains feasible.  

## Results  
Experiments on both real‑world sensor data streams and standard benchmarks (e.g., CIFAR‑10, ImageNet) demonstrate up to 23 % reduction in energy consumption while maintaining >95 % accuracy compared with static models; latency improves by ~18 % due to lighter architectures; personalisation error between services is <5 %.  

## Significance  
This work bridges NAS and federated learning for edge devices, enabling scalable, privacy‑preserving intelligence without central data collection. It reduces energy waste in resource‑constrained environments and opens a path toward truly adaptive AI at the edge.  

## Related Concepts  
Federated Learning, Neural Architecture Search (NAS), Energy‑aware Optimization, Primal‑Dual Algorithms, Heterogeneous Edge Devices, Progressive Greedy Pruning.
