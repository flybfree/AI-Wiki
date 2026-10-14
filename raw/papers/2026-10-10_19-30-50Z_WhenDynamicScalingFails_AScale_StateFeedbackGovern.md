---
title: When Dynamic Scaling Fails: A Scale-State Feedback Governs Recurrent-State Quantization in Linear-Attention and SSM LLMs
published: 2026-10-10T19:30:50Z
authors: Yuhang Jiang
url: http://arxiv.org/abs/2610.15139v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Dynamic Scaling Fails: A Scale-State Feedback Governs Recurrent-State Quantization in Linear-Attention and SSM LLMs

## Abstract
Linear-attention and state-space LLMs carry long context in a fixed-size recurrent state, and quantizing that state is the natural way to cut its cost during long decode. Unlike a weight tensor, the state is rewritten at every step, so a quantizer applied at each step sits inside the recurrence and its errors compound. INT4 that leaves synthetic recall perfectly intact at the start destroys it a thousand steps later. The mechanism is a feedback between the quantizer scale and the state it is derived from. Yoking that scale to a full-precision reference removes the resulting norm explosion entirely, yet recovers only 1.8 of the 5.4 nats lost, so numerical instability and functional degradation are separable failures. The remainder is a resolution problem that locating outliers does not solve, since every outlier-aware scheme here loses to plain persistent scaling. Allocating bits across layers does help, but under article-disjoint splits a learned allocation collapses onto the trivial rule of protecting the first few layers. Run out to 32K, group-wise INT4 is worth no more than discarding the state. Contain the scale rather than locate outliers, and report the decode horizon at which a bit-width was certified.

## Metadata
- **Published**: 2026-10-10T19:30:50Z
- **Authors**: Yuhang Jiang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.15139v1)