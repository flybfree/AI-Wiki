---
title: A Multi-Dimensional Evaluation of Explainability in Media Bias Detection
published: 2026-07-22T09:29:49Z
authors: Ting Chen, Raina Zhang, Benjamin M. Ampel, Sagar Samtani
url: http://arxiv.org/abs/2607.19954v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Multi-Dimensional Evaluation of Explainability in Media Bias Detection

## Abstract
Detecting media bias automatically is difficult because biased framing is often subtle, yet in domains such as news analysis, accurate predictions alone are insufficient without explanations that reflect the model's underlying reasoning. We present a multi-dimensional evaluation of explainability in encoder-based media bias detection using the Bias Annotations By Experts (BABE) dataset. Specifically, we study BERT and RoBERTa as classifiers (base and large variants) along three complementary axes: predictive performance, explanation plausibility (token-level alignment with expert rationales), and mechanistic faithfulness (whether compact sets of attention heads recover predictive signal under counterfactual rationale masking). To induce variation in plausibility, we additionally investigate attention-supervised finetuning, which incorporates expert rationale annotations as an auxiliary training signal. Attention supervision serves as an intervention on attribution plausibility, while the effectiveness of attribution methods varies substantially across architectures. Circuit analysis further reveals substantial variation in mechanistic recoverability across architectures, suggesting that model scale alone does not determine circuit compressibility. Taken together, our findings suggest that predictive performance, attribution plausibility, and mechanistic faithfulness characterize different aspects of model behavior and should be evaluated separately when studying explainability in media bias detection.

## Metadata
- **Published**: 2026-07-22T09:29:49Z
- **Authors**: Ting Chen, Raina Zhang, Benjamin M. Ampel, Sagar Samtani
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19954v1)