---
title: When Successful Strategies Fail: Adaptation to Environmental Novelty in Terminal Agents
published: 2026-09-27T19:47:43Z
authors: Janvijay Singh, Vaishnavi Shrivastava, Dilek Hakkani-Tur, Ece Kamar, Asli Celikyilmaz
url: http://arxiv.org/abs/2609.33870v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Successful Strategies Fail: Adaptation to Environmental Novelty in Terminal Agents

## Abstract
LLM agents increasingly solve long-horizon tasks by autonomously interacting with their environment. In doing so, their strategies rely on assumptions about that environment: which resources and tools exist, where they are located, and how they behave. When these assumptions no longer hold, reliable agents must detect the change and adapt while pursuing the same goal. We study this adaptation capability through environmental novelty: a change that keeps the task objective fixed while invalidating an assumption underlying an otherwise successful trajectory. We introduce AGNI, an automated pipeline that extracts trajectory-relevant assumptions, injects targeted environmental changes, and validates that the resulting novel tasks remain solvable. Across three terminal benchmarks, AGNI produces diverse novelties spanning resources, interfaces, constraints, and execution semantics. Evaluating multiple LLM agents reveals a substantial adaptation gap between base and novel tasks. Trajectory analysis suggests that agents often encounter evidence of the change but fail to diagnose its cause and revise their strategy. Finally, post-training for environmental novelty improves adaptation to held-out novel tasks while also improving performance on base tasks. Our results highlight a gap between task competence and adaptive capability and motivate environmental variation as a core dimension of agent training and evaluation.

## Metadata
- **Published**: 2026-09-27T19:47:43Z
- **Authors**: Janvijay Singh, Vaishnavi Shrivastava, Dilek Hakkani-Tur, Ece Kamar, Asli Celikyilmaz
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33870v1)