---
title: Disentangling Semantic Attention from Structural Bias in the Attention Manifold
published: 2026-07-27T05:30:19Z
authors: Pengkun Jiao, Bin Zhu, Jingjing Chen, Yu-gang Jiang
url: http://arxiv.org/abs/2607.24017v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Disentangling Semantic Attention from Structural Bias in the Attention Manifold

## Abstract
The empirical success of attention mechanism in Multimodal Large Language Models (MLLMs) often obscures its inherent, subtle flaws. Specifically, MLLMs consistently exhibit disproportionate attention toward certain semantically uninformative visual tokens, a phenomenon termed "register" or "Visual Attention Sinks." While existing inference intervention methods attempt to identify these sink tokens and redistribute their attention weights, such approaches typically treat these tokens in isolation and suffer from computational inefficiency. Instead, we reframe this phenomenon as a generalized textual bias exerted over visual features that extends beyond isolated sink tokens. From this perspective, a pervasive structural bias leads to the dilution of the semantic visual signal, precipitating multimodal hallucinations as the model prioritizes linguistic priors over valid visual evidence. To address this limitation, we introduce Saliency-guided Purification and Adaptive Redistribution (SPAR), a training-free, plug-and-play intervention. SPAR mitigates this generalized textual bias by purifying structural noise and subsequently redistributing the reclaimed attention budget to the most informative visual regions. Comprehensive evaluations across a diverse spectrum of hallucination benchmarks demonstrate that SPAR effectively restores authentic visual grounding with negligible computational overhead.

## Metadata
- **Published**: 2026-07-27T05:30:19Z
- **Authors**: Pengkun Jiao, Bin Zhu, Jingjing Chen, Yu-gang Jiang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24017v1)