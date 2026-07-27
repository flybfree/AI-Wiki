---
title: Dynamic Commonsense Coordination for Empathetic Response Generation
published: 2026-07-24T09:30:57Z
authors: Zhengyu Qi
url: http://arxiv.org/abs/2607.22136v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dynamic Commonsense Coordination for Empathetic Response Generation

## Abstract
Empathetic Response Generation (ERG) requires models to recognize users' emotions and generate empathetic responses. Commonsense knowledge has been shown to support such reasoning, yet existing approaches typically reuse fixed commonsense representations across understanding and generation, limiting their ability to coordinate such knowledge across different stages. We propose DCC, a Dynamic Commonsense Coordination Framework with three complementary modules: residual-based commonsense interaction (SCE-AttnRes) to integrate contextual and situational commonsense representations, Association-Guided Commonsense Filtering (AGCF) to down-weight low-relevance commonsense relations, and Iterative Commonsense-Aware Decoding (ICAD) to dynamically retrieve commonsense memories during generation. Experiments on the Empathetic-Dialogues benchmark show that DCC improves emotion classification accuracy and response diversity over the CEM baseline while maintaining comparable perplexity. An LLM-based blind evaluation further demonstrates that DCC generates responses with better relevance, coherence, and informativeness. The code and implementation details will be publicly available at https://github.com/Hanabi-Q/DCC-ERG.

## Metadata
- **Published**: 2026-07-24T09:30:57Z
- **Authors**: Zhengyu Qi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22136v1)