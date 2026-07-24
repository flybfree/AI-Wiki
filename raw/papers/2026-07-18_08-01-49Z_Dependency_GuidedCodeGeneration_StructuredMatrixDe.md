---
title: Dependency-Guided Code Generation: Structured Matrix Decomposition and Consistency-Guided Refinement
published: 2026-07-18T08:01:49Z
authors: Mingqiao Mo, Yangchen Zeng, Zikai Xiao, Xin Xiao, Wenhua Nie, Zhaolu Kang, Guangyuan Dong, Kai Shu, Hao Zhang, Xiaodong Fan
url: http://arxiv.org/abs/2607.16692v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dependency-Guided Code Generation: Structured Matrix Decomposition and Consistency-Guided Refinement

## Abstract
The increasing complexity of modern software systems has made automated code generation a fundamental task in software engineering. However, existing approaches often fail to adequately capture the intricate, multi-level dependencies among code entities, leading to generated code that is logically incomplete or difficult to integrate into real-world systems. To address this limitation, we propose a dependency-aware code generation framework that explicitly models interactions among code entities through a graph-based representation. We decompose dependencies into two complementary components: a quantized matrix that captures strong, explicit relations, and a sparse low-rank factorization that models weaker, implicit interactions. The decomposition is efficiently learned via an alternating optimization procedure. During code generation, the learned dependency structure is incorporated as a constraint, ensuring both semantic coherence and structural consistency of the generated code. Furthermore, we introduce a sparse triplet representation for strong dependencies, significantly improving storage efficiency and computational scalability. Extensive experiments demonstrate that our approach consistently produces code with superior semantic alignment and structural fidelity compared to existing methods.

## Metadata
- **Published**: 2026-07-18T08:01:49Z
- **Authors**: Mingqiao Mo, Yangchen Zeng, Zikai Xiao, Xin Xiao, Wenhua Nie, Zhaolu Kang, Guangyuan Dong, Kai Shu, Hao Zhang, Xiaodong Fan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.16692v1)