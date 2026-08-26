---
title: Robust Data-Collection Policy Learning for Low-Variance Online Policy Evaluation
published: 2026-08-25T07:10:06Z
authors: Claire Chen, Shuze Daniel Liu, Licheng Luo, Rohan Chandra, Nan Jiang, Shangtong Zhang
url: http://arxiv.org/abs/2608.24146v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Robust Data-Collection Policy Learning for Low-Variance Online Policy Evaluation

## Abstract
In reinforcement learning policy evaluation, classic on-policy methods often suffer from high variance when estimating policy performance. To mitigate this issue, behavior policy search has been proposed to learn data-collecting policies tailored to reduce online evaluation variance. However, these approaches do not account for uncertainties in the transition functions. In practice, simulator transitions often differ from the real world due to modeling errors or approximation limitations. As a result, behavior policies trained in simulation may still yield high variance when deployed in real environments, leading to costly reliance on real-world evaluation samples. In this work, we propose a double-loop gradient-based algorithm for learning behavior policies that are both efficient and robust to transition uncertainty. Theoretically, we derive novel transition-variance gradient expressions and establish global convergence guarantees for the algorithm. Numerically, we demonstrate that our method is less sensitive to transition perturbations than existing approaches, providing supportive evidence for its practical utility.

## Metadata
- **Published**: 2026-08-25T07:10:06Z
- **Authors**: Claire Chen, Shuze Daniel Liu, Licheng Luo, Rohan Chandra, Nan Jiang, Shangtong Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24146v1)