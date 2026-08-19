---
title: GUPO: Gradient Uncertainty-aware Policy Optimization for Post-Training Large Language Models
published: 2026-08-18T06:22:55Z
authors: Peizheng Guo, Jianqi Zhang, Xingyu Zhang, Yun Fan, Jiahuan Zhou, Changwen Zheng, Wenwen Qiang
url: http://arxiv.org/abs/2608.17411v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GUPO: Gradient Uncertainty-aware Policy Optimization for Post-Training Large Language Models

## Abstract
Group Relative Policy Optimization (GRPO) has become a widely used approach for post-training Large Language Models (LLMs) for reasoning. In GRPO, the group gradients induced by different queries within the same mini-batch are directly averaged to form the policy update. However, these group gradients can point in conflicting directions. Our empirical analysis suggests that group-gradient conflicts tend to be associated with less effective policy updates, motivating the need for a reliable aggregated update direction under such conflicts. Standard GRPO aggregation treats the realized group gradients as deterministic contributions and does not account for differences in their reliability during aggregation. To address this issue, we propose Gradient Uncertainty-Aware Policy Optimization (GUPO), which models each group gradient as a random variable under a Bayesian formulation and estimates its probability distribution. GUPO then derives gradient uncertainty using a Dirichlet-based formulation and uses it to calibrate the contribution of each group gradient during aggregation. Extensive experiments on multiple benchmarks demonstrate the effectiveness of GUPO.

## Metadata
- **Published**: 2026-08-18T06:22:55Z
- **Authors**: Peizheng Guo, Jianqi Zhang, Xingyu Zhang, Yun Fan, Jiahuan Zhou, Changwen Zheng, Wenwen Qiang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17411v1)