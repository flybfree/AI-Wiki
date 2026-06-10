---
title: Multi-Faceted Interactivity Alignment in Full-Duplex Speech Models
published: 2026-06-09T17:46:55Z
authors: Atsumoto Ohashi, Neil Zeghidour, Alexandre Défossez, Eugene Kharitonov
url: http://arxiv.org/abs/2606.11167v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Multi-Faceted Interactivity Alignment in Full-Duplex Speech Models

## Abstract
Full-duplex spoken dialogue models can listen and speak simultaneously, making them a promising architecture for natural conversation. However, current models are trained solely with supervised learning through token-level likelihood maximization, which does not directly optimize interaction-level behaviors, causing interactivity issues such as excessive silence and ill-timed turn-taking. Recent work has applied reinforcement learning (RL) to improve interactivity, but existing methods address only a limited set of interactive behaviors in their rewards. In this work, we propose a post-training alignment method that comprehensively improves the interactivity of full-duplex spoken dialogue models through RL. We address the four canonical axes of interactivity: pause handling, turn-taking, backchanneling, and user interruption. For each axis, we extract short audio segments from human conversation corpora and optimize the model with axis-specific reward functions. An extra LLM-based reward for response quality prevents semantic degradation. We apply our method to two open-source models, Moshi and PersonaPlex, demonstrating consistent improvements in interactivity on both offline evaluation with pre-recorded audio and real-time multi-turn dialogue evaluation.

## Metadata
- **Published**: 2026-06-09T17:46:55Z
- **Authors**: Atsumoto Ohashi, Neil Zeghidour, Alexandre Défossez, Eugene Kharitonov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.11167v1)