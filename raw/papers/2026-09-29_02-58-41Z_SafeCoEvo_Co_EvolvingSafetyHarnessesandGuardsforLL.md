---
title: SafeCoEvo: Co-Evolving Safety Harnesses and Guards for LLM Agents at Test-Time
published: 2026-09-29T02:58:41Z
authors: Yu Cheng, Yongkang Hu, Shuaijie Ma, Zhihang Lin, Weicheng Meng, Jingyang Qiao, Jiuan Zhou, Yushuo Zhang, Yihang Chen, Weilin Luo, Kun Shao, Dong Li, Zhizhong Zhang, Yuan Xie, Zhaoxia Yin
url: http://arxiv.org/abs/2609.36580v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SafeCoEvo: Co-Evolving Safety Harnesses and Guards for LLM Agents at Test-Time

## Abstract
LLM agents deployed in real-world environments continually encounter new tasks and safety risks, while execution feedback typically becomes available only after each task is completed. However, existing self-evolving approaches commonly rely on multiple rounds of optimization over fixed and repeatedly accessible task distributions, fundamentally differing from test-time adaptation in real-world deployment, where only experience accumulated from past tasks can be used to improve safety decisions on future unseen tasks. To address this limitation, we propose SafeCoEvo, a test-time Harness-Guard co-evolution framework for LLM agent safety that enables the external safety system to continually adapt from accumulated runtime experience. SafeCoEvo jointly improves two complementary safety capabilities at different timescales: S-Harness rapidly externalizes recent runtime experience into updatable explicit safety knowledge that can promptly influence subsequent tasks, while GuardVPO internalizes accumulated runtime safety experience over a longer timescale into parametric risk-judgment capabilities. By combining short-term rapid adaptation with long-term capability consolidation, SafeCoEvo continually improves the agent's safety capabilities, reducing the unsafe outcome rate by 10.05% while improving the task success rate by 12.15% over the strongest baseline, thereby achieving simultaneous gains in safety and task utility.

## Metadata
- **Published**: 2026-09-29T02:58:41Z
- **Authors**: Yu Cheng, Yongkang Hu, Shuaijie Ma, Zhihang Lin, Weicheng Meng, Jingyang Qiao, Jiuan Zhou, Yushuo Zhang, Yihang Chen, Weilin Luo, Kun Shao, Dong Li, Zhizhong Zhang, Yuan Xie, Zhaoxia Yin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.36580v1)