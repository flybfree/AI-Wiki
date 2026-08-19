---
title: EvoTS-Agent: A Self-Evolving LLM Agent for Financial Time Series Change Point Detection
published: 2026-08-18T15:55:32Z
authors: Lei Jiang, Ye Wei, Xinyu Xi, Jordan Langham-Lopez, Yifan Bao, Raad Khraishi, Yihao Ang, Anthony K. H. Tung, Lukasz Szpruch, Hao Ni
url: http://arxiv.org/abs/2608.17933v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EvoTS-Agent: A Self-Evolving LLM Agent for Financial Time Series Change Point Detection

## Abstract
Financial time series exhibit non-stationary and heterogeneous statistical properties, making change-point detection challenging because no single unsupervised algorithm performs consistently across assets and market regimes. Conventional workflows consequently depend heavily on expert-driven model selection, feature design, and hyperparameter tuning, limiting their scalability and adaptability. We propose EvoTS-Agent, a validation-guided self-evolving LLM agent for autonomous financial time-series change-point detection. EvoTS-Agent first performs curated exploratory data analysis to characterize dataset properties and initialize candidate detection models. It then evolves executable experiment trajectories through three complementary operators: \textit{Revision} exploits the current best solution, \textit{Alternative Strategy} explores fundamentally different modeling directions when progress stagnates, and \textit{Recombination} synthesizes complementary evidence from high-performing trajectories. Validation feedback guides trajectory evolution throughout the search, enabling the agent to adapt its detection pipeline to the statistical characteristics of each dataset while preserving reliable optimization. Experiments across four benchmark datasets demonstrate that EvoTS-Agent consistently outperforms existing LLM-based agents while maintaining a 100\% execution success rate across all evaluated backbone LLMs.

## Metadata
- **Published**: 2026-08-18T15:55:32Z
- **Authors**: Lei Jiang, Ye Wei, Xinyu Xi, Jordan Langham-Lopez, Yifan Bao, Raad Khraishi, Yihao Ang, Anthony K. H. Tung, Lukasz Szpruch, Hao Ni
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17933v1)