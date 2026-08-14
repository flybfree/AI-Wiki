---
title: Branch and Bound for Relational Verification of Neural Networks
published: 2026-08-13T11:47:46Z
authors: Kota Fukuda, Zhenya Zhang, Guanqin Zhang, Jianjun Zhao
url: http://arxiv.org/abs/2608.13118v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Branch and Bound for Relational Verification of Neural Networks

## Abstract
Verification of neural networks against relational specifications, such as global robustness, is crucial for safety-critical applications of cyber-physical systems (CPS), given their increasing adoption of AI components. Compared to simple trace properties (e.g., local robustness), verifying relational specifications requires reasoning about the relationship between multiple network inferences, which brings significant technical challenges. Existing research has explored abstraction techniques based on sound and convex over-approximation of neural network outputs; however, since these approaches are inherently incomplete and may raise false alarms, they further underscore the need of effective abstraction refinement.   In this paper, we propose a branch-and-bound (BaB) framework to mitigate the issue, which iteratively splits the problem until all sub-problems are verified. Specifically, our BaB framework features splitting of relational neurons rather than individual neurons as prior works do, and as the core of our technique, we devise a relational neuron selection strategy based on the dual formulation of the verification problem, which allows us to efficiently select the (most likely) optimal relational neuron that maximizes the refinement brought by problem splitting. We evaluate SaBRe on 817 verification problems across ACAS Xu, MNIST-F, MNIST-C, CIFAR and GTSRB. The results show that SaBRe outperforms different baseline approaches, in terms of the number of solved instances and verification efficiency, which demonstrates the effectiveness of our proposed techniques.

## Metadata
- **Published**: 2026-08-13T11:47:46Z
- **Authors**: Kota Fukuda, Zhenya Zhang, Guanqin Zhang, Jianjun Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13118v1)