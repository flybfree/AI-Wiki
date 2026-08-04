---
title: TabDPT-Turbo: Efficient In-Context Learning for Tabular Prediction
published: 2026-08-02T17:33:30Z
authors: Rasa Hosseinzadeh, Alex Labach, Zexin Xue, Shuyi Han, Valentin Thomas, Anthony L. Caterini
url: http://arxiv.org/abs/2608.01400v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TabDPT-Turbo: Efficient In-Context Learning for Tabular Prediction

## Abstract
Tabular foundation models, driven by in-context learning, have rapidly grown in quality and popularity. However, recent approaches with either cell-based architectures or retrieval have sacrificed efficiency for raw performance, restricting their utility in situations where compute is limited or inference speed is crucial. We adopt an alternate approach, sticking with row-based attention while incorporating long context pre-training to eliminate the need for retrieval. By combining this with architectural improvements and SSL pre-training on a newly-sourced, larger corpus of real data results, we present TabDPT-Turbo, a model that provides comparable default performance to TabDPT v1.1 on TabArena-Lite, CC18, and CTR23, at orders of magnitude faster. In our experiments, TabDPT-Turbo is the fastest model overall among leading foundation models. We have released the new model as TabDPT v1.2 at https://github.com/layer6ai-labs/TabDPT-inference.

## Metadata
- **Published**: 2026-08-02T17:33:30Z
- **Authors**: Rasa Hosseinzadeh, Alex Labach, Zexin Xue, Shuyi Han, Valentin Thomas, Anthony L. Caterini
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01400v1)