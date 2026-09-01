---
title: TSPFN: A Temporal Tabular Foundation Model for Physiological Time Series Classification
published: 2026-08-31T15:58:22Z
authors: Jérémie Stym-Popper, Clément Rambour, Federica Granese, Nicolas Thome, Olivier Bernard
url: http://arxiv.org/abs/2608.31013v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TSPFN: A Temporal Tabular Foundation Model for Physiological Time Series Classification

## Abstract
Designing models that generalize effectively in low- to medium-data regimes remains a primary challenge in medical machine learning, particularly for physiological time-series classification. While tabular foundation models such as TabPFN offer an attractive alternative to conventional fine-tuning through in-context learning, they are not designed to capture the temporal dependencies inherent to physiological signals. ~In this paper, we introduce TSPFN, a foundation model that redesigns TabPFN's architecture for time series data. TSPFN integrates structured temporal representations and positional embeddings to capture intra-sample temporal and channel dependencies. To fully leverage its spatio-temporal design, the model is pretrained on 140,000 real-world physiological time series across multiple medical domains. This yields a unified, generalizable framework capable of learning the specificities of medical time series. Experiments across diverse physiological benchmarks demonstrate that TSPFN consistently outperforms standard tabular baselines and TabPFN, and achieves superior cross-domain generalization compared to specialized deep time-series models. All our experiments, ablation studies, and pre-processing scheme are publicly available at https://github.com/Jeremstym/TSPFN

## Metadata
- **Published**: 2026-08-31T15:58:22Z
- **Authors**: Jérémie Stym-Popper, Clément Rambour, Federica Granese, Nicolas Thome, Olivier Bernard
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.31013v1)