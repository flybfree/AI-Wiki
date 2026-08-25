---
title: OVIBench: Benchmarking Online Video Question Answering under Interruption
published: 2026-08-23T08:12:08Z
authors: Naiming Liu, Zhiheng Wu, Shuning Wang, Tie Zhang, Bowen Liu, Tong Wang
url: http://arxiv.org/abs/2608.22279v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# OVIBench: Benchmarking Online Video Question Answering under Interruption

## Abstract
Recent vision language models (VLMs) have achieved strong progress in video understanding. However, most existing video QA research and benchmarks still follow an offline, single-round paradigm, overlooking realistic interactions where users may interrupt the model during answer generation. To address this gap, we formulate the task of Online Video Question Answering under Interruption and introduce OVIBench, the first standardized benchmark for evaluating VLMs in this setting. OVIBench categorizes interruptions into three types: Cancellation, False Trigger, Correction and supports both open-ended and multiple-choice evaluations. To enable large-scale and reproducible testing, we develop an offline simulation protocol that reproduces interruption during generation under a unified temporal setup, together with a multi-dimensional metric suite for assessing interruption understanding and response generation. Experiments demonstrate that OVIBench effectively distinguishes models' interruption-handling abilities, especially in following correction requests. Finally, we construct a train set OVI-Train for interruption-aware fine-tuning. Models fine-tuned on this dataset achieve significant gains on OVIBench, validating the effectiveness of our benchmark and data design. OVIBench, OVI-Train, and the evaluation code will be released.

## Metadata
- **Published**: 2026-08-23T08:12:08Z
- **Authors**: Naiming Liu, Zhiheng Wu, Shuning Wang, Tie Zhang, Bowen Liu, Tong Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22279v1)