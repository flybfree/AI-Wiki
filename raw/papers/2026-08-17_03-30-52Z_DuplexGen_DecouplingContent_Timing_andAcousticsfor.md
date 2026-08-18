---
title: DuplexGen: Decoupling Content, Timing, and Acoustics for Synthetic Dialogue Speech
published: 2026-08-17T03:30:52Z
authors: Pengcheng Wang, Sheng Li, Jiyi Li, Takahiro Shinozaki
url: http://arxiv.org/abs/2608.16053v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DuplexGen: Decoupling Content, Timing, and Acoustics for Synthetic Dialogue Speech

## Abstract
Synthetic conversational speech has become an important resource for developing and evaluating conversational speech systems. However, existing dialogue synthesis pipelines typically generate dialogue content first and then insert interruptions, overlap, and backchannels using handcrafted markers or timing rules, making conversational timing prescribed rather than interaction-driven. We present DuplexGen, a dialogue synthesis framework that explicitly decouples content, timing, and acoustics. An LLM first generates the dialogue script, and then two full-duplex conversational models perform the script while listening to each other in real time. This allows conversational timing to emerge naturally while preserving the scripted content. Finally, a high-fidelity text-to-speech model re-renders the interaction without altering its timing. As a demonstration of the proposed framework, we construct a patient--clinician conversational speech corpus with construction-time annotations, including word timestamps, speaker activity, overlap regions, and interaction events. Experimental results show that the proposed framework produces conversational dynamics closer to real dialogue than conventional stitching-based synthesis.

## Metadata
- **Published**: 2026-08-17T03:30:52Z
- **Authors**: Pengcheng Wang, Sheng Li, Jiyi Li, Takahiro Shinozaki
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16053v1)