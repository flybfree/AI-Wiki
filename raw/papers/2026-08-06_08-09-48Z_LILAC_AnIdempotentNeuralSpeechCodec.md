---
title: LILAC: An Idempotent Neural Speech Codec
published: 2026-08-06T08:09:48Z
authors: June Young Yi, Dongwook Lee, Jiheum Yeom, Sungroh Yoon
url: http://arxiv.org/abs/2608.05727v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LILAC: An Idempotent Neural Speech Codec

## Abstract
Neural Audio Codecs are widely adopted in speech generation and editing. However, existing neural audio codecs are not idempotent: across the paper's twelve baseline systems, every configuration tested rewrites, on average, at least 15% of its tokens in a single decode-re-encode pass. This poses a problem for utilizing Neural Audio Codecs as token interfaces in pipelines where re-encoding decoded outputs can occur. We present LILAC, a fully convolutional 24 kHz speech codec at 9.375 Hz and 0.75 kbit/s that is codec idempotent by construction; re-encoding the decoded audio of any valid token stream returns the identical stream. LILAC achieves idempotency while maintaining competitive quality, reaching UTMOS 4.14 and 4.24 on LibriSpeech and LibriTTS-R test sets, comparable to SOTA sub-1 kbit/s Neural Audio Codecs.

## Metadata
- **Published**: 2026-08-06T08:09:48Z
- **Authors**: June Young Yi, Dongwook Lee, Jiheum Yeom, Sungroh Yoon
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05727v1)