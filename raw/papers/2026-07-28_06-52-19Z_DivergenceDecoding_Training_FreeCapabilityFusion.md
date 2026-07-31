---
title: Divergence Decoding: Training-Free Capability Fusion
published: 2026-07-28T06:52:19Z
authors: Yimi Wang, Hao Li, Shuo Yang, He Cao, Dechen Zhang, Ziang Wu, Zhiyuan Yan, Fanyang Mo, Li Yuan
url: http://arxiv.org/abs/2607.27248v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Divergence Decoding: Training-Free Capability Fusion

## Abstract
While large language models excel in reasoning, these generalists often lack knowledge for specialized scientific domains. Conversely, domain models~(specialists), while knowledgeable, suffer from specialization side-effects including diminished logic and reduced robustness.To address this dilemma, we introduce Divergence Decoding, a training-free framework for capability fusion. It reconstructs the "draft-and-verify" skeleton of speculative decoding into an adaptive routing mechanism. The core is using Jensen-Shannon divergence to monitor the distributional disagreement between the two models at each token. When the specialist exhibits significant divergence, our method identifies it as a potential reasoning risk and instantaneously routes control to the generalist. This allows the dynamic injection of general reasoning while preserving domain expertise, achieving inference-time policy composition of the generalist and the specialist.We evaluate Divergence Decoding across diverse model families (Qwen and Llama series) on challenging scientific benchmarks (GPQA, ChemBench, and ChemCoTBench). Experimental results demonstrate that Divergence Decoding outperforms both the domain-specialized and general-purpose models, effectively surpassing the performance of most single-model baseline. This suggests that Divergence Decoding provides a general, training-free paradigm for fusing diverse LLM capabilities through adaptive inference-time collaboration.

## Metadata
- **Published**: 2026-07-28T06:52:19Z
- **Authors**: Yimi Wang, Hao Li, Shuo Yang, He Cao, Dechen Zhang, Ziang Wu, Zhiyuan Yan, Fanyang Mo, Li Yuan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27248v1)