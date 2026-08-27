---
title: Learning What to Share and What to Personalize: Hierarchical Strategy Co-Evolution for Agent Memory
published: 2026-08-26T03:24:52Z
authors: Yupeng Han, Shuochen Liu, Kai Zhang, Ze Liu, Zhihong Pan, Xianquan Wang
url: http://arxiv.org/abs/2608.25329v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning What to Share and What to Personalize: Hierarchical Strategy Co-Evolution for Agent Memory

## Abstract
Memory-augmented agents maintain compact user profiles throughout extended conversations, enabling personalized and consistent responses without the need to process the entire dialogue history. The quality of these user profiles relies on the underlying memory management strategy: at each step, the agent must determine what to retain, compress, or discard. However, existing methods typically employ a static, one-size-fits-all strategy established before training. In practice, the optimal memory decision is inherently user-specific and dynamically evolves alongside policy optimization. To address this, we propose \textbf{HiPS} (\textbf{Hi}erarchical \textbf{P}ersonalized \textbf{S}trategy), a framework that decouples memory management into a globally shared foundation and a user-specific adaptive tier. Specifically, HiPS employs \textbf{Universal Strategy} to extract shared principles from cross-persona trajectories, alongside \textbf{Persona Delta Distillation} to generate tailored rules for users whose behaviors diverge from general patterns. \textbf{Cross-Level Rule Flow} dynamically calibrates their boundary by promoting broadly validated personal rules and demoting contradicted global ones. The architecture establishes a co-evolution loop where a mechanism guarantees that all strategy refinements are anchored to task outcomes. Extensive experiments demonstrate consistent improvements over memory-augmented baselines.

## Metadata
- **Published**: 2026-08-26T03:24:52Z
- **Authors**: Yupeng Han, Shuochen Liu, Kai Zhang, Ze Liu, Zhihong Pan, Xianquan Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25329v1)