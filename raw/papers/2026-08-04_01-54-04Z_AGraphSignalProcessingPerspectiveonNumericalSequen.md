---
title: A Graph Signal Processing Perspective on Numerical Sequence Representations in LLM In-Context Learning
published: 2026-08-04T01:54:04Z
authors: Jiajun Bao, Zihao Qi, Toni J. B. Liu, Gurbir Arora, Raphaël Sarfati, Nicolas Boullé, Christopher J. Earls
url: http://arxiv.org/abs/2608.03015v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Graph Signal Processing Perspective on Numerical Sequence Representations in LLM In-Context Learning

## Abstract
Pretrained large language models (LLMs) have demonstrated in-context learning (ICL) capabilities for numerical inference over sequences serialized as text. Prior work has identified and characterized this form of numerical inference primarily through output-level evaluations such as prediction error. However, how numerical information is organized within LLM representations remains much less understood. To study this internal organization, we adopt a graph signal processing perspective in which attention induces a weighted graph over tokens, while token hidden states define signals on its nodes. Quantitative graph-spectral diagnostics and qualitative token-graph visualizations reveal that representations become more clearly differentiated by input dynamical complexity as context length increases. Simpler inputs produce attention-induced token graphs with stronger global connectivity and smoother, spectrally concentrated hidden-state signals, whereas more complex inputs produce more localized graphs and hidden-state signals with broader spectral support and greater high-frequency energy. Together, these findings point to systematic, context-dependent internal signatures associated with numerical ICL that are conserved across model families.

## Metadata
- **Published**: 2026-08-04T01:54:04Z
- **Authors**: Jiajun Bao, Zihao Qi, Toni J. B. Liu, Gurbir Arora, Raphaël Sarfati, Nicolas Boullé, Christopher J. Earls
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03015v1)