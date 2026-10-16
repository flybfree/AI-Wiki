---
title: All-in-One Memory: Process-Rewarded Reinforcement Learning for Memory Agents
published: 2026-10-15T03:02:24Z
authors: Bingbing Wang, Jingjie Lin, Weiming Qiao, Jing Li, Ruifeng Xu
url: http://arxiv.org/abs/2610.21147v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# All-in-One Memory: Process-Rewarded Reinforcement Learning for Memory Agents

## Abstract
Large language models increasingly rely on external memory to answer queries grounded in long-horizon histories such as multi-session dialogues and lengthy documents. However, existing memory methods often optimize retrieval and memory construction separately, without a shared reward space for evaluating search, writing, and stopping decisions. To address this, we propose All-in-One Memory (AiO-Mem), which organizes these operations as transitions over a shared evidence state and directly evaluates the semantic quality of each action in a unified reward space. AiO-Mem compiles heterogeneous histories into source-traceable multi-view events, providing a shared substrate for retrieval and memory writing. A unified memory policy actor then rolls out complete interaction trajectories over this shared evidence state. A separate trajectory-conditioned process reward model is trained through evidence-grounded supervised fine-tuning and trajectory-level DPO to assign process scores to the collected trajectories. These scores are aggregated into an action-balanced trajectory reward and used by Process-Aligned DAPO (PA-DAPO) to optimize the memory policy. Across long-context memory benchmarks, AiO-Mem consistently improves answer accuracy over both static memory systems and RL-trained memory agents.

## Metadata
- **Published**: 2026-10-15T03:02:24Z
- **Authors**: Bingbing Wang, Jingjie Lin, Weiming Qiao, Jing Li, Ruifeng Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.21147v1)