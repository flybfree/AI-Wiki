---
title: Learning Where Outcomes Change:Credit-Addressable Reasoning for Multimodal Geometry
published: 2026-08-31T08:44:36Z
authors: Jiani Guo, Junjie Wang, Jie Wu, Pengxiang Zhao, Dongdong Zhang, Shaohan Huang, Yujiu Yang, Furu Wei
url: http://arxiv.org/abs/2608.30457v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning Where Outcomes Change:Credit-Addressable Reasoning for Multimodal Geometry

## Abstract
Multimodal geometry reasoning requires VLMs to extract precise visual relations and preserve them through multi-step deduction. Existing free-form traces obscure the decisions that determine the answer, and trajectory-level reinforcement learning distributes a single terminal signal across the entire response. We introduce credit-addressable reasoning, in which the semantic units exposed during inference also define where learning compares alternatives and assigns credit. We instantiate this principle with Code-CoT, which retains the diagram, represents visual relations as line-addressable executable code, and organizes reasoning into typed events, and CE-GRPO, which selects event boundaries using structural priors and type-normalized entropy, samples complete continuations from shared prefixes, and converts outcome differences into localized advantages. Across nine geometry benchmarks, CE-GRPO achieves an average accuracy of 76.04, outperforming Qwen3-VL-8B and trajectory-level GRPO by $8.09$ and 3.43 points, respectively. Its relative advantage increases with the number of intermediate events, demonstrating the value of representation--optimization co-design for long, dependency-heavy multimodal reasoning.

## Metadata
- **Published**: 2026-08-31T08:44:36Z
- **Authors**: Jiani Guo, Junjie Wang, Jie Wu, Pengxiang Zhao, Dongdong Zhang, Shaohan Huang, Yujiu Yang, Furu Wei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30457v1)