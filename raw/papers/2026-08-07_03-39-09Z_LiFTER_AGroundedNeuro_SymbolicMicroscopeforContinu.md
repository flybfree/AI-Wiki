---
title: LiFTER: A Grounded Neuro-Symbolic Microscope for Continuous-Time Dynamic Graph Forecasting
published: 2026-08-07T03:39:09Z
authors: Minwoo Yu, Young-guk Ha
url: http://arxiv.org/abs/2608.06765v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LiFTER: A Grounded Neuro-Symbolic Microscope for Continuous-Time Dynamic Graph Forecasting

## Abstract
Continuous-time dynamic graph models predict future links by compressing past interactions into neural states. Although effective for forecasting, this computation obscures which entities are shared across events and how temporal patterns contribute to a prediction. We treat this gap as a property of the predictive architecture rather than a problem to be addressed after prediction. Link-Fact Temporal Rule Inducer (LiFTER) is a neuro-symbolic predictor that preserves observed interactions as grounded temporal facts and applies executable tempo- ral rules to pre-query facts. Each score is a signed sum of rule exe- cutions whose historical facts, entity bindings, and temporal order are explicitly satisfied. The evidence and rules responsible for a prediction can therefore be inspected, independently recomputed, and intervened upon. Across four CTDG benchmarks, LiFTER achieves competitive historical-negative forecasting and the highest macro explanation ac- curacy and deletion fidelity. The same architecture also serves as a microscope that separates the contributions of recurrence, history po- sition, and transition across datasets and traces them to individual facts. Independent execution reconstructs all logits for 19,664 test predictions with a maximum error of 0.0000131. LiFTER turns future-link forecasting into a verifiable grounded computation.

## Metadata
- **Published**: 2026-08-07T03:39:09Z
- **Authors**: Minwoo Yu, Young-guk Ha
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06765v1)