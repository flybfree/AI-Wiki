---
title: Z-PEFT: Zero-shot Backdoor Detection in Parameter-Efficient Fine-Tuning via Canonical Spectral Signatures
published: 2026-08-03T14:10:54Z
authors: Nicola Pitzalis, Donald Shenaj, Giacomo Cignoni, Andrea Cossu, Davide Bacciu, Antonio Carta
url: http://arxiv.org/abs/2608.02271v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Z-PEFT: Zero-shot Backdoor Detection in Parameter-Efficient Fine-Tuning via Canonical Spectral Signatures

## Abstract
Parameter-Efficient Fine-tuned (PEFT) models are frequently downloaded from open repositories by practitioners. This widespread practice creates a significant attack surface, as malicious actors can publish backdoored models that induce specific behaviors in response to predefined triggers. We study the problem of weight-space backdoor detection, where a detector classifier predicts whether a model is malicious using only its weights, enabling a lightweight safety mechanism. Most existing methods are designed and evaluated in a closed-world setting, where the detector is trained and tested on the same attack type. In contrast, we evaluate backdoor detection under novel conditions, including previously unseen attacks and datasets. We propose Z-PEFT, a lightweight meta-classifier that relies exclusively on layer-wise spectral measures for classification. Our experiments show that strong performance in the closed-world setting does not necessarily translate to high accuracy in zero-shot backdoor detection. Among weight-space detectors, Z-PEFT achieves the best performance while maintaining low and scalable computational cost.

## Metadata
- **Published**: 2026-08-03T14:10:54Z
- **Authors**: Nicola Pitzalis, Donald Shenaj, Giacomo Cignoni, Andrea Cossu, Davide Bacciu, Antonio Carta
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02271v1)