---
title: InFactPlanner: Planning Sustainable Geo-Distributed LLM Data Centers
published: 2026-08-13T07:57:22Z
authors: Nicoletta Tsiopani, Moysis Symeonides, George Pallis, Marios D. Dikaiakos
url: http://arxiv.org/abs/2608.12915v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# InFactPlanner: Planning Sustainable Geo-Distributed LLM Data Centers

## Abstract
The rapid growth of LLM inference is shifting sustainability concerns from one-time training to continuous serving, where infrastructure decisions shape energy use, carbon emissions, water consumption, and service quality. Yet operators often need to compare deployment alternatives before large-scale infrastructure is built, making direct measurement costly, slow, and sometimes infeasible. We present InFactPlanner, a trace-driven decision-support framework for what-if analysis of sustainable AI data center deployment for LLM inference across single and geo-distributed sites. InFactPlanner combines query traces, hardware-model profiles, candidate site configurations, PUE/WUE parameters, renewable generation models, and time-varying grid carbon intensity to estimate power, energy, carbon emissions, water use, latency, and server utilization. The framework abstracts low-level serving effects into configurable hardware-model profiles, enabling rapid comparison of site selection, capacity placement, hardware, model, renewable integration, and routing choices. We validate the energy accounting pipeline by reproducing reference LLM inference energy estimates with less than 10% deviation, evaluate scalability across multiple data centers and server counts, and demonstrate scenario-driven decision analyses for hardware selection, renewable placement, geographic deployment, and carbon-aware routing. Our results show that sustainability-optimal choices can differ from latency-optimal ones, and that the carbon value of deployment depends strongly on the local grid mix.

## Metadata
- **Published**: 2026-08-13T07:57:22Z
- **Authors**: Nicoletta Tsiopani, Moysis Symeonides, George Pallis, Marios D. Dikaiakos
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12915v1)