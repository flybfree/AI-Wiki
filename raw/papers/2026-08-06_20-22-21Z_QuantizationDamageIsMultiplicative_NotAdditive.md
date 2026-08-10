---
title: Quantization Damage Is Multiplicative, Not Additive
published: 2026-08-06T20:22:21Z
authors: Zekun Wu, Swati Dhiman, Adriano Koshiyama
url: http://arxiv.org/abs/2608.06564v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Quantization Damage Is Multiplicative, Not Additive

## Abstract
Quantization is how large language models are actually deployed, and below four bits it is known to hurt. What nobody can say is which of the model's decisions will change at a given bit-width. The damage is silent: a compressed agent stops calling its tools, then loses half its safety refusals, yet benchmark scores barely move. Prior work assumes quantization adds noise of a roughly fixed size, which would make confident decisions safe. We measure the decision itself instead. The margin of a two-way decision is the model's score for the option it picks minus the score of its best alternative; we track it before and after quantization across 16 models from 8 model families, three quantization methods, and bit-widths from 8 down to 2. Quantization does not add fixed-size noise to the margin. It multiplies the margin by a factor that collapses with bit-width (median 0.86 at 4 bits, 0.33 at 3, 0.00 at 2); we call this margin shrinkage. This contraction reduces the protection a large margin affords; the model's own small biases pick the direction of failure: at 3 bits the decision to call a tool collapses toward inaction while the choice of which tool is untouched. In fitted statistical comparison, additive-noise accounts never win on the damaged tool and safety decisions. The fitted relation predicts flip rates within a median of 1.8 percentage points on held-out decisions, though no flip was used in the fit; per decision, the predicted flip probabilities are calibrated uncertainty estimates (expected calibration error 0.004 over 131,758 predictions). The same form holds in every model we measure, but the constants are each model's own and do not transfer. A small paired margin set, measured per model and bit-width, estimates which decisions break without full generative evaluation; under our cost-matched tests, nothing repairs damage more cheaply than one more bit.

## Metadata
- **Published**: 2026-08-06T20:22:21Z
- **Authors**: Zekun Wu, Swati Dhiman, Adriano Koshiyama
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06564v1)