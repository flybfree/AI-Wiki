---
title: The Intruder Threshold: A Spectral Law for LoRA Fine-Tuning
published: 2026-07-26T15:17:41Z
authors: Peng Xie
url: http://arxiv.org/abs/2607.23711v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Intruder Threshold: A Spectral Law for LoRA Fine-Tuning

## Abstract
LoRA fine-tuning can create intruder dimensions: new leading singular vectors of the updated weight matrix $W+BA$ that are nearly orthogonal to all pretrained singular vectors and that drive catastrophic forgetting. Since their discovery, no theory has predicted, layer by layer on measured spectra, when they appear. We derive a per-layer critical update strength $s^\ast=\barθ/(γσ_1(BA))$, computed from the measured spectrum of $W$ alone through the rectangular spiked-deformation transform, together with an exact secular-equation characterization of the updated spectrum, with no fitted parameters. In a pre-specified study spanning four dense Transformer families, a state-space model, a mixture-of-experts model, and an encoder-decoder (18 adapters, 9{,}840 layer scans), the law localizes the empirical threshold within a factor of two on $82\%$ of layers, separates intruder-bearing from intruder-free layers at deployment with a mean AUC of $0.89$, holds unchanged on six third-party adapters, and predicts where WikiText-2 perplexity begins to degrade; a combination of the two pre-specified edge evaluations reaches $98\%$ and is confirmed out-of-bag on the external adapters ($0.997$). Full fine-tuning disperses its update far below the threshold of every layer, which resolves the asymmetry between LoRA and full fine-tuning. Norm-matched interventions confirm that threshold-crossing layers, rather than update magnitude, carry the forgetting, and a spike-budget rule derived from the thresholds, requiring one SVD and no validation sweeps, reduces forgetting by $62\%$ on the most fragile model at no task cost.

## Metadata
- **Published**: 2026-07-26T15:17:41Z
- **Authors**: Peng Xie
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23711v1)