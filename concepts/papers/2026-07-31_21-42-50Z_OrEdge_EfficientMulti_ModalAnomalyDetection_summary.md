# Summary: 2026-07-31_21-42-50Z_OrEdge_EfficientMulti_ModalAnomalyDetectioninDistr.md
Saved: 2026-08-03 23:49
Source: 2026-07-31_21-42-50Z_OrEdge_EfficientMulti_ModalAnomalyDetectioninDistr.md
Model: None

---

## Summary  
The paper proposes Orthogonal-Edge (OrEdge), a lightweight framework for real-time multi‑modal anomaly detection in distributed software systems, using orthogonal‑domain temporal representations to replace costly attention or graph models. It jointly processes logs, metrics, and traces to detect abnormal behavior while minimizing computational load and model size.

## Key Contributions  
- [Finding 1] OrEdge reduces the reconstruction model size to at most 9.6K parameters, compared with 20K–143K in existing methods.  
- [Finding 2] It achieves sub‑second inference on Raspberry Pi edge devices, reducing latency by over an order of magnitude.  
- [Finding 3] Orthogonal‑domain temporal modeling provides comparable detection performance to attention‑ and graph‑based approaches.

## Methodology  
The authors introduced OrEdgeCore, a lightweight orthogonal‑domain reconstruction module that learns recurring patterns across heterogeneous observability signals. By projecting each modality into orthogonal subspaces and reconstructing them with low‑rank matrices, the framework captures long‑term dependencies while suppressing transient noise, enabling efficient joint analysis without attention mechanisms or explicit graph construction.

## Results  
Evaluated on three real‑world microservice datasets (MSDS, SN, TT), OrEdge attains detection F1 scores within 5% of state‑of‑the‑art methods. Its model footprint is under 10K parameters and inference runs in <1 s on a Raspberry Pi 4, whereas comparable models exceed 20K parameters and take >5 s.

## Significance  
The work demonstrates that orthogonal‑domain learning offers an effective alternative for real‑time edge anomaly detection, balancing accuracy with computational efficiency—a crucial requirement for distributed software monitoring where resources are scarce.

## Related Concepts  
Orthogonal‑domain temporal representations; multi‑modal data fusion; lightweight reconstruction modules; edge inference; attention‑based models; graph neural networks; microservice observability; F1 score; sub‑second latency.
