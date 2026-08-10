---
title: WorldMark: A Plug-and-Play World Knowledge Interface for Cross-Host Language Model Watermarking
published: 2026-08-05T16:34:32Z
authors: Song Xiao, Yuqi Yuan, Yanshuo Zhang, Kejun Zhang
url: http://arxiv.org/abs/2608.06416v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# WorldMark: A Plug-and-Play World Knowledge Interface for Cross-Host Language Model Watermarking

## Abstract
Watermarking traces the provenance of text produced by large language models by embedding statistically detectable signals during decoding. Existing schemes fall into logits-based, sampling-based, entropy-aware, and adaptive-strength families, yet all of them place watermark signals according to local token statistics. In the open-ended text-generation settings evaluated in this work, local statistics may provide insufficient guidance for placing robust watermark signals. We introduce WorldMark, a plug-and-play interface that uses World Knowledge Memory (WKM) to organize semantic and episodic knowledge in a memory graph, converts the retrieved knowledge into a token-level knowledge saliency score, and adjusts the strength of a host watermark through Asymmetric Knowledge Modulation (AKM). WorldMark requires no backbone retraining and introduces no additional detector-side model or parameter. On the primary C4 evaluation, the complete WorldMark interface improves clean and attacked detection across three adaptive-strength host variants while slightly reducing perplexity. Additional pilot experiments on C4 and OpenGen show that direct memory conditioning transfers across multiple watermark families but can be unstable without saliency-aware modulation. WorldMark requires no additional detector-side model or parameter and introduces negligible overhead under the primary protocol.

## Metadata
- **Published**: 2026-08-05T16:34:32Z
- **Authors**: Song Xiao, Yuqi Yuan, Yanshuo Zhang, Kejun Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06416v1)