---
title: What Limits Recursive Reasoning Models: Optimization, Architecture and Test-Time Scaling
url: http://arxiv.org/abs/2609.39967v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_15-32-55Z_WhatLimitsRecursiveReasoningModels_Optimization_Ar.md
generated_at: 2026-09-30 22:09
model: qwen3.6-35b-a3b
---

## Summary
This study investigates the factors limiting recursive reasoning models, which use shared Transformer blocks to achieve large effective depth with few parameters for algorithmic tasks. By establishing a unified experimental pipeline across six domains, the authors identify that stable optimization relies on an intermediate gradient horizon, large physical batches, and controlled recurrent state updates rather than complex hierarchical architectures. The resulting 13.6M-parameter model sets new baselines, significantly improving out-of-distribution generalization and accuracy on tasks like Sudoku and ARC-AGI compared to existing approaches.

## Key Takeaways
- Stable recursive reasoning requires a specific optimization recipe rather than architectural complexity

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.39967v1)
