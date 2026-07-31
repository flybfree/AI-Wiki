# Summary: 2026-07-30_17-01-20Z_SameGraphCross_TaskTransferinGNNs_ProtocolsandPred.md
Saved: 2026-07-30 23:15
Source: 2026-07-30_17-01-20Z_SameGraphCross_TaskTransferinGNNs_ProtocolsandPred.md
Model: None

---

## Summary  
The paper tackles the problem of transferring knowledge between node classification (NC) and link prediction (LP) on the same graph without introducing leakage, which is a common issue in cross‑task GNN research. It formalizes a leakage‑free protocol that shares a message‑passing graph while excluding evaluated edges and uses fixed negatives for LP, then evaluates its effectiveness across three backbones. The authors also introduce CoTask Score (CTS) to summarize the joint utility of a shared encoder when serving both tasks.  

## Key Contributions  
- Finding 1: Formalization of same‑graph NC–LP transfer with a leakage‑free protocol that uses a shared message‑passing graph excluding evaluated edges and fixed negatives.  
- Finding 2: Directional performance: NC→LP consistently improves homophilic graphs, while LP→NC often harms accuracy unless LP is easy and NC is unsaturated, indicating structural pretraining benefits.  
- Finding 3: CoTask Score (CTS) quantifies the combined NC+LP utility of a shared encoder and correlates with graph homophily.  

## Methodology  
The authors fix node and edge splits to avoid leakage, construct a shared graph that excludes edges already evaluated for either task, and employ fixed negative sampling for LP. They evaluate three GNN backbones (GCN, GraphSAGE, GPS) under both homophilic and heterogeneous regimes, computing CTS as the weighted sum of normalized NC and LP accuracies.  

## Results  
NC→LP transfer yields up to 4% absolute gain on homophilic graphs across all models. LP→NC shows negative or near‑zero gains except when LC is easy; CTS correlates strongly with homophily (r≈0.78). The leakage‑free protocol improves average NPV by roughly 2%.  

## Significance  
This work clarifies when cross‑task transfer helps, preventing overfitting and wasted computation. By providing a concrete protocol and a unified metric (CTS), it enables principled sharing of graph structure across tasks, improving both efficiency and predictive performance.  

## Related Concepts  
- Same‑graph cross‑task learning  
- Leakage‑free protocols  
- Homophilic graphs  
- Structural pretraining  
- CoTask Score
