---
title: Aftab: A Comprehensive Benchmark of CNN Encoders and Advanced Value Functions in Parallelized Q-Networks
published: 2026-08-07T15:29:15Z
authors: Taha Shieenavaz, Shabnam Zareshahraki, Loris Nanni
url: http://arxiv.org/abs/2608.07335v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Aftab: A Comprehensive Benchmark of CNN Encoders and Advanced Value Functions in Parallelized Q-Networks

## Abstract
Recent advancements in deep reinforcement learning have increasingly favored simplified, highly parallelized paradigms. Notably, the Parallelized Q-Network (PQN) algorithm achieves stable off-policy learning without relying on computationally expensive replay buffers or target networks. However, the representational capacity and parameter efficiency of visual encoders operating in these buffer-free settings remain underexplored. In this work, we systematically investigate the architectural design space of Convolutional Neural Networks for PQN. We design and rigorously evaluate eight distinct CNN topologies, optimizing for sample efficiency under strict parameter constraints. Furthermore, we study the impact of representation and value estimation enhancements by integrating the Hadamax encoding paradigm and advanced Q-learning extensions, including distributional, ensemble, and dueling heads. Extensive experiments on the Atari-57 benchmark demonstrate that our proposed composite architecture, Aftab, achieves an Interquartile Mean (IQM) Human-Normalized Score of 6.479, establishing a 0.86 Probability of Improvement over the standard PQN baseline. Additionally, structural resilience evaluations on the highly non-stationary Procgen Hard benchmark confirm out-of-distribution generalization, with Aftab yielding an IQM Procgen Normalized Score of 0.418 compared to the baseline's 0.382. Ultimately, this work establishes an efficient, probabilistically superior structural reference for model-free reinforcement learning, all while preserving the simplicity and memory efficiency of unbuffered, parallelized optimization.   The complete Aftab framework, including all model definitions, training configurations, and raw experimental logs, is open-sourced and available on our GitHub repository: https://github.com/tahashieenavaz/aftab

## Metadata
- **Published**: 2026-08-07T15:29:15Z
- **Authors**: Taha Shieenavaz, Shabnam Zareshahraki, Loris Nanni
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07335v1)