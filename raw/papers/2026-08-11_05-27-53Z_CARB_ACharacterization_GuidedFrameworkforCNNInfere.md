---
title: CARB: A Characterization-Guided Framework for CNN Inference Cost Prediction and Deployment Screening
published: 2026-08-11T05:27:53Z
authors: Linh Nguyen, Zhixin Pan
url: http://arxiv.org/abs/2608.10506v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CARB: A Characterization-Guided Framework for CNN Inference Cost Prediction and Deployment Screening

## Abstract
Accurate pre-deployment estimation of CNN inference cost--energy, latency, and peak memory--is increasingly critical as models are deployed on resource-constrained GPU platforms. Existing approaches rely on FLOPs, latency measurements, or single-device profiling as energy proxies, overlooking the non-linear interactions between architectural design and hardware load. We present a workload characterization study of 13 419 CNN configurations on two GPU platforms (RTX 5090 and RTX 3080) under GPU telemetry, revealing that energy, latency, and memory exhibit fundamentally distinct scaling behaviors: energy and latency diverge by 3x under high computational demand, and cross-GPU transferability differs by target--energy and latency require platform-specific models while memory transfers well across the two tested platforms. Building on these characterization findings, we develop CARB, a cascade-blended ensemble that jointly predicts all three targets with R2 ~0.99, and a two-stage deployment screening workflow that eliminates over 90% of candidates in seconds, reducing large design spaces to a Pareto-prioritized shortlist validated against real hardware.

## Metadata
- **Published**: 2026-08-11T05:27:53Z
- **Authors**: Linh Nguyen, Zhixin Pan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10506v1)