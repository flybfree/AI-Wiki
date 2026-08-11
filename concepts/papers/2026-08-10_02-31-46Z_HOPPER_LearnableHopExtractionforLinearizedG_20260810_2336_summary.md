# Summary: 2026-08-10_02-31-46Z_HOPPER_LearnableHopExtractionforLinearizedGraphSeq.md
Saved: 2026-08-10 23:36
Source: 2026-08-10_02-31-46Z_HOPPER_LearnableHopExtractionforLinearizedGraphSeq.md
Model: None

---

## Summary  
Graph neural networks often suffer from the coupling between information depth and processing depth, leading to over‑smoothing or loss of long‑range signals. Linearized Graph Sequence Models (LGSMs) attempt to decouple these by treating node propagation states as a sequence, but they rely on fixed graph operators that cannot adapt to input features or downstream tasks. HOPPER addresses this limitation by introducing an end‑to‑end learnable hop extraction mechanism that precedes the state‑space processing of LGSMs. The framework learns how and when to extract hops based on node features, graph structure, and task objectives while preserving permutation equivariance.

## Key Contributions  
- [Finding 1] HOPPER introduces a learnable hop‑extraction module that can be conditioned on node features and the graph topology, enabling flexible propagation strategies beyond fixed adjacency or non‑backtracking operators.  
- [Finding 2] The extractor supports graph‑aware, structure‑aware, and hop‑adaptive mechanisms, allowing the model to dynamically decide which hops to retain or cancel based on local context and long‑range dependencies.  
- [Finding 3] Experiments demonstrate that HOPPER achieves state‑of‑the‑art performance on the ECHO‑Synth benchmark and that tuning the maximum neighborhood size (structural memory window) further improves accuracy on the LRIM physics‑based long‑range dependency task.

## Methodology  
The authors start from Linearized Graph Sequence Models, which linearize message passing into a sequence of states. Instead of using static graph operators, they embed an end‑to‑end extractor that outputs a variable‑length hop sequence before feeding it to a modern state‑space model. The extraction process is learned jointly with the downstream task, allowing the network to adaptively decide which hops to propagate and when to cancel them. By conditioning the extractor on node features and graph structure, HOPPER can generate feature‑conditioned sequences while maintaining permutation equivariance across permutations of input nodes.

## Results  
On the ECHO‑Synth benchmark, HOPPER consistently outperforms prior LGSM baselines, achieving a mean accuracy improvement of 3.2 % over the best fixed‑operator model. Moreover, systematic ablation shows that increasing the maximum neighborhood size from 2 to 5 hops raises performance by an additional 1.8 % on LRIM, confirming that a longer structural memory window can capture more long‑range dependencies when learned adaptively.

## Significance  
HOPPER provides a principled way to separate information depth from processing depth in graph neural networks, mitigating over‑smoothing and preserving long‑range signals. By learning the hop extraction process end‑to‑end, it offers a flexible architecture that can be applied across diverse tasks without sacrificing permutation equivariance.

## Related Concepts  
Linearized Graph Sequence Models (LGSM), hop extraction, message passing, state‑space models, permutation equivariance, graph neural networks, adjacency‑based sequences, non‑backtracking sequences.
