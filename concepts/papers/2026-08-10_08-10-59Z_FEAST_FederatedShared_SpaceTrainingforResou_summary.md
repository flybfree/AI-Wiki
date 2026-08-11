# Summary: 2026-08-10_08-10-59Z_FEAST_FederatedShared_SpaceTrainingforResource_Het.md
Saved: 2026-08-10 23:41
Source: 2026-08-10_08-10-59Z_FEAST_FederatedShared_SpaceTrainingforResource_Het.md
Model: None

---

## Summary  
Federated learning (FL) must accommodate devices with varying computational capabilities; a fixed model cannot suit all clients while training separate models per deployment is costly. FEAST proposes a federated shared‑space training framework that jointly trains multiple subnetworks within each client’s inference budget, producing an elastic supernet that can be sliced for efficient deployment and balanced parameter access.

## Key Contributions  
- FEAST jointly trains multiple subnetworks within each client’s limited inference budget, yielding an elastic supernet suitable for slicing.  
- It introduces sparse aggregation and a γ‑allocation protocol to balance parameter reachability across heterogeneous clients.  
- The framework reduces aggregate model‑parameter traffic by 6.8× relative to full supernet transmission while achieving higher population‑averaged accuracy than existing weight‑sharing baselines.

## Methodology  
The authors address heterogeneity by constructing a supernet composed of several smaller subnetworks, each trained under the client’s inference budget constraint. Training proceeds via federated updates where only the relevant supernet slice is communicated to the server; the server aggregates these slices using sparse aggregation. A γ‑allocation protocol dynamically assigns training‑data volumes and inference budgets across subnetworks to prevent accuracy distortion and ensure fairness.

## Results  
In simulations with SuperFedNAS and DeepFedNAS, the supernets achieve only ~25% at 25 M parameters and ≤17.09% at 596 M inference MACs, whereas FEAST reaches 71.06% accuracy at the same budget, outperforming the strongest heterogeneous weight‑sharing baseline by 2.4 points. Across CIFAR‑100, CINIC‑10, and TinyImageNet‑200, FEAST yields the highest population‑averaged accuracy when each client receives its largest affordable subnetwork.

## Significance  
FEAST demonstrates that a single elastic model can adapt to diverse client capabilities without sacrificing performance or incurring prohibitive communication costs. By integrating budget‑aware training and sparse aggregation, it offers a practical solution for real‑world heterogeneous federated deployments where resources are limited and uneven.

## Related Concepts  
- Federated learning (FL)  
- Elastic models / supernets  
- Subnetwork routing  
- Sparse aggregation  
- γ‑allocation protocol
