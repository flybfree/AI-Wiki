---

title: "Summary: Relaxation-Informed Training of Neural Network Surrogate Models"
url: http://arxiv.org/abs/2604.22746v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-04-24_17-46-55Z_Relaxation_InformedTrainingofNeuralNetworkSurrogat.md
generated_at: "2026-06-11 10:27"
model: nvidia/nemotron-3-nano-4b

---


## Summary
This paper introduces training regularizers that directly target the tractability of mixed‑integer linear program (MILP) formulations derived from ReLU neural network surrogates. By penalizing large big‑M constants and unstable neurons, as well as the per‑sample LP relaxation gap, the authors achieve up to four orders of magnitude faster solves while preserving surrogate accuracy.

## Key Takeaways
- A bound‑based regularizer penalizes both the size of MILP big‑M constants and the count of unstable neurons in the network.  
- An LP relaxation gap regularizer explicitly minimizes the per‑sample gap using a gradient derived from LP dual variables without custom autodiff tools.  
- Combining these regularizers approximates the full total derivative of the LP gap with respect to network parameters, capturing both direct and indirect sensitivities.

## Context
Neural surrogate models are increasingly used for high‑dimensional optimization but often produce MILPs that are intractable due to poor structural properties. Aligning training objectives with downstream problem characteristics is a longstanding challenge; this work bridges that gap by designing regularizers that improve MILP solvability.

## Implications
Faster MILP solves enable real‑time or large‑scale applications of neural surrogates in industry and research, making complex combinatorial optimization more feasible. Practitioners can adopt these regularizers to balance model performance with computational efficiency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2604.22746v1)
