---
title: RSIAgent: Autonomous Exploration for Recursive Self-improvement in New Environments
published: 2026-09-14T10:46:40Z
authors: Sibo Zhu, Shicheng Fan, Xinyue Wang, Wenyi Wu, Kun Zhou, Biwei Huang
url: http://arxiv.org/abs/2609.15364v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RSIAgent: Autonomous Exploration for Recursive Self-improvement in New Environments

## Abstract
Digital agents must often adapt to new environments whose interfaces, tools, and failure modes are not fully captured by pretrained models. We introduce \textbf{RSIAgent}, a training-free multi-agent framework for recursive self-improvement through autonomous memory construction. RSIAgent coordinates curriculum, actor, and verifier agents to continually explore the environment, validate outcomes, and retain environment-specific knowledge, including reusable causal relationships between actions, conditions, and consequences. It further adopts a \textbf{broad-then-deep} exploration strategy, combining parallel broad recursive self-exploration for discovering diverse environment structures with focused deep self-exploration for uncovering hard cases, hidden constraints, boundary conditions, and previously unknown causal dependencies. The resulting memory is frozen and can be directly reused for downstream tasks without updating model parameters. Experiments on OSWorld-v2 and Agent's Last Exam show that RSIAgent substantially improves strong open-source models, enabling Kimi-K3 and GLM-5.3 to outperform frontier closed-source models including GPT-6.

## Metadata
- **Published**: 2026-09-14T10:46:40Z
- **Authors**: Sibo Zhu, Shicheng Fan, Xinyue Wang, Wenyi Wu, Kun Zhou, Biwei Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.15364v1)