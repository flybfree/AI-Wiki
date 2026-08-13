---
title: Generative Learning for Quantum Measurement Design
published: 2026-08-11T20:02:41Z
authors: Jun Dai, Olivier Nahman-Lévesque, Guillaume Rabusseau, Hong-Ye Hu, Cunlu Zhou
url: http://arxiv.org/abs/2608.11396v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Generative Learning for Quantum Measurement Design

## Abstract
Extracting quantum information from a quantum state is a fundamental task of quantum computation, often requiring the estimation of many non-commuting observables under a finite measurement budget. For both near-term and early fault-tolerant settings, the measurement protocol must balance statistical efficiency against implementation resources such as circuit depth, connectivity, and entangling-gate count. Many existing strategies focus on two extremes: hardware-friendly product measurements with high sampling cost, and fully commuting measurements with deep circuits. Here we recast resource-constrained measurement design as a generative learning problem. We introduce FlowMeas, which uses a generative flow network to directly sample finite ensembles of shallow Clifford measurement circuits subject to a prescribed shot budget and hardware constraints. At zero entangling depth, FlowMeas learns qubit-wise commuting measurement schedules and already matches or improves leading product-measurement methods on nearly all molecular benchmarks. Allowing one or two entangling gate layers yields further reductions in energy estimation error of up to $27\%$ relative to the strongest state-independent product-measurement baseline. The learned policy can also be reused across related Hamiltonians, substantially accelerating retraining along a molecular potential-energy surface. We further obtain results for molecular Hamiltonians with up to 20 qubits and apply the framework to a compactly encoded 54-qubit interacting fermionic model, extending the demonstrated scale beyond prior molecular benchmarks. These results establish generative learning as a flexible and unified framework for quantum measurement design under practical resource constraints.

## Metadata
- **Published**: 2026-08-11T20:02:41Z
- **Authors**: Jun Dai, Olivier Nahman-Lévesque, Guillaume Rabusseau, Hong-Ye Hu, Cunlu Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11396v1)