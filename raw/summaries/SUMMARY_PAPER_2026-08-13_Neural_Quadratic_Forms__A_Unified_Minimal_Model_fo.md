---
title: Neural Quadratic Forms: A Unified Minimal Model for Sudden Learning and Scaling Laws
url: http://arxiv.org/abs/2608.13335v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_15-05-43Z_NeuralQuadraticForms_AUnifiedMinimalModelforSudden.md
generated_at: 2026-08-13 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a unified minimal model that explains both sudden learning plateaus and smooth power‑law loss reductions observed in neural training, regardless of microscopic architecture. By showing that symmetry forces a universal quadratic expansion about near‑zero weights, the authors demonstrate that all layer types reduce to a single structure matrix A(x) whose dynamics drive the training behavior.

## Key Takeaways
- The training dynamics are governed by the order parameter M = WWᵀ, which switches modes one after another when data matrices share an eigenbasis.  
- Small initial weights cause these switch‑on times to be far apart, producing plateaus that appear as a singular limit of a smooth flow.  
- When many modes are unresolved, the events merge into a power law whose exponent is predicted by the theory.

## Context
This work bridges disparate phenomena in deep learning—stepwise convergence and continuous scaling laws—by revealing a common underlying symmetry across architectures such as perceptrons, attention layers, mixtures of experts, and convolutions. It provides a theoretical bridge between low‑level weight dynamics and high‑level training behavior that has long been treated separately.

## Implications
For practitioners, the model offers a way to predict when plateaus will occur and how to accelerate convergence by controlling the structure matrix A(x). For researchers, it opens avenues for designing architectures whose symmetry can be tuned to achieve desired learning regimes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13335v1)
