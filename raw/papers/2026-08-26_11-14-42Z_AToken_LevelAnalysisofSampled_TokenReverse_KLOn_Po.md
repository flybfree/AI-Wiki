---
title: A Token-Level Analysis of Sampled-Token Reverse-KL On-Policy Distillation
published: 2026-08-26T11:14:42Z
authors: Bing Shao, Jiazheng Zhang, Long Ma, Yujiong Shen, Senjie Jin, Xin Guo, Yuming Yang, Mingxu Chai, Zhiheng Xi, Tao Gui, Qi Zhang, Xuanjing Huang
url: http://arxiv.org/abs/2608.25643v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Token-Level Analysis of Sampled-Token Reverse-KL On-Policy Distillation

## Abstract
On-policy distillation (OPD) supervises a student on its own trajectories with token-level signals from a frozen teacher, yet how a sampled loss allocates updates across tokens remains poorly understood. We analyze the gradient of the per-token K2 estimator of reverse KL with respect to the student logits. The $\ell_1$ norm of this gradient factorizes into the absolute teacher--student log-probability gap and a student-side softmax factor that grows as the sampled token becomes less likely under the student. In our math-distillation runs, these per-token norms are highly non-uniform: low-student-probability tokens account for a disproportionate share of their sum and are also enriched in large teacher--student gaps. As a lightweight intervention suggested by this analysis, we study Surprise-aware Reweighting (SuRe), a detached, bounded weighting rule that further amplifies this existing allocation. Across two Qwen3 student scales, SuRe improves several math metrics over vanilla OPD and shows no clear degradation on the selected out-of-domain benchmarks. Our primary contribution is therefore a gradient-level characterization of reverse-KL OPD trained with the K2 estimator, with SuRe as one empirical instantiation.

## Metadata
- **Published**: 2026-08-26T11:14:42Z
- **Authors**: Bing Shao, Jiazheng Zhang, Long Ma, Yujiong Shen, Senjie Jin, Xin Guo, Yuming Yang, Mingxu Chai, Zhiheng Xi, Tao Gui, Qi Zhang, Xuanjing Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25643v1)