---
title: DualSQL: Text-to-SQL with Multi-Agent Reinforcement Learning
published: 2026-09-16T05:16:37Z
authors: Shijie Chen, Yu Gan, Yeounoh Chung, Jiani Zhang, Quannan Li, Sravan Babu Bodapati, Cody J. Greer, Yu Su, Fatma Ozcan
url: http://arxiv.org/abs/2609.18135v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DualSQL: Text-to-SQL with Multi-Agent Reinforcement Learning

## Abstract
State-of-the-art Text-to-SQL systems are typically multi-agent pipelines centered around two fundamental tasks: schema linking and SQL generation. However, existing work trains separate models for each task, failing to leverage the synergy between these interrelated tasks. In this work, we propose DualSQL, a new Text-to-SQL system consisting of two agents powered by a single model backbone. The agents share the same model weights and agentic scaffold, enabling joint optimization through a robust multi-agent reinforcement learning (RL) framework. We design three database access tools to facilitate effective multi-step reasoning grounded to interactions with the databases. To improve training and avoid model collapse, we introduce a set of rollout guardrail mechanisms that stabilizes multi-agent RL training, supporting DualSQL to keep improving during training. We also introduce a new SQL correctness metric, robust execution match (REX), to more accurately judge SQL correctness and assign reward signals. Being trained on only 3755 examples, DualSQL-4B achieves an impressive 68.0% execution accuracy on the BIRD development set, matching previous 7B models. DualSQL-8B further improves to 71.1%, outperforming previous state-of-the-art single-model solutions with 32B parameters. These results demonstrate the strength of joint multi-agent reinforcement learning for building high performance Text-to-SQL pipelines.

## Metadata
- **Published**: 2026-09-16T05:16:37Z
- **Authors**: Shijie Chen, Yu Gan, Yeounoh Chung, Jiani Zhang, Quannan Li, Sravan Babu Bodapati, Cody J. Greer, Yu Su, Fatma Ozcan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.18135v1)