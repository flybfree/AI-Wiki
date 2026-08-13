---
title: Hamilton-Zero: A Neural Tensor-Network Foundation Model for Ground States of Arbitrary Quadratic Qubit Hamiltonians
url: http://arxiv.org/abs/2608.11911v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_10-42-38Z_Hamilton_Zero_ANeuralTensor_NetworkFoundationModel.md
generated_at: 2026-08-12 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Hamilton-Zero, a neural tensor-network foundation model that learns ground states of arbitrary qubit Hamiltonian systems with about half a billion parameters. It achieves this by representing the state as manifold functions on SU(2)^N and using Lie derivatives for Hamiltonian evaluation. The model is trained up to 8100 qubits on a held-out dataset, showing scalability beyond classical simulation limits.

## Key Takeaways
- The model uses manifold variational optimisation over centrally odd scalar functions on SU(2)^N instead of explicit amplitudes, enabling universal quantum ground-state learning.
- Training leverages a replica-exchange Langevin sampler and sharded natural-gradient KFAC optimiser to handle up to 1024 qubits during fine‑tuning while pre‑training on hundreds of thousands of Hamiltonians.
- The approach preserves the spin‑½ sector’s ground‑state upper bound via the Peter–Weyl theorem, allowing reliable predictions for systems up to 8100 qubits.

## Context
This work bridges deep learning and quantum many‑body physics by treating Hamiltonian ground states as optimisation problems on a Lie group manifold. It extends large language model training techniques to quantum information, offering a new paradigm for scalable quantum advantage.

## Implications
Hamilton-Zero could accelerate the development of fault‑tolerant quantum computers by providing pre‑computed ground‑state resources. Practitioners may integrate these models into hybrid classical‑quantum workflows to reduce simulation bottlenecks and enable faster algorithmic design.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11911v1)
