---
title: Reasoning Denoiser: Denoising Reasoning Traces for Hallucination Detection in Large Reasoning Models
published: 2026-07-24T08:48:17Z
authors: Junlin Fang, Do Nguyen-Thanh, Xiaogang Xu, Zhen Fang, Sean Du
url: http://arxiv.org/abs/2607.22098v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reasoning Denoiser: Denoising Reasoning Traces for Hallucination Detection in Large Reasoning Models

## Abstract
Large reasoning models (LRMs) generate long reasoning traces before producing final answers. While these traces may contain useful signals for hallucination detection, harnessing them is non-trivial because long trajectories often include noisy steps that obscure the cues relevant to truthfulness assessment. In this paper, we identify two prevalent forms of reasoning noises, i.e., irrelevant steps and repetitive steps, and show that both substantially degrade hallucination detection performance. Existing confidence-based scores and naive embedding-based filtering fail to reliably separate noisy from informative steps. To address this challenge, we propose REDE, a novel learning framework for denoising reasoning traces for hallucination detection. Specifically, REDE leverages final-answer attention as an automatic supervision signal to shape the step-level representation space, yielding refined embeddings in which noisy steps can be reliably identified and filtered. REDE can be readily plugged into diverse hallucination detectors by operating on the filtered reasoning trajectory after removing noisy steps. Extensive experiments on multiple reasoning benchmarks show that REDE consistently improves detection performance over competitive baselines.

## Metadata
- **Published**: 2026-07-24T08:48:17Z
- **Authors**: Junlin Fang, Do Nguyen-Thanh, Xiaogang Xu, Zhen Fang, Sean Du
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22098v1)