---
title: Code World Model: Coding Agent as World Brain
published: 2026-08-26T15:37:33Z
authors: Yiwen Chen, Guosheng Lin, Chi Zhang
url: http://arxiv.org/abs/2608.25927v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Code World Model: Coding Agent as World Brain

## Abstract
World models aim to simulate how complex environments evolve under actions and events, yet existing video-based world models primarily learn dynamics from visual observations, which reveal outcomes rather than the underlying knowledge, rules, and mechanisms governing world evolution. This makes it difficult to maintain persistent consequences and support coherent, open-ended evolution. We introduce Code World Model, a framework that separates world evolution from visual realization by combining the reasoning and coding capabilities of language models with the generative priors of video models. A coding agent serves as the world brain, reasoning about events and their consequences and generating executable code to maintain persistent world state and perform rule-consistent evolution. To connect executable state with visual generation, we introduce a proxy representation that encodes frame-wise spatiotemporal constraints and is compiled into a proxy video, which conditions a video model to render high-fidelity visual observations. We further develop data pipelines for constructing aligned proxy-observation pairs from gameplay and real-world videos. After fine-tuning on paired gameplay data, MiniMax-H3 follows proxy-based spatiotemporal specifications from simple interactive worlds built by the coding agent while preserving rich visual details and dynamics. These results demonstrate the potential of combining code for persistent world evolution with video models for flexible visual realization, providing a new path toward open-ended world models.

## Metadata
- **Published**: 2026-08-26T15:37:33Z
- **Authors**: Yiwen Chen, Guosheng Lin, Chi Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25927v1)