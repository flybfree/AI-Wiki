---
title: Agent-Centric Animal Pose Forecasting
published: 2026-07-21T19:48:21Z
authors: Eyrun Eyjolfsdottir, Kristin Branson
url: http://arxiv.org/abs/2607.19548v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agent-Centric Animal Pose Forecasting

## Abstract
Understanding animal behavior at an algorithmic level -- what animals attend to, how they form internal models and plans, and how this maps to action -- remains a central challenge in neuroscience and ethology. Data-driven generative models offer a path toward this understanding. We introduce a framework for training agent-centric autoregressive models of animal behavior from tracked pose, applicable to single animals and to groups in which each agent senses and responds to its conspecifics. Our models input egocentric sensory observations and output egocentric movements, mirroring the biological constraint that animals observe and act on the world from their own reference frame. Social behavior emerges from agents independently sensing and responding to one another. This agent-centric formulation requires managing many parallel representations of the same data, along with ML-specific transformations like discretization. We release a general-purpose library focused on the composable sequences of operations that translate between these representations. We show that trained models capture the distribution of social behavior in groups of courting Drosophila, and our library includes quantitative tools for measuring fit. We demonstrate how the library supports systematic comparison across input and output representations and that it adapts straightforwardly to a new domain.

## Metadata
- **Published**: 2026-07-21T19:48:21Z
- **Authors**: Eyrun Eyjolfsdottir, Kristin Branson
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19548v1)