---
title: Meta-Task: Turning Terminal Task Synthesis into a Terminal Task for Scalable Agent Training
published: 2026-07-30T09:41:08Z
authors: Zhihong Pan, Jiyuan He, Kai Zhang, Yupeng Han, Ze Liu, Yuze Zhao, Yongcong Ye, Zhaohua Yang
url: http://arxiv.org/abs/2607.27929v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Meta-Task: Turning Terminal Task Synthesis into a Terminal Task for Scalable Agent Training

## Abstract
Training terminal agents at scale requires diverse, verifiable terminal tasks and high-quality interaction trajectories, yet acquiring such data remains a significant challenge. Existing synthesis methods face two key limitations: (1) weak reliability caused by the disconnect between task generation and real execution, and (2) limited diversity and scalability due to dependence on existing repositories. We propose Meta-Task, a framework that redefines terminal task synthesis as a Terminal-Bench-format task itself: an agent operates within a real container environment to iteratively generate, execute, and verify tasks, so that synthesized components are checked for internal consistency and executability within the generation loop itself. Building upon this, we decouple the target task requirements along multiple dimensions, introduce a multi-phase mechanism that dynamically designs novel task specifications before producing the actual tasks, and incorporate optional external material support to enhance diversity and realism. We additionally apply LLM-as-Judge filtering to ensure the quality of the final training data. Experiments on Terminal-Bench 2.0 show that fine-tuning on only 3,221 Meta-Task synthesized trajectories achieves 22.5% and 31.8% Avg Pass@1 for Qwen3-14B and Qwen3-32B respectively, outperforming concurrent approaches with significantly less training data.

## Metadata
- **Published**: 2026-07-30T09:41:08Z
- **Authors**: Zhihong Pan, Jiyuan He, Kai Zhang, Yupeng Han, Ze Liu, Yuze Zhao, Yongcong Ye, Zhaohua Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27929v1)