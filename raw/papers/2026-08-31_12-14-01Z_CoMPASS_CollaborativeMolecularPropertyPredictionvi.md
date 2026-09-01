---
title: CoMPASS: Collaborative Molecular Property Prediction via Adaptive Small-Large Model Synergy
published: 2026-08-31T12:14:01Z
authors: Wentao Li, Jiangjie Qiu, Yijun Li, Leyi Zhao, Xiaonan Wang
url: http://arxiv.org/abs/2608.30674v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CoMPASS: Collaborative Molecular Property Prediction via Adaptive Small-Large Model Synergy

## Abstract
Accurate molecular property prediction requires both statistical reliability and chemical reasoning. Graph neural networks can be calibrated directly on labeled assays but remain limited by the coverage of their training data. Large language models (LLMs) can compare molecular evidence and articulate chemical rationales, yet are unreliable as standalone quantitative predictors. The central challenge is therefore to determine when an LLM should influence a calibrated model and by how much. Here we present CoMPASS, a retrieval-calibrated framework for small-large model collaboration. CoMPASS retains a graph attention network (GAT) as the predictive anchor, retrieves locally relevant training molecules, provides attention-grounded evidence to an LLM, and converts its proposal into a bounded correction through an agreement-aware gate. Across six classification and two regression benchmarks, CoMPASS improves the GAT anchor in regions of correctable uncertainty while limiting LLM intervention in high-confidence regimes. Ablations show that the gains arise from validation-calibrated retrieval and bounded fusion rather than prompting alone. These results suggest that generative reasoning should augment calibrated prediction through evidence-grounded, controlled corrections rather than direct output replacement. Code is available at https://github.com/littlepeachs/CoMPASS.

## Metadata
- **Published**: 2026-08-31T12:14:01Z
- **Authors**: Wentao Li, Jiangjie Qiu, Yijun Li, Leyi Zhao, Xiaonan Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30674v1)