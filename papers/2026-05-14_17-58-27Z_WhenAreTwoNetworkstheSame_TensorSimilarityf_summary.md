---
title: "2026 05 14 17 58 27Z Whenaretwonetworksthesame Tensorsimilarityf Summary"
date: 2026-05-14
tags: ['paper', 'research', 'ai']
---
# Summary: 2026-05-14_17-58-27Z_WhenAreTwoNetworkstheSame_TensorSimilarityforMecha.md


**Source**: [Original Paper](https://example.com/placeholder)
Saved: 2026-05-15 00:02
Source: 2026-05-14_17-58-27Z_WhenAreTwoNetworkstheSame_TensorSimilarityforMecha.md
Model: None

---

## Summary
This paper addresses a fundamental challenge in mechanistic interpretability: determining when two neural network components implement the same underlying computation. The authors argue that existing similarity measures are flawed because they either rely on empirical behavior, which fails to capture out-of-distribution mechanisms, or on basis-dependent parameters, which ignore weight-space symmetries. To resolve this, the authors introduce "tensor similarity," a novel weight-based metric designed specifically for tensor-based models that is invariant to these symmetries. This metric provides a rigorous algebraic framework for verifying functional equivalence, offering a more robust alternative to empirical approximation methods.

## Key Contributions
- The introduction of tensor similarity, a new metric that is invariant to weight-space symmetries, allowing for the accurate comparison of network structures regardless of basis transformations.
- The development of an efficient recursive algorithm that captures global functional equivalence and accounts for complex cross-layer mechanisms within tensor-based models.
- Empirical validation demonstrating that tensor similarity tracks functional training dynamics, such as grokking and backdoor insertion, with significantly higher fidelity than existing similarity metrics.

## Methodology
The authors approach the problem by identifying the limitations of current metrics in mechanistic interpretability. They posit that verifying if two parts of a model implement the same computation is a prerequisite for interpretability, yet current methods are blind to out-of-distribution mechanisms or disregard weight-space symmetries. To address this, they formulate tensor similarity as a weight-based metric. This metric is designed to be invariant to the symmetries inherent in weight space, thereby capturing the true functional equivalence of the networks. The methodology involves deriving an efficient recursive algorithm that can compute this similarity across layers, effectively transforming the problem of measuring similarity from one of empirical approximation into a solved algebraic problem. This approach allows for a more precise verification of faithfulness in neural network components.

## Results
The primary result is the successful definition and implementation of tensor similarity for tensor-based models. The authors demonstrate that this metric effectively captures global functional equivalence. In empirical evaluations, tensor similarity was shown to track functional training dynamics with higher fidelity than existing metrics. Specifically, the metric accurately reflected changes during phenomena such as grokking and backdoor insertion. These results suggest that tensor similarity provides a more reliable indicator of mechanistic identity compared to previous methods that relied on empirical behavior or basis-dependent parameters.

## Significance
This work is significant because it provides a rigorous, algebraic solution to the problem of verifying mechanistic identity in neural networks. By reducing the measurement of similarity to a solved algebraic problem, it offers a more robust and theoretically sound method for mechanistic interpretability. This advancement allows researchers to verify faithfulness with greater confidence, facilitating a deeper understanding of how neural networks implement computations. It also opens new avenues for analyzing model behavior during critical training phases, such as grokking, where empirical metrics may fall short.

## Related Concepts
- Mechanistic Interpretability
- Tensor Similarity
- Weight-Space Symmetries
- Functional Equivalence
- Grokking
- Backdoor Insertion
- Basis-Dependent Parameters
- Recursive Algorithms

[[When Are Two Networks the Same? Tensor Similarity for Mechanistic Interpretability]]