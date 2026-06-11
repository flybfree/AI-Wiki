---
title: When Are Two Networks the Same? Tensor Similarity for Mechanistic Interpretability
url: http://arxiv.org/abs/2605.15183v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-14_17-58-27Z_WhenAreTwoNetworkstheSame_TensorSimilarityforMecha.md
generated_at: 2026-06-11 10:41
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces tensor similarity, a weight‑based metric that determines whether two neural networks implement the same computation by comparing their tensor representations. This approach is invariant to out‑of‑distribution mechanisms and basis‑dependent parameters, allowing exact verification of functional equivalence without empirical approximation.

## Key Takeaways
- Tensor similarity provides an exact algebraic test for global functional equivalence between models, avoiding reliance on empirical behavior or weight‑space symmetries.
- The metric captures cross‑layer mechanisms such as grokking and backdoor insertion by recursively comparing tensor structures across layers.
- Because it is invariant to basis changes, tensor similarity yields a more reliable similarity measure than existing empirical or parameter‑based methods.

## Context
Current mechanistic interpretability relies on metrics that either approximate behavior empirically or are sensitive to weight representations, limiting their usefulness for rigorous verification. This work fills that gap by offering a principled, symmetry‑aware comparison for tensor‑based architectures.

## Implications
Practitioners can now programmatically confirm whether two network components perform identical functions, supporting safer model analysis and debugging. The method also enables automated detection of unintended mechanisms, improving trust in AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.15183v1)
