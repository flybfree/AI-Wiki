---
title: INTENT-AS-A-TOOL Makes it Easy to Track Agentic Misalignment
published: 2026-08-27T16:47:19Z
authors: Yutong Zhang, Jianshuo Dong, Peng Xu, Long Wang, Jie Zhang, Tianwei Zhang, Xiaoping Zhang, Han Qiu
url: http://arxiv.org/abs/2608.27348v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# INTENT-AS-A-TOOL Makes it Easy to Track Agentic Misalignment

## Abstract
As large language models (LLMs) are deployed as autonomous agents, safety failures increasingly involve consequential actions. We study agentic misalignment, where agents take harmful actions under goal conflicts and pressures. Using chain-of-thought (CoT) monitoring, we find that harmful execution is often preceded by intent signals in reasoning. However, post-hoc CoT labels are too coarse to show how intent changes during generation. We introduce INTENT-AS-A-TOOL, an approach that adds intent-targeted tools to give the model a dedicated channel for expressing commitment to a target behavior. The probability of calling an intent tool provides a judge-free, fine-grained signal of the model's tendency to pursue that behavior. Our results show that INTENT-AS-A-TOOL complements CoT monitoring, expands post-hoc CoT labels into dense trajectories, and identifies critical steps for online intervention. These findings suggest that action preferences are useful for tracking agentic misalignment during reasoning. Our code and data are accessible: https://github.com/RebeccaZhang22/intent-as-a-tool.

## Metadata
- **Published**: 2026-08-27T16:47:19Z
- **Authors**: Yutong Zhang, Jianshuo Dong, Peng Xu, Long Wang, Jie Zhang, Tianwei Zhang, Xiaoping Zhang, Han Qiu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27348v1)