---
title: ChainPrune: Evaluating and Reducing Redundancy in Long Chain-of-Thought Reasoning
published: 2026-08-22T09:09:05Z
authors: Weihang Pan, Zhengxu Yu, Yuxiang Zhang, Wenzhi Li, Zhongming Jin, Binbin Lin, Xiaofei He, Jieping Ye
url: http://arxiv.org/abs/2608.21860v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ChainPrune: Evaluating and Reducing Redundancy in Long Chain-of-Thought Reasoning

## Abstract
Chain-of-Thought (CoT) reasoning has significantly enhanced the multi-step problem-solving capabilities of large language models (LLMs) by introducing explicit intermediate reasoning. However, advanced Large Reasoning Models (LRMs) often exhibit overthinking behaviors, including excessively long reasoning steps, redundant steps, and high computational overhead. Existing token-length reward strategies aim to promote concise outputs, but often result in pseudo-conciseness, where token count is reduced, yet redundant reasoning persists, leading to longer and less structurally efficient chains. To address these limitations, we propose ChainPrune, a novel reasoning path semantic structural optimization method to efficiently and controllably synthesize self-generated high-quality training data. We initially consolidate self-generated reasoning paths into a tree-based structure, followed by a multi-criteria dominant path selection process for preference data construction that formulates shallow reasoning trajectories while preserving essential reasoning steps. To further enhance the quality of reasoning, we incorporate a DPO-based preference learning method combined with supervised loss, effectively mitigating false reward suppression. This innovative integration significantly enhances both the efficiency and effectiveness of our reasoning framework. Comprehensive experimental results demonstrate significant reductions in step length and computational overhead, while maintaining or even enhancing accuracy.

## Metadata
- **Published**: 2026-08-22T09:09:05Z
- **Authors**: Weihang Pan, Zhengxu Yu, Yuxiang Zhang, Wenzhi Li, Zhongming Jin, Binbin Lin, Xiaofei He, Jieping Ye
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21860v1)