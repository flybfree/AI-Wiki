---
title: WnW: Waxing-and-Waning KV Cache for Long-Form Speech LLMs
published: 2026-08-24T01:48:30Z
authors: Yiming Yao, Chenyang Lyu, Xuanfan Ni, Longyue Wang, Weihua Luo, Yazheng Yang, Jinsong Su
url: http://arxiv.org/abs/2608.22704v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# WnW: Waxing-and-Waning KV Cache for Long-Form Speech LLMs

## Abstract
Long-form audio inputs make the KV cache the dominant memory cost of speech LLMs. Prefill-only KV compression methods permanently discard audio KV positions once evicted, with no pathway to recover them during decoding. We show this is fragile on long-form audio: prefill attention concentrates near the audio start (an attention-sink effect), while decode-time attention distributes broadly, and the two rankings overlap weakly. We propose WnW (Waxing-and-Waning KV cache), which classifies KV-heads into anchor, tidal, and fixed roles via offline calibration. Anchor heads remain on GPU and serve as a decode-time importance observer; tidal heads keep a CPU-resident complement that is recalled chunk-by-chunk based on aggregated anchor-head scores; fixed heads keep only an on-GPU subset, with the rest permanently discarded. On LibriSpeech-Long with two 3B backbones (Voxtral-mini-3b and Qwen2.5-Omni-3B), WnW preserves near-Full-Cache accuracy while keeping only 20% of audio tokens on GPU, where prefill-only baselines fail to terminate. Results generalize across language, task, and domain shifts, and CPU-GPU recall adds little decode-time overhead in our measurements.

## Metadata
- **Published**: 2026-08-24T01:48:30Z
- **Authors**: Yiming Yao, Chenyang Lyu, Xuanfan Ni, Longyue Wang, Weihua Luo, Yazheng Yang, Jinsong Su
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22704v1)