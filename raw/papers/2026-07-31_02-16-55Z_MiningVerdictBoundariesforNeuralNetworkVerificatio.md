---
title: Mining Verdict Boundaries for Neural Network Verification
published: 2026-07-31T02:16:55Z
authors: Jiawei Ren, Guanqin Zhang, Zhenya Zhang, Yulei Sui
url: http://arxiv.org/abs/2607.28954v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Mining Verdict Boundaries for Neural Network Verification

## Abstract
Branch and Bound (BaB) aims to achieve complete verification of neural networks by adaptively partitioning the problem and applying off-the-shelf verifiers to subproblems. Its problem-splitting history can be represented as a tree, where each subproblem corresponds to a child node. A key problem of BaB lies in searching for the verdict boundaries across all the paths that divide the verified and unverified subproblems. We observe that the existing BaB approach tackles this problem by solving each expensive subproblem sequentially along the tree path as its depth increases, requiring costly bounds propagation at every visited BaB tree node (i.e., subproblem), which is inefficient. To address this issue, we propose effective search approaches that leverage the monotonicity of each path to efficiently and precisely locate the verdict boundary by simultaneously splitting multiple activation functions (e.g., ReLU), rather than processing them one at a time as in the classical approach. Our approach performs an effective exponential search along each path, allowing us to skip many boundary-unrelated subproblems when identifying the verdict boundary. The enhanced version further improves this process by estimating the boundary's position using quantitative information obtained from subproblem solving. We perform experimental evaluation on commonly-used benchmarks to assess our proposed techniques, and compare them with recent BaB-based approaches.

## Metadata
- **Published**: 2026-07-31T02:16:55Z
- **Authors**: Jiawei Ren, Guanqin Zhang, Zhenya Zhang, Yulei Sui
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28954v1)