---
title: ixi-sLM: On-Device sLM for AI Call Agent Service
published: 2026-10-14T01:29:08Z
authors: Han-Sang Lee, Kyuho Lee, Juneyoung Park, Seongbae Lee, Jin Kyu Park, Minjae Kim, Yuri Hong, Jinwoo Lee, Youngwook Kwon, Seongwan Kim, Seungheon Hyeon, Jaeho Lee, Kiduk Kwon
url: http://arxiv.org/abs/2610.19382v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ixi-sLM: On-Device sLM for AI Call Agent Service

## Abstract
Running an AI call agent on-device makes it private, network-independent, and free of per-query cloud cost, but shipping one as a real-world service imposes constraints a cloud deployment never faces: ~1GiB memory budget, in-call latency and thermal limits, static-integer NPU execution, Korean STT input far from sLM pretraining, and cloud-level quality expectations. We bring ixi-sLM, a 1.2B Korean sLM, to mobile NPUs through ON-DEVICE MODELING: domain-adaptive modeling trims the vocabulary by call frequency to shrink the embedding and LM head that take nearly half the model under INT4 transformer weights and refits the tokenizer to call speech (18% fewer tokens on call traffic), while task-aware quantization calibrates on real calls and assigns per-module mixed precision by activation sensitivity. A single domain-adapted model runs ixi-O's two production services, AI Call Summary and AI Call Answering, at 94% of a state-of-the-art cloud LLM's task-weighted quality; our on-device modeling carries that quality onto the NPU with only a marginal drop in overall score, in an 803MiB model (28% of FP16) at 23% of the CPU's per-call energy. The same recipe deploys across Qualcomm and Apple NPUs and serves several million ixi-O subscribers in production.

## Metadata
- **Published**: 2026-10-14T01:29:08Z
- **Authors**: Han-Sang Lee, Kyuho Lee, Juneyoung Park, Seongbae Lee, Jin Kyu Park, Minjae Kim, Yuri Hong, Jinwoo Lee, Youngwook Kwon, Seongwan Kim, Seungheon Hyeon, Jaeho Lee, Kiduk Kwon
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.19382v1)