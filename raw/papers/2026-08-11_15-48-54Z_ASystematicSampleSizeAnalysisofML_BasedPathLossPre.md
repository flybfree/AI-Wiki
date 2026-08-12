---
title: A Systematic Sample Size Analysis of ML-Based Path Loss Prediction for LPWAN
published: 2026-08-11T15:48:54Z
authors: Robert Bitterling, Christian Nettersheim, Jörn Hees, Michael Rademacher
url: http://arxiv.org/abs/2608.11083v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Systematic Sample Size Analysis of ML-Based Path Loss Prediction for LPWAN

## Abstract
Low Power Wide Area Networks like LoRa are increasingly deployed for smart city applications, requiring accurate path loss prediction for effective network planning. Traditional (empirical) propagation models often exhibit limited accuracy in these scenarios. We investigate machine learning models for LoRa path loss prediction, systematically analyzing how prediction accuracy scales with training set size using real-world measurements from an urban deployment. Our approach employs a Random Forest with LiDAR-derived terrain features and k-Nearest Neighbors with coordinate data, comparing their performance against established empirical models and specialized LPWAN models. Under random pooled splits, both ML models consistently outperform the considered baseline models across the evaluated training-set sizes. At maximum training size, they achieve RMSE values below 6.5 dB compared to 9.7 dB for the best baseline, indicating accurate within-deployment interpolation. A leave-one-gateway-out check qualifies this result: RF shows placement-dependent transfer to held-out gateways, with moderate degradation for several gateways but larger errors for others, whereas coordinate-only k-NN degrades substantially when the gateway location is unseen

## Metadata
- **Published**: 2026-08-11T15:48:54Z
- **Authors**: Robert Bitterling, Christian Nettersheim, Jörn Hees, Michael Rademacher
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11083v1)