---
title: Learn How to Act from Your Own Interactions: On-Policy Self-Distillation for GUI Agents
published: 2026-09-23T03:38:11Z
authors: Yan Zhang, Daiqing Wu, Huawen Shen, Liang Li, Gang Cao, Zhi Gong, Wei Dai, Xiaode Zhang, Can Ma, Yu Zhou
url: http://arxiv.org/abs/2609.27307v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learn How to Act from Your Own Interactions: On-Policy Self-Distillation for GUI Agents

## Abstract
Graphical User Interface (GUI) agents enable the fulfillment of complex user instructions through multi-turn interactions with software environments, requiring step-wise reasoning and long-horizon memory to guide actions and retain task-relevant information, respectively. Recent on-policy self-distillation (OPSD) methods have achieved strong performance on GUI grounding, a foundational subtask for GUI agents, owing to dense token-level supervision from privilege-conditioned self-teachers. However, extending existing OPSD methods to multi-turn GUI agents is hindered by self-teachers' limited privilege-following ability and insufficient privileged guidance. In this paper, we introduce GUI-SD-v2, the next version of GUI-SD, which extends OPSD from GUI grounding to multi-turn GUI interaction and addresses key limitations through a two-stage training framework. Specifically, GUI-SD-v2 first strengthens privilege following by jointly optimizing rollouts with and without privileged guidance from the same GUI states. Furthermore, it selectively distills step-specific reasoning and memory guidance through a privilege-conditioned self-teacher, supporting action decisions and the retention of task-relevant information for subsequent interactions. Extensive experiments on two representative GUI agent benchmarks, AndroidWorld and MobileWorld, show that GUI-SD-v2 compares favorably with existing OPSD baselines while consistently outperforming the evaluated state-of-the-art methods in both Pass@1 and Pass@3 success rates. Code and training data will be publicly released.

## Metadata
- **Published**: 2026-09-23T03:38:11Z
- **Authors**: Yan Zhang, Daiqing Wu, Huawen Shen, Liang Li, Gang Cao, Zhi Gong, Wei Dai, Xiaode Zhang, Can Ma, Yu Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.27307v1)