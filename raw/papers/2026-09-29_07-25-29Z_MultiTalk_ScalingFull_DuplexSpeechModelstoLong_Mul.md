---
title: MultiTalk: Scaling Full-Duplex Speech Models to Long, Multi-Party, Bilingual Conversation
published: 2026-09-29T07:25:29Z
authors: Ke Wang, Houxing Ren, Zimu Lu, Yunqiao Yang, Zhuofan Zong, Mingjie Zhan, Hongsheng Li
url: http://arxiv.org/abs/2609.36903v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MultiTalk: Scaling Full-Duplex Speech Models to Long, Multi-Party, Bilingual Conversation

## Abstract
End-to-end full-duplex speech models have brought open-source machine conversation closer to human-like interaction, yet existing systems remain limited in two intertwined dimensions: long-context robustness and multi-party interaction. Real-world scenarios such as meetings, group lessons, and social-robot reception require a single model to track, contextualize, and respond to multiple speakers over extended durations. Progress is constrained by both data and evaluation: open multi-party speech corpora remain small and are not designed for codec-frame-level full-duplex modeling, while existing long-audio benchmarks focus on passive listening and speech-to-speech benchmarks are mostly short and dyadic. We extend the Moshi paradigm jointly along the long-horizon and multi-party axes in English and Chinese. First, we release 57.6k hours of synthetic training data ($\href{https://huggingface.co/datasets/MultiTalk/MultiTalkPT}{MultiTalkPT}$ and $\href{https://huggingface.co/datasets/MultiTalk/MultiTalkFT}{MultiTalkFT}$) for long-form, multi-party, English-Chinese full-duplex dialogue, with controllable length, participant count, turn-taking, overlap, backchannels, interruptions, addressee shifts, and long-range coreference. Second, we introduce $\href{https://huggingface.co/datasets/MultiTalk/MultiTalkBench}{MultiTalkBench}$, built from real human recordings, for evaluating long-form, multi-party, bilingual full-duplex dialogue. Conversations average 32.6 minutes and include probes for long-range entity tracking, topic coherence, and addressee selection. Third, we train a bilingual Moshi-style model that sustains coherent multi-party English-Chinese conversations over extended durations and substantially outperforms open-source baselines including Moshi, MiniCPM-o-4.5, and Qwen3-Omni-30B-A3B-Instruct on MultiTalkBench.

## Metadata
- **Published**: 2026-09-29T07:25:29Z
- **Authors**: Ke Wang, Houxing Ren, Zimu Lu, Yunqiao Yang, Zhuofan Zong, Mingjie Zhan, Hongsheng Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.36903v1)