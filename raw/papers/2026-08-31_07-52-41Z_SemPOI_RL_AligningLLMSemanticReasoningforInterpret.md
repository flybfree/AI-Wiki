---
title: SemPOI-RL: Aligning LLM Semantic Reasoning for Interpretable Out-of-Town POI Sequential Generation
published: 2026-08-31T07:52:41Z
authors: Yunqi Liu, Yang Zhang, Ruixing Zhang, Liangzhe Han, Yi Qiao, Tongyu Zhu, Leilei Sun
url: http://arxiv.org/abs/2608.30399v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SemPOI-RL: Aligning LLM Semantic Reasoning for Interpretable Out-of-Town POI Sequential Generation

## Abstract
Large language models (LLMs) exhibit strong semantic reasoning and open-ended generation abilities, but aligning these abilities with structured sequential generation remains challenging. This challenge is particularly evident in out-of-town (OOT) POI sequence generation, where a model must infer transferable travel intent from a user's hometown behaviors, adapt to cross-city interest drift, and generate a coherent destination trajectory under structural constraints. Existing approaches either rely on latent ID-based transfer with limited interpretability or directly use LLMs for sequence generation without explicitly grounding inferred semantics into position-aware predictions. To address this gap, we propose SemPOI-RL, a framework that aligns LLM semantic reasoning with structured sequence generation for interpretable OOT recommendation. Specifically, we first fine-tune an LLM to infer destination-oriented travel styles from users' hometown trajectories, using natural language as an interpretable semantic intermediate. We then introduce a Semantic POI Alignment Module (SPAM) to ground these inferred styles into a style-conditioned masked autoencoder for position-aware trajectory generation. Finally, we apply reinforcement learning with recommendation-oriented rewards to align LLM-generated styles with downstream sequence quality. Experiments on two real-world datasets show that SemPOI-RL consistently outperforms both traditional recommenders and direct LLM baselines, while providing interpretable style attribution across different phases of a trip. The code is available at https://github.com/Wind-Flipped/SemPOI-RL .

## Metadata
- **Published**: 2026-08-31T07:52:41Z
- **Authors**: Yunqi Liu, Yang Zhang, Ruixing Zhang, Liangzhe Han, Yi Qiao, Tongyu Zhu, Leilei Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30399v1)