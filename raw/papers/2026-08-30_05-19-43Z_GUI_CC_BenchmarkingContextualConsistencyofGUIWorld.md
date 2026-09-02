---
title: GUI-CC: Benchmarking Contextual Consistency of GUI World Models as Agent Environments
published: 2026-08-30T05:19:43Z
authors: Lin Fu, Zheyuan Yang, Tianhui Zhang, Jinbiao Wei, Guo Gan, Boxu Liu, Yilun Zhao, Yu Rong
url: http://arxiv.org/abs/2609.00048v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GUI-CC: Benchmarking Contextual Consistency of GUI World Models as Agent Environments

## Abstract
GUI world models are increasingly evaluated as one-step next-screen predictors, yet their intended use is often as multi-step environments for GUI agents. This mismatch leaves a key requirement under-tested: generated states must remain contextually consistent when they are repeatedly reused for future interaction. We introduce GUI-CC, a benchmark that evaluates contextual consistency of GUI world models as agent environments rather than isolated next-screen predictors. GUI-CC contains two complementary tracks: an offline reference-action track that rolls models along real mobile GUI trajectories, and an online agent-loop track that lets fixed probing agents interact with model-generated UIs. We construct 500 offline trajectory tasks from GUIOdyssey and 200 emulator-verified online tasks across 30 mobile apps. GUI-CC evaluates transition fidelity, transition plausibility, contextual consistency, and task progress. Experiments show that plausible single-step generation does not guarantee reliable environment simulation: current models often produce usable-looking screens while failing to preserve task-relevant context or support executable multi-step rollouts.

## Metadata
- **Published**: 2026-08-30T05:19:43Z
- **Authors**: Lin Fu, Zheyuan Yang, Tianhui Zhang, Jinbiao Wei, Guo Gan, Boxu Liu, Yilun Zhao, Yu Rong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00048v1)