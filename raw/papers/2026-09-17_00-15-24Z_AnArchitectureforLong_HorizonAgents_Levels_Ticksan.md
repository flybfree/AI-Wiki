---
title: An Architecture for Long-Horizon Agents: Levels, Ticks and Cascaded Intelligence
published: 2026-09-17T00:15:24Z
authors: Erik Nijkamp, Anurag Koul, Egor Pakhomov, Bo Pang
url: http://arxiv.org/abs/2609.19519v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# An Architecture for Long-Horizon Agents: Levels, Ticks and Cascaded Intelligence

## Abstract
Language-model agents are increasingly asked to carry out work spanning days or weeks, such as an operations remediation or a research programme. Such a task outlives any context window, any process and any interval at which a person can attend. In this paper, we argue that a long-horizon agent must run continually without forgetting before it can learn continually. This ability lies in the harness around the model rather than in the model itself. We derive seven bottlenecks from the long-horizon setting and answer them with a hierarchical architecture of three parts: (i) levels indexed by time scale, each keeping a bounded file summarising the level below; (ii) a clocked tick as the unit of autonomous action; and (iii) cascaded intelligence, where work is escalated to a more capable model only after failing review. We report on a ten-day campaign in which an agent built on this architecture reproduced a published reinforcement-learning result with a human attending once a day, and show (1) the agent kept the thread across every context reset and session boundary of the campaign, (2) operating knowledge written early changed later behaviour with no change to model weights, and (3) where learned components would enter such a system. Overall, our experience suggests continual learning for these agents needs a substrate outliving every context and process, and the checks the harness already runs are where a learner belongs.

## Metadata
- **Published**: 2026-09-17T00:15:24Z
- **Authors**: Erik Nijkamp, Anurag Koul, Egor Pakhomov, Bo Pang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.19519v1)