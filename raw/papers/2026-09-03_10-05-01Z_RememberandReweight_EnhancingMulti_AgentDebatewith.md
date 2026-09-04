---
title: Remember and Reweight: Enhancing Multi-Agent Debate with Experience Memory and Confidence Estimation
published: 2026-09-03T10:05:01Z
authors: Xuanfa Jin, Zhijian Ma, Yongcheng Zeng, Xinyu Cui, Haifeng Zhang, Jun Wang
url: http://arxiv.org/abs/2609.03619v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Remember and Reweight: Enhancing Multi-Agent Debate with Experience Memory and Confidence Estimation

## Abstract
Multi-agent debate (MAD) improves the reasoning capabilities of large language models by having multiple agents iteratively refine their responses through discussion. However, MAD suffers from a critical vulnerability known as shared misconception: when a majority of agents initially converge on an incorrect answer, the debate process tends to amplify rather than correct the error. Existing methods primarily address peer skew but leave the agents' inherently biased concept priors unaddressed. To mitigate this systematic weakness, we propose R$^2$-MAD (Remember and Reweight for Multi-Agent Debate), a framework that equips agents with an experience memory accumulated from past debates. R$^2$-MAD intervenes on both failure modes through two complementary mechanisms: A debate-state-aware retrieval policy dynamically calibrates the concept prior by retrieving relevant historical evidence based on the current consensus level. Then these retrieved experiences provide a basis for estimating per-agent reliability, yielding confidence weights to modulate peer influence. Experiments on various benchmarks show that R$^2$-MAD achieves consistent improvements over existing single-agent and MAD baselines.

## Metadata
- **Published**: 2026-09-03T10:05:01Z
- **Authors**: Xuanfa Jin, Zhijian Ma, Yongcheng Zeng, Xinyu Cui, Haifeng Zhang, Jun Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03619v1)