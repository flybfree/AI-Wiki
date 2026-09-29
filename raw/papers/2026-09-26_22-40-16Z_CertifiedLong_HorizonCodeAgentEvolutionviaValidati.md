---
title: Certified Long-Horizon Code Agent Evolution via Validation-Gated Skill Optimization
published: 2026-09-26T22:40:16Z
authors: Yifan Wang, Hao Cheng, Xiaomin Li, Yuexing Hao, Hemanth Neelgund Ramesh, Dongwon Jung, Hao Tang, Keru Wang, Chenliang Zhou, Qianhui Wu, Wenlin Yao, Ananth Grama, Andrzej Banburski-Fahey, Baolin Peng, Jaron Lanier, Jianfeng Gao
url: http://arxiv.org/abs/2609.32990v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Certified Long-Horizon Code Agent Evolution via Validation-Gated Skill Optimization

## Abstract
Long horizon agent self-evolution without model weight updates is essential for enabling deployed agents to accumulate reusable skills and improve over time. Prior self-evolution work has focused primarily on short-horizon tasks, while repository-level software engineering remains unexplored despite being an ideal testbed for long-horizon adaptation. In this setting, agents are required to solve streams of sequential tasks, navigate complex dependencies with evolving repositories and persistently store and reuse experience. Text-based skill optimization offers an efficient, non-parametric approach for such adaptation. However, existing methods often suffer from unstable updates, performance drawdown, and agent collapse over extended deployments. In this paper, we formalize the concept of in-context self-evolution and introduce VALVE, a validated-gated framework for long-horizon skill optimization. We establish finite convergence, provide theoretical guarantees for future-task gain and drawdown, and derive the validation and evaluation holdout sizes required for a prescribed tolerance, with leading-order scaling   Empirically, our pipeline, VALVE achieves stable self-improvement over evolution horizon spanning more than 1,000 SWE tasks, with average final and peak gains of $14.9$ and $16.5$ points across three frontier models (GPT-5.5, Claude-4.6 and MiniMax-M2.7). The validation gate reduces average drawdown by 75% and produces an 11x more compact skill bank than ungated evolution. We further present extensive ablations identifying the design choices most critical to long-horizon skill evolution.

## Metadata
- **Published**: 2026-09-26T22:40:16Z
- **Authors**: Yifan Wang, Hao Cheng, Xiaomin Li, Yuexing Hao, Hemanth Neelgund Ramesh, Dongwon Jung, Hao Tang, Keru Wang, Chenliang Zhou, Qianhui Wu, Wenlin Yao, Ananth Grama, Andrzej Banburski-Fahey, Baolin Peng, Jaron Lanier, Jianfeng Gao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32990v1)