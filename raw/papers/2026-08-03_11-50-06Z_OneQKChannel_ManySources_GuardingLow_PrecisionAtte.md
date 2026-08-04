---
title: One QK Channel, Many Sources: Guarding Low-Precision Attention Collapse
published: 2026-08-03T11:50:06Z
authors: Shuxiao Xie, Shuyang Xie, Yuan Cao, Dezhi Ran, Wei Yang, Tao Xie
url: http://arxiv.org/abs/2608.02091v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# One QK Channel, Many Sources: Guarding Low-Precision Attention Collapse

## Abstract
A bfloat16 transformer can train normally for many steps and then collapse abruptly. Distinct low-precision errors can trigger the same failure, leaving unclear whether each source needs its own repair or one shared route can be blocked. We isolate a reproduced GPT-2-class collapse to the streaming-softmax accumulator, where fp32 accumulation repairs it, and use the fault as an assay for moving controlled errors across sources. Errors placed outside attention still drive the same query-key (QK) spectral runaway, while correcting only QK keeps training stable with the source fault active. This source-channel dissociation shows that fault source is not failure channel. It holds across the tested architectures and scales and reproduces on a second GPU architecture. A causal probe projects each update off the current QK weights' leading three singular directions: the query projection's largest singular value stays at 11.1, whereas removing equal energy elsewhere leaves it at 237. The QK channel therefore drives the early runaway rather than merely tracking it. Entry depends on temporal sign-coherence across steps, not aggregate deviation. QK-Guard closes the channel with a dormant controller that switches on parameter-free QK normalization when attention-logit saturation begins. It contains every tested runaway and matches always-on QK normalization over 60k steps, while non-QK actions at the same trigger fail. The results support intervention at the shared QK locus rather than separate repair at each fault source.

## Metadata
- **Published**: 2026-08-03T11:50:06Z
- **Authors**: Shuxiao Xie, Shuyang Xie, Yuan Cao, Dezhi Ran, Wei Yang, Tao Xie
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02091v1)