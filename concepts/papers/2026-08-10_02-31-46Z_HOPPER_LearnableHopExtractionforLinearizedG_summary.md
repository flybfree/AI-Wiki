# Summary: 2026-08-10_02-31-46Z_HOPPER_LearnableHopExtractionforLinearizedGraphSeq.md
Saved: 2026-08-10 23:33
Source: 2026-08-10_02-31-46Z_HOPPER_LearnableHopExtractionforLinearizedGraphSeq.md
Model: None

---

## Summary  
The paper proposes HOPPER, a learnable extension of linearized graph sequence models (LGSMs) that extracts hop sequences adaptively before they are processed by a state‑space model. It seeks to resolve the depth‑coupling problem in graph neural networks, which can cause over‑smoothing or loss of long‑range information. By learning how to generate hops conditioned on node features, graph structure, and downstream tasks, HOPPER introduces flexible propagation mechanisms while preserving permutation equivariance. The framework therefore enables more expressive representation learning for complex graphs.

## Key Contributions  
- [Finding 1] Introduces HOPPER, an end‑to‑end learnable hop extraction mechanism for LGSMs.  
- [Finding 2] Demonstrates that standard adjacency‑based and non‑backtracking sequences are special cases of the extractor family.  
- [Finding 3] Shows that varying the maximum neighborhood size (structural memory window) can optimize accuracy on the LRIM physics‑based long‑range dependency benchmark.

## Methodology  
The authors model LGSMs as state‑space models where each node’s state evolves over time according to a sequence of hops. They propose a neural extractor that takes the current node features and graph context, outputs a variable‑length hop vector for each position in the sequence, and feeds this into the state machine. The extractor is trained jointly with the downstream task using permutation‑invariant loss functions, ensuring that the learned extraction respects graph symmetry.

## Results  
Experiments on the ECHO‑Synth benchmark show HOPPER achieving top performance among LGSM baselines, outperforming both fixed‑hop and deep GNN approaches. On the LRIM physics dataset, adjusting the maximum neighborhood size (the structural memory window) yields higher accuracy, confirming that a learnable extraction can adapt to longer dependencies. These results validate that learning hop sequences improves long‑range graph representation.

## Significance  
HOPPER decouples propagation depth from processing depth, allowing deep architectures without over‑smoothing or information loss. By making the hop extraction process learnable and conditionally adaptive, it offers a principled way to tailor message passing for diverse graphs, advancing both theory and practice in graph sequence modeling.

## Related Concepts  
- Linearized Graph Sequence Models (LGSM)  
- Message passing  
- State‑space models  
- Permutation equivariance  
- Hop sequences
