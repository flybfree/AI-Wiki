---
title: StepJack: Benchmarking Computer-Use Agent Safety Against Multi-Step Indirect Prompt Injection
published: 2026-08-06T18:14:30Z
authors: Zhuoxin Zhan, Akbar Rafiey, Avery Ma, Leila Pishdad, Layla El Asri
url: http://arxiv.org/abs/2608.06477v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# StepJack: Benchmarking Computer-Use Agent Safety Against Multi-Step Indirect Prompt Injection

## Abstract
Computer-use agents (CUAs) face a growing threat from indirect prompt injection, where adversarial instructions are planted in the environment such as web pages. In this paper, we introduce multi-step indirect prompt injection, a new attack class against CUAs in which the adversarial goal is decomposed into multiple innocuous-looking sub-steps and distributed across a chain of pages referenced along the agent's navigation path. We develop a pipeline to automatically decompose an adversarial goal under the constraint that the execution of the decomposed sub-steps must achieve the original goal while optimizing the innocuousness of each decomposed sub-step. With this pipeline, we build StepJack, a CUA safety benchmark with 480 test examples. On this benchmark, we evaluate six state-of-the-art CUAs and find that at a fixed decomposition depth, multi-step attacks raise attack success rate (ASR) on three of six CUAs, by up to 31.2 points (e.g., GPT-5.4-mini: 41.7% at single-step to 72.9% at three-step); averaged over the five CUAs that can reliably follow the reference chain (all but EvoCUA-32B), ASR rises from 31.3% at single-step to 36.9% at three-step. Dataset and code are available at https://github.com/BorealisAI/StepJack.

## Metadata
- **Published**: 2026-08-06T18:14:30Z
- **Authors**: Zhuoxin Zhan, Akbar Rafiey, Avery Ma, Leila Pishdad, Layla El Asri
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06477v1)