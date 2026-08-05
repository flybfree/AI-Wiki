---
title: OPTD: On-Policy Transition Distillation with Consistency-Guided Adaptive Compression for Few-Step Diffusion Language Models
published: 2026-08-03T23:09:43Z
authors: Xiaocheng Lu, Hualei Zhang, Shuhan Guo, Jie Zhang, Xiaoyi Pang, Jian Liu, Haoxi Li, Bohai Gu, Haoxuan Che, Jingcai Guo, Song Guo
url: http://arxiv.org/abs/2608.02942v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# OPTD: On-Policy Transition Distillation with Consistency-Guided Adaptive Compression for Few-Step Diffusion Language Models

## Abstract
Diffusion language models (dLLMs) can predict many tokens in parallel, but accurate generation still requires many iterative denoising steps. Few-step distillation accelerates decoding by compressing multiple teacher steps into a single student transition. However, existing methods construct supervision on off-policy trajectories. At inference, the student's early parallel commitments alter the context of later predictions, so the states it actually visits drift away from the supervised ones--precisely when step compression is most aggressive. On-policy distillation is a natural remedy for this mismatch, but it leaves open how far each transition should advance: matching only the teacher's next action limits compression, while indiscriminately merging future actions can violate intermediate dependencies. To address this limitation, we propose OPTD, On-Policy Transition Distillation with consistency-guided adaptive compression. It samples partial states from the few-step student's own trajectories, uses a frozen, question-only teacher to identify outcome-aligned future candidates, and orders them by current-state confidence. The method then selects the longest prefix whose joint commitment preserves the teacher's rollout outcome. A set-bottleneck objective promotes every verified future candidate to the decoder's release threshold, while a frozen-teacher KL anchor regularizes all other active positions. Neither target construction nor training uses a gold response. Across four mathematical reasoning and code-generation benchmarks, OPTD consistently improves the quality--efficiency trade-off and attains the strongest overall quality-constrained AUP among the evaluated few-step baselines.

## Metadata
- **Published**: 2026-08-03T23:09:43Z
- **Authors**: Xiaocheng Lu, Hualei Zhang, Shuhan Guo, Jie Zhang, Xiaoyi Pang, Jian Liu, Haoxi Li, Bohai Gu, Haoxuan Che, Jingcai Guo, Song Guo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02942v1)