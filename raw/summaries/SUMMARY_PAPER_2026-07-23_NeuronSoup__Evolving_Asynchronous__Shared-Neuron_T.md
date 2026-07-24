---
title: NeuronSoup: Evolving Asynchronous, Shared-Neuron Temporal Graphs without Backpropagation
url: http://arxiv.org/abs/2607.15217v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-16_17-18-59Z_NeuronSoup_EvolvingAsynchronous_Shared_NeuronTempo.md
generated_at: 2026-07-23 23:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
NeuronSoup introduces an asynchronous neural architecture where continuous signals travel through shared hidden neurons with variable delays, enabling constructive or destructive interference without backpropagation. The system evolves a 204‑path network of 266 hidden neurons on MNIST using a genetic algorithm and reaches 85.9 % test accuracy while occupying only 115 KB.

## Key Takeaways
- The architecture replaces synchronous layer‑by‑layer processing with asynchronous, delay‑mediated signal propagation through a pool of shared neurons that accumulate state for later arrivals, creating emergent interference effects.
- Evolution occurs on a flat real‑valued genome of 14,602 genes via a genetic algorithm, producing a network of 204 active paths and 266 hidden neurons with 156 shared across multiple paths, achieving high classification accuracy without differentiable computation.
- The model’s compact size (115 KB) and ability to adapt computation depth per sample demonstrate that non‑differentiable, biologically inspired designs can outperform deep learning on fixed‑depth tasks.

## Context
Current deep learning relies on fully connected, differentiable graphs where each layer processes all inputs simultaneously, limiting flexibility and requiring explicit engineering of lateral interactions. NeuronSoup’s genetic evolution offers a paradigm shift toward self‑organizing computation that mirrors biological neural dynamics without gradient‑based optimization.

## Implications
This approach could enable ultra‑lightweight inference for edge devices by eliminating the need for large compute graphs. Practitioners may adopt similar co‑evolved topologies to solve domain‑specific problems where adaptive depth and lateral communication are advantageous over handcrafted architectures.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.15217v1)
