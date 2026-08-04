---
title: FedChronos: Federated Fine-Tuning of Time-Series Foundation Models for Privacy-Preserving Commodity Price Forecasting
published: 2026-08-02T14:59:12Z
authors: Amit Sharma, Nitin Auluck, Akramul Azim
url: http://arxiv.org/abs/2608.01290v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FedChronos: Federated Fine-Tuning of Time-Series Foundation Models for Privacy-Preserving Commodity Price Forecasting

## Abstract
Time-series foundation models (TSFMs) such as Chronos have demonstrated strong forecasting capabilities across domains, yet adapting them to institutionally fragmented settings, where data cannot be centralized due to regulatory, competitive, or sovereignty constraints, remains unexplored. We introduce FedChronos, a framework for federated parameter-efficient fine-tuning of an already pre-trained TSFM, a setting that existing federated time-series work has not addressed, since prior methods either pre-train from scratch or align prototypes rather than adapt a fixed backbone. Our approach applies Low-Rank Adaptation (LoRA) to the Chronos-T5 backbone and trains across distributed clients using FedAvg and FedProx, transmitting only lightweight adapter weights (384~KB per round, an 86$\times$ reduction over full-model exchange). We evaluate FedChronos on daily commodity prices from 15 Indian agricultural markets across 9 states, a naturally non-IID federated setting, and find that naïve LoRA fine-tuning overfits substantially on small per-client datasets, dropping below zero-shot performance. We further observe that differential privacy (DP) noise can act as implicit regularization and counteract this overfitting: in our experiments the strongest configuration ($\varepsilon = 5$) reduces mean absolute percentage error (MAPE) by 31% over zero-shot and 26% over the best traditional baseline, while bounding each round's information leakage via per-round $(\varepsilon, δ)$-differential privacy. Because the model is compact and the updates are small, the approach also suits edge AI deployments where both the network link and the client device are constrained. Overall, our findings suggest that privacy and accuracy can be complementary rather than competing objectives in federated TSFM fine-tuning.

## Metadata
- **Published**: 2026-08-02T14:59:12Z
- **Authors**: Amit Sharma, Nitin Auluck, Akramul Azim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01290v1)