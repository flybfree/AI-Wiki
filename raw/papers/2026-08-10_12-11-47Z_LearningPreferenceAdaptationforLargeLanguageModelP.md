---
title: Learning Preference Adaptation for Large Language Model Personalization via Verbal Reinforcement Learning
published: 2026-08-10T12:11:47Z
authors: Yuting Liu, Wei Wu, Jianzhe Zhao, Guibing Guo
url: http://arxiv.org/abs/2608.09507v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning Preference Adaptation for Large Language Model Personalization via Verbal Reinforcement Learning

## Abstract
Natural language user preferences provide an interpretable interface for LLM personalization. However, universal preference summaries often contain information irrelevant to a particular downstream task. Directly supplying the full preference summary therefore wastes context capacity and introduces cross-task distraction, while manually designing task-specific preference views is difficult to scale. In this work, we study \emph{task-specific preference adaptation}: given a universal user preference summary and a downstream task, derive a task-conditioned representation that preserves sufficient decision-relevant evidence while removing redundant context. To this end, we propose \textsc{AlignXada}, a training-free meta-learning framework that induces reusable textual refinement policies for adapting universal preference summaries to task-specific ones. The refinement policy is iteratively optimized by a meta learner through verbal reinforcement learning. Across 13 tasks and three downstream models (39 task--model cells), \textsc{AlignXada} achieves an average gain of 3.82 points, improving 33 cells while retaining only 22.8\% of the original profile tokens and outperforming RAG in 36 cells. An extended faithfulness analysis further shows that the refined profiles remain largely grounded in the source preferences while preserving task-relevant personalization signals, suggesting that profile-side adaptation serves as a practical complement to universal memory construction for lifelong personalized agents.

## Metadata
- **Published**: 2026-08-10T12:11:47Z
- **Authors**: Yuting Liu, Wei Wu, Jianzhe Zhao, Guibing Guo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09507v1)