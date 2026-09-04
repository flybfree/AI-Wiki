---
title: CRAW: Codec Robust Audio Watermarking
published: 2026-09-02T19:44:04Z
authors: David Chernin, Ethan Fetaya
url: http://arxiv.org/abs/2609.03107v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CRAW: Codec Robust Audio Watermarking

## Abstract
Recent advances in generative speech models have made it increasingly difficult to distinguish authentic from synthetic audio, enabling new forms of fraud and misinformation. Audio watermarking offers a promising defense by embedding an imperceptible signal into generated speech that can later be detected to verify its provenance. However, recent studies have shown that existing post-hoc watermarking methods fail under neural codecs and denoisers, transformations routinely applied during real-world storage, transmission, and processing, severely limiting their practical utility. Here we introduce CRAW, a codec-robust audio watermarking framework that jointly improves robustness against neural re-synthesis while maintaining high perceptual quality. CRAW combines distortion-aware training with an attention-based pooling mechanism, inference-time perceptual mask- ing, and an error-correcting code to recover the fidelity lost during robust training. Experiments demonstrate that CRAW achieves state-of-the-art robustness against neural codecs, denoisers, and vocoders while maintaining perceptual quality comparable to existing post-hoc watermarking methods. The code is available at https://github.com/DavidC1212/craw.

## Metadata
- **Published**: 2026-09-02T19:44:04Z
- **Authors**: David Chernin, Ethan Fetaya
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03107v1)