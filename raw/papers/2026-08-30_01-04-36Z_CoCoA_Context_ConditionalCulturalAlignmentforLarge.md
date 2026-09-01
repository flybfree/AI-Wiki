---
title: CoCoA: Context-Conditional Cultural Alignment for Large Language Models
published: 2026-08-30T01:04:36Z
authors: Kyungdon Lee, Wei Xu, Alan Ritter, Dong-Ho Lee, JinYeong Bak
url: http://arxiv.org/abs/2608.29492v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CoCoA: Context-Conditional Cultural Alignment for Large Language Models

## Abstract
Large Language Models (LLMs) often favor Western-associated entities across cultural contexts. Conventional debiasing methods aim for uniform neutrality, but cultural bias mitigation demands context-conditional behavior, preferring culturally appropriate entities when cultural cues are present and remaining neutral when they are absent. We propose CoCoA (Context-Conditional Cultural Alignment), a framework that learns this behavior through dual-context training on the same entity pairs under contexts with and without cultural cues. CoCoA combines a contrastive alignment objective with calibration and drift regularization, optimized through goal-aware gradient reconciliation. We evaluate CoCoA on CAMeL and Camellia, two entity-centric cultural bias benchmarks, across ten language settings and four LLMs. CoCoA reduces the Cultural Bias Score from 43 to 24 on average while maintaining near-neutral preferences at 50.2, with minimal impact on general performance across five standard benchmarks. These findings highlight that effective cultural alignment requires context-conditional modeling rather than uniform debiasing, and establish a new direction for mitigating entity-centric cultural bias in LLMs.

## Metadata
- **Published**: 2026-08-30T01:04:36Z
- **Authors**: Kyungdon Lee, Wei Xu, Alan Ritter, Dong-Ho Lee, JinYeong Bak
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29492v1)