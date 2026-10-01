---
title: Low-Discrepancy Dither for Quantized Recurrent State Caches
published: 2026-09-30T07:41:07Z
authors: Snigdha Chandan Khilar
url: http://arxiv.org/abs/2609.39185v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Low-Discrepancy Dither for Quantized Recurrent State Caches

## Abstract
Mamba-style and hybrid language models compress their past into a fixed-size recurrent state that is rewritten at every generated token. Storing this state in low precision saves memory bandwidth, but every rounding error is fed back into the next update and can accumulate over long generations. Production systems round the state stochastically; we ask which rounding rule such caches should use. We find that a deterministic golden-ratio Weyl dither, which needs no random numbers, consistently brings the quantized model closer to the full-precision one than stochastic rounding, across pure and hybrid models, storage formats, and long decoding horizons, at no extra cost. Round-to-nearest behaves differently: because it discards small updates, its error keeps growing, so it can look best in short evaluations yet falls far behind over long generations. A discrepancy analysis explains this ordering, and we document implementation pitfalls that silently remove the benefit.

## Metadata
- **Published**: 2026-09-30T07:41:07Z
- **Authors**: Snigdha Chandan Khilar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.39185v1)