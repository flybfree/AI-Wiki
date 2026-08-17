---
title: When Denoising Hurts: Rethinking the Terminal Step of Diffusion Time Series Forecasters -- Extended Version
published: 2026-08-14T08:25:01Z
authors: Dat Nguyen-Cong, Luong Tran, Tung Kieu
url: http://arxiv.org/abs/2608.14067v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Denoising Hurts: Rethinking the Terminal Step of Diffusion Time Series Forecasters -- Extended Version

## Abstract
Diffusion models offer a natural way to model uncertainty in time series forecasting, yet their iterative sampling process is often treated as a uniformly beneficial refinement procedure. Our study challenges this view by examining how forecast quality evolves throughout reverse diffusion. We find that general temporal structure is often recovered at relatively high noise levels, whereas continued low-noise refinement can introduce statistical drift and degrade the final forecast. Our analysis further suggests that this behavior explains why prior methods often favor relatively narrow diffusion architecture and schedule design. Building on this observation, we propose a label-free global stopping criterion that detects the optimal termination point, eventually speeding up inference and improving predictive accuracy. Additionally, since early stopping terminates inference in high-noise regions, we propose a Bernoulli timestep sampler that concentrates training on this region while preserving coverage of the full diffusion process. Extensive experiments conducted across eight real-world datasets demonstrate the superior performance of our method compared to existing approaches.

## Metadata
- **Published**: 2026-08-14T08:25:01Z
- **Authors**: Dat Nguyen-Cong, Luong Tran, Tung Kieu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14067v1)