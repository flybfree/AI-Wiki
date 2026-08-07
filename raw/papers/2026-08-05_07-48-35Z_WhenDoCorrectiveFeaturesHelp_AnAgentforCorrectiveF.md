---
title: When Do Corrective Features Help? An Agent for Corrective Feature Discovery on Black-Box Forecasters
published: 2026-08-05T07:48:35Z
authors: Fangxin Wang, Ziyi Zhang, Diyi Zhuang, Langzhou He, Shiyu Wang, Baichuan Mo, Philip S. Yu
url: http://arxiv.org/abs/2608.05207v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Do Corrective Features Help? An Agent for Corrective Feature Discovery on Black-Box Forecasters

## Abstract
Frozen pretrained forecasters often fail in structured, recurring ways that are costly to repair through fine-tuning. We study corrective feature discovery: mining interpretable features of a frozen forecaster's residual to drive a lightweight post-hoc corrector. Prior automated feature engineering models the data-generating process; corrective features instead model the model-failure process. We present CRAFTER (Corrective Residual Agent with Feature-based Temporal Exploration and Reasoning), which keeps the backbone frozen and mines its residual with two complementary generators: a compositional search over the raw input channels, and a large language model (LLM) that proposes named feature combinations, binary flags, and short executable code. A single validation-grounded gate accepts or rejects every candidate regardless of its origin, and a validation-selected corrector applies the accepted features or leaves the forecast unchanged. This source-agnostic pipeline also allows prior feature-engineering systems to be evaluated under identical conditions, making CRAFTER an instrument for attributing forecast improvements to the feature source alone. Across six public datasets and six frozen backbones, CRAFTER surpasses every dedicated feature-engineering system at every feature budget, roughly doubling the improvement achieved by the corrector alone and reducing the error of the weakest backbones by up to 27%. These gains are robust across different LLM backends and persist even when applied on top of fine-tuned backbones.

## Metadata
- **Published**: 2026-08-05T07:48:35Z
- **Authors**: Fangxin Wang, Ziyi Zhang, Diyi Zhuang, Langzhou He, Shiyu Wang, Baichuan Mo, Philip S. Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05207v1)