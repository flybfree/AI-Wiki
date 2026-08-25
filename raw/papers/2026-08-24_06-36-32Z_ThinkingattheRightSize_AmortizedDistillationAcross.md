---
title: Thinking at the Right Size: Amortized Distillation Across Post-Trained LLMs
published: 2026-08-24T06:36:32Z
authors: Yan Zhou, Sara Kangaslahti, Jonathan Geuter, Nihal V. Nayak, Marco Fumero, Francesco Locatello, David Alvarez-Melis
url: http://arxiv.org/abs/2608.22854v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Thinking at the Right Size: Amortized Distillation Across Post-Trained LLMs

## Abstract
Practical deployment of large language models (LLMs) requires families of post-trained variants---instruction-tuned, reasoning-tuned, and chat-style models---each at multiple sizes to meet diverse latency and memory budgets. Producing each (variant, size) pair independently is prohibitive, so model families typically span only a handful of coarse-grained sizes per post-trained variant. Boomerang distillation (Kangaslahti et al., 2026) reduces this cost along the size axis for base models. Through model size interpolation, it constructs models of intermediate sizes from a single teacher-student pair without additional training. However, it still treats each post-trained variant as a separate object of optimization. We introduce ADAPT---Amortized Distillation Across Post-Trained LLMs---a framework for amortizing distillation across both axes of a model family: size and post-training variant, producing $L \times K$ models for $L$ interpolated sizes across $K$ post-trained variants with a single distillation run. ADAPT combines two components. First, a two-phase distillation procedure constructs post-trained students through pre-training alignment and supervised fine-tuning distillation, enabling smooth size--performance interpolation on generation and reasoning tasks. Second, weight-delta initialization approximates this construction across post-trained variants by transferring the distillation-induced weight change from the base model to students initialized from different post-trained variants. The resulting continuum of interpolated models also enables adaptive model-size selection at inference time, improving the compute--accuracy trade-off for long-form reasoning tasks.

## Metadata
- **Published**: 2026-08-24T06:36:32Z
- **Authors**: Yan Zhou, Sara Kangaslahti, Jonathan Geuter, Nihal V. Nayak, Marco Fumero, Francesco Locatello, David Alvarez-Melis
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22854v1)