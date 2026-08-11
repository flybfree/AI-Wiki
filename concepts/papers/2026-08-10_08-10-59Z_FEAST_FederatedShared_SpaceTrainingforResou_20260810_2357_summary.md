# Summary: 2026-08-10_08-10-59Z_FEAST_FederatedShared_SpaceTrainingforResource_Het.md
Saved: 2026-08-10 23:57
Source: 2026-08-10_08-10-59Z_FEAST_FederatedShared_SpaceTrainingforResource_Het.md
Model: None

---

## Summary  
Federated learning struggles to serve devices with varying computational capabilities, while training a separate model per client is cost‑prohibitive. FEAST proposes a federated shared‑space training framework that learns multiple subnetworks within each client’s inference budget. The framework balances model size and accuracy by routing only the relevant supernet portion and merging it sparsely across clients. It also introduces a γ‑allocation protocol to prevent budget‑induced accuracy distortion.

## Key Contributions  
- Jointly training several subnetworks inside each client’s limit mitigates imbalance caused by differing inference budgets.  
- Sparse aggregation and routing reduce aggregate model‑parameter traffic by ~6.8× relative to full supernet transmission.  
- A γ‑allocation protocol controls the coupling between training data volume, inference budget, and accuracy.

## Methodology  
The authors employ federated supernet training where each client jointly optimizes multiple subnetworks constrained by its compute budget. Only the supernet portion that fits within the client’s inference limit is transmitted; clients perform sparse aggregation of returned parameter slices. A γ‑allocation mechanism allocates training data and model parameters proportionally to ensure fair resource use.

## Results  
SuperFedNAS and DeepFedNAS achieve at most 17.09 % accuracy at 596 M inference MACs, whereas FEAST reaches 71.06 %, surpassing the strongest weight‑sharing baseline by 2.4 points. Across CIFAR‑100, CINIC‑10, and TinyImageNet‑200, FEAST yields the highest population‑averaged accuracy when each client uses its largest affordable subnetwork.

## Significance  
FEAST shows that a single elastic supernet can serve diverse devices without sacrificing performance, dramatically cutting communication overhead. The γ‑allocation protocol provides a principled way to align training effort with real‑world resource constraints, enabling scalable and fair federated learning across heterogeneous hardware.

## Related Concepts  
- Federated Learning (FL)  
- Supernet Training / Elastic Model  
- Subnetwork Routing  
- Sparse Aggregation  
- γ‑Allocation Protocol
