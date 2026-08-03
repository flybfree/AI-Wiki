---
title: Versatile On-device Adaptation at the Edge by Unifying Few-shot, Zero-shot, Continual, and In-context Learning
published: 2026-07-31T12:37:48Z
authors: Douwe den Blanken, Martin Lefebvre, Charlotte Frenkel
url: http://arxiv.org/abs/2607.29353v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Versatile On-device Adaptation at the Edge by Unifying Few-shot, Zero-shot, Continual, and In-context Learning

## Abstract
With the ever-increasing pervasiveness of smart edge devices, the demand is growing for applications that can be tailored to users (e.g., custom keyword spotting) or patients (e.g., adaptive health monitoring). Yet, most edge devices rely on fixed inference algorithms and thus cannot learn on-device to personalize predictions. When they can, devices typically support only a specific learning scenario, such as few-shot learning (FSL): going beyond this requires resorting either to another specialized device or to cloud-based retraining, which implies significant energy and latency overheads, a lack of real-time capabilities, and privacy concerns. In this work, we introduce embedder-centric learning (ECL), a framework that unifies four different online learning scenarios: FSL for on-the-fly customization, continual learning (CL) for knowledge accumulation, zero-shot learning (ZSL) for leveraging semantic data, and in-context learning (ICL) for adapting beyond classification. We demonstrate in silicon that ECL can be deployed on resource-constrained devices across four real-world use cases representative of the aforementioned learning scenarios. Our approach establishes a new state-of-the-art performance for FSL character recognition (Omniglot: 96.8% for 5-way 1-shot, 83.3% for 32-way 1-shot), and the first hardware baseline for CL in keyword spotting (NeuroBench keyword FSCIL: 71.8% for 200-way 5-shot). Moreover, we present the first hardware demonstrations of ZSL with semantic data (60.6% for 5-way spoken sentence classification) and ICL (46.2% at the 500th token of RegBench) operating at micro-to-milliwatt power budgets. Therefore, by unifying multiple learning scenarios, we pave the way for smart and versatile devices that can adapt right at the edge, without reliance on the cloud.

## Metadata
- **Published**: 2026-07-31T12:37:48Z
- **Authors**: Douwe den Blanken, Martin Lefebvre, Charlotte Frenkel
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29353v1)