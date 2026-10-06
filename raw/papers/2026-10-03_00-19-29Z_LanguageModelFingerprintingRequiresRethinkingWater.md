---
title: Language Model Fingerprinting Requires Rethinking Watermark Teachers
published: 2026-10-03T00:19:29Z
authors: Jeongyeon Hwang, Anshul Nasery, Sewoong Oh, Jungseul Ok
url: http://arxiv.org/abs/2610.04169v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Language Model Fingerprinting Requires Rethinking Watermark Teachers

## Abstract
LLM fingerprinting via watermark distillation embeds a statistical watermark signal into model weights, enabling model owners to identify their models behind black-box APIs. Revisiting a recent protocol, we find that its utility evaluation understates text quality degradation in open-ended generation, favoring overly strong watermark teachers. Weakening the watermark improves text quality but sacrifices detectability. To move beyond this trade-off, we rethink whether text watermarks designed for verifying generated text are suitable distillation teachers for model fingerprinting. Such watermarks are typically designed to remain detectable from an individual output, limiting how sparse the watermark signal can be. In contrast, fingerprint verification can aggregate signal across queries, making sparser watermark signals viable. This raises a key question: where should the sparse signal be placed? We analyze signal placement through token surprisal and show that, even at comparable watermark strength, different placements can target tokens with different plausibility under the base model. This motivates near-tie restriction, which uses top-1-relative logit gaps to restrict the watermark bias to tokens close to the base model's top prediction. Across multiple models, near-tie improves detection--quality frontiers under deployment changes, preserves higher text quality across query budgets, and further improves existing watermarking schemes when combined with them.

## Metadata
- **Published**: 2026-10-03T00:19:29Z
- **Authors**: Jeongyeon Hwang, Anshul Nasery, Sewoong Oh, Jungseul Ok
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04169v1)