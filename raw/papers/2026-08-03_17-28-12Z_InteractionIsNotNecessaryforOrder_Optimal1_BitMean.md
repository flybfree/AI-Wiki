---
title: Interaction Is Not Necessary for Order-Optimal 1-Bit Mean Estimation
published: 2026-08-03T17:28:12Z
authors: Jiachen Hu, Han Zhong
url: http://arxiv.org/abs/2608.02538v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Interaction Is Not Necessary for Order-Optimal 1-Bit Mean Estimation

## Abstract
This paper is concerned with one-bit mean estimation, where each independent sample is represented by a single binary message. We consider distributions on $\mathbb{R}$ with mean in $[-λ,λ]$ and absolute $k$-th central moment at most $σ^k$, where $k>1$ is fixed. For this class, previous work attained the optimal sample complexity for general queries using a two-stage protocol. The first stage localizes the mean. The second-stage queries are chosen after localization and refine the estimate around the decoded center. We show that this interaction can be avoided by constructing a randomized fully non-adaptive protocol that fixes all queries before observing the data and matches the optimal adaptive sample complexity. For target accuracy $ε$ and confidence $1-δ$, its sample complexity scales as \[ \log\fracλσ + \begin{cases} (σ/ε)^2\log(1/δ), & k>2,\\ (σ/ε)^2\log(σ/ε)\log(1/δ), & k=2,\\ (σ/ε)^{k/(k-1)}\log(1/δ), & 1<k<2, \end{cases} \] up to constants depending only on $k$. In the range covered by the known lower bound, this rate is minimax optimal even among fully adaptive protocols. This gives a negative answer to the COLT 2026 open problem asking whether interaction is necessary for order-optimal one-bit mean estimation with general queries \citep[Open Problem~1]{lau2026open}.

## Metadata
- **Published**: 2026-08-03T17:28:12Z
- **Authors**: Jiachen Hu, Han Zhong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02538v1)