---
title: Learning to Reason and Use Tools through Unsupervised Fine-Tuning in Task-Oriented Dialog Systems
published: 2026-08-31T08:22:26Z
authors: Markel Ferro, Oier Lopez de Lacalle
url: http://arxiv.org/abs/2608.30426v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning to Reason and Use Tools through Unsupervised Fine-Tuning in Task-Oriented Dialog Systems

## Abstract
Current dialogue systems struggle with dynamic information retrieval, often leading to hallucinations and lower response accuracy. We address this by adapting the ReAct framework for Task-Oriented Dialogue, enabling Large Language Models (LLMs) to access external knowledge and produce factual responses. Mainly, we propose an unsupervised fine-tuning pipeline that harvests reasoning trajectories via in-context learning inference. High-quality samples are filtered using an LLM-based judge to construct a robust training set. This is enhanced by a unsupervised self-improvement loop, where improved checkpoints generate increasingly better trajectories for subsequent fine-tuning iterations. Experiments on the SIMMC dataset demonstrate that ReAct-based systems outperform baselines due to superior reasoning and tool use. Notably, our fine-tuned 8B model surpasses a 70B in-context system. Finally, we present an error analysis, impact of scene complexity, and cross-domain generalization.

## Metadata
- **Published**: 2026-08-31T08:22:26Z
- **Authors**: Markel Ferro, Oier Lopez de Lacalle
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30426v1)