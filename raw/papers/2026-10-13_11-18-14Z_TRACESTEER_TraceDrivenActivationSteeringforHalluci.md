---
title: TRACESTEER: Trace Driven Activation Steering for Hallucination Mitigation in Diffusion Language Models
published: 2026-10-13T11:18:14Z
authors: Xin Zhang, Yili Wang, Yue Tan, Xin He, Rui Miao, Yixin Liu, Yi Chang, Xin Wang
url: http://arxiv.org/abs/2610.18173v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TRACESTEER: Trace Driven Activation Steering for Hallucination Mitigation in Diffusion Language Models

## Abstract
Diffusion large language models (dLLMs) have emerged as a promising alternative to autoregressive LLMs, yet remain susceptible to hallucination. Activation steering offers a promising mitigation approach by guiding parallel token predictions through internal representations. However, existing steering methods largely overlook two characteristics of dLLMs: dynamic denoising states and temporal hallucination risks, which challenge predefined steering vectors and uniform intervention strengths. We propose TRACESTEER, a trace-driven activation steering framework that uses preceding denoising predictions as feedback to jointly adapt steering direction and strength. Specifically, Denoising Feedback Steering (DF-Steering) constructs step-specific steering vectors from preceding predictions and current hidden states. Trajectory-Guided Steering Gate (TS-Gate) regulates their strength using prediction uncertainty and the denoising timestep. With the backbone frozen, factual supervision and magnitude regularization jointly guide the learning of adaptive steering interventions, promoting factual reliability and stability throughout denoising. Experiments on two dLLMs show improved factual reliability on TruthfulQA and generalization across five downstream benchmarks.

## Metadata
- **Published**: 2026-10-13T11:18:14Z
- **Authors**: Xin Zhang, Yili Wang, Yue Tan, Xin He, Rui Miao, Yixin Liu, Yi Chang, Xin Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.18173v1)