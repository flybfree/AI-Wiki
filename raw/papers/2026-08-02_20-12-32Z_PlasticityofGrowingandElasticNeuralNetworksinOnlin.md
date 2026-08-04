---
title: Plasticity of Growing and Elastic Neural Networks in Online Continual Learning
published: 2026-08-02T20:12:32Z
authors: Jeong Min Kong, Richard S. Sutton
url: http://arxiv.org/abs/2608.01475v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Plasticity of Growing and Elastic Neural Networks in Online Continual Learning

## Abstract
Neural networks that can grow or both grow and shrink during learning, referred to as growing neural networks and elastic neural networks, respectively, have recently been explored in offline continual learning with a particular focus on catastrophic forgetting. Driven by the observations that 1) online continual learning closely resembles how animals learn; 2) loss of plasticity---the progressive decline in a learning network's ability to learn---is another crucial challenge facing continual learning; and 3) incremental introduction of randomly initialized hidden units was recently shown to help preserve plasticity, in this paper, we study the plasticity of several foundational growing and elastic networks in online continual learning. Our experiments in supervised learning settings show that adaptive growing networks, which incrementally incorporate new, randomly initialized units to the network while keeping all existing connections adaptive, can maintain high prediction accuracy without losing plasticity despite the continuous increase in the dead hidden unit proportion. Furthermore, we demonstrate that adaptive elastic networks, which in addition to progressively adding new hidden units also prune estimated dead hidden units at the beginning of each new task, can achieve excellent accuracy without loss of plasticity while simultaneously maintaining a near-constant, compact size. Our results suggest that growing and elastic networks, which exhibit the ability to adapt its structure to the relevant learning objectives, can be a promising class of algorithms also for preserving high plasticity in online continual learning.

## Metadata
- **Published**: 2026-08-02T20:12:32Z
- **Authors**: Jeong Min Kong, Richard S. Sutton
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01475v1)