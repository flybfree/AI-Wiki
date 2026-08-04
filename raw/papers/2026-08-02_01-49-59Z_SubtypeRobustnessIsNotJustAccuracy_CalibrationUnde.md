---
title: Subtype Robustness Is Not Just Accuracy: Calibration Under Unseen Subtype Shift
published: 2026-08-02T01:49:59Z
authors: Hanyu Su, Carlota Julbe i Juanola, Yibo Hu
url: http://arxiv.org/abs/2608.00928v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Subtype Robustness Is Not Just Accuracy: Calibration Under Unseen Subtype Shift

## Abstract
Subtype robustness asks whether a model keeps the correct coarse prediction when test examples come from fine-grained subtypes absent from training but still inside a known coarse category. Prior work studies this almost entirely through accuracy. We ask whether the model also stays calibrated. We present the first systematic study of the question across ImageNet, BREEDS, iNaturalist and CIFAR-100 with five architectures. Calibration breaks down on unseen subtypes, where accuracy drops while confidence barely follows, leaving the model systematically overconfident exactly where it has become less accurate. At matched accuracy loss, generic image corruption causes a much larger drop in confidence, so the effect is not a general consequence of losing accuracy. The model reacts to visible degradation but not to in-taxonomy novelty. Recalibration tuned on seen subtypes narrows the gap but does not close it, and out-of-distribution scores flag the affected inputs only weakly. Subtype robustness should therefore be evaluated through calibration, not accuracy alone.

## Metadata
- **Published**: 2026-08-02T01:49:59Z
- **Authors**: Hanyu Su, Carlota Julbe i Juanola, Yibo Hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00928v1)