---
title: Beyond Static and Linear: What Attention Constraints Best Fit Human Reading Times?
published: 2026-08-24T20:54:29Z
authors: Lanni Bu, Xiulin Yang, Christian Clark, Alex Warstadt, Ethan Gotlieb Wilcox
url: http://arxiv.org/abs/2608.23818v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Static and Linear: What Attention Constraints Best Fit Human Reading Times?

## Abstract
Transformer-based language models are widely used as models of human language processing, yet their attention mechanisms allow lossless access to the full preceding context, unlike the limited memory systems of humans. We hypothesize that installing memory constraints into transformers' attention mechanisms can improve their fit to human behavioral data. While previous work has explored individual constraints in isolation, we conduct a systematic comparison of multiple attention-based memory mechanisms across different model sizes and training corpora, evaluating both psychometric predictive power for human reading times and grammatical competence. We additionally compare static constraints, in which the constraint strength is fixed throughout training, to dynamic memory curricula. We find that constraints that are sensitive to the content of intervening tokens consistently achieve the highest alignment with human reading times, outperforming distance-based constraints. We observe a dissociation between psychometric fit and grammatical competence under dynamic memory curricula, suggesting that Transformers cannot serve as a one-size-fits-all cognitive model.

## Metadata
- **Published**: 2026-08-24T20:54:29Z
- **Authors**: Lanni Bu, Xiulin Yang, Christian Clark, Alex Warstadt, Ethan Gotlieb Wilcox
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23818v1)