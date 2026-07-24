---
title: Gate-Zero Growth: A Geometric Framework for Function-Preserving Continual Learning
url: http://arxiv.org/abs/2607.14571v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-16_05-00-49Z_Gate_ZeroGrowth_AGeometricFrameworkforFunction_Pre.md
generated_at: 2026-07-23 23:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes gate‑zero growth, a function‑preserving operator that adds new residual blocks via a zero‑initialised gate to continual learning. Geometric analysis shows it yields rank separation and controlled forgetting compared with non‑FP methods.

## Key Takeaways
- Old directions remain unchanged, preserving old domain knowledge throughout the adaptation process.  
- New‑weight directions are flat at the growth point, making them a source of new functional variation without affecting existing functions.  
- Gate opening during learning causes function drift O(||α||^2) and Jacobian leakage O(||α||_∞), allowing safe capacity activation.

## Context
Continual learning struggles with domain shift and forgetting; traditional methods degrade performance. This work offers a geometric perspective on how to activate latent capacity safely, providing a common framework for various adapter techniques.

## Implications
For practitioners, gate‑zero growth provides a principled way to integrate new knowledge while minimizing degradation of existing models. The framework can be adapted to LoRA, ReZero, and adapter constructions, offering a baseline for safe continual learning in industry applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.14571v1)
