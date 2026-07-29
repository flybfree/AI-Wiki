---
title: Where Steering Signals Come From: Activation Source Selection in Activation Steering
published: 2026-07-28T04:18:24Z
authors: Jiaran Ye, Lingxu Ran, Zijun Yao, Chenpeng Wang, Yong Jiang, Lei Hou, Juanzi Li, Liangming Pan
url: http://arxiv.org/abs/2607.25270v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Where Steering Signals Come From: Activation Source Selection in Activation Steering

## Abstract
Activation steering controls language models by adding vectors or features to hidden states at inference time, but the upstream source of these steering signals is often treated as a secondary detail. We study this source choice as activation source selection: the combination of source context and activation readout policy used to collect the hidden states from which a steering signal is built. Holding the downstream intervention fixed, we show across three instruction-tuned models and four steering task families that changing only the source activations substantially changes steering success. We further find that effective steering is not explained simply by whether the desired behavior appears in the source text. Instead, strong signals come from execution-boundary states, where the model is about to produce or continue the target behavior. This pre-/post-realization distinction explains why answer-based sources sometimes work: their useful component aligns with execution-boundary directions rather than target appearance alone. Building on this view, we introduce tail subtraction, which removes shared prompt and continuation semantics from boundary states and yields cleaner, more stable steering signals. Overall, our results suggest that steering depends on representations of what the model is about to do, not merely on what has already appeared.

## Metadata
- **Published**: 2026-07-28T04:18:24Z
- **Authors**: Jiaran Ye, Lingxu Ran, Zijun Yao, Chenpeng Wang, Yong Jiang, Lei Hou, Juanzi Li, Liangming Pan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25270v1)