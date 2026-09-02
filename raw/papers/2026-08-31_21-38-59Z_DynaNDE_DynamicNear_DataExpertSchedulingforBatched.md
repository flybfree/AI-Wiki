---
title: DynaNDE: Dynamic Near-Data Expert Scheduling for Batched MoE Inference
published: 2026-08-31T21:38:59Z
authors: Xiaoyang Lu, Belthangady Akash Vi Narayana Pai, Xian-He Sun
url: http://arxiv.org/abs/2609.00407v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DynaNDE: Dynamic Near-Data Expert Scheduling for Batched MoE Inference

## Abstract
Mixture-of-Experts (MoE) models enable efficient scaling of large language model (LLM) inference but suffer from substantial data-movement overhead when deployed on neural processing unit (NPU)-based systems. Near-Data Processing (NDP) provides a promising way to mitigate this bottleneck via cooperative NPU-NDP execution. However, existing NPU-NDP MoE systems do not fully account for hardware heterogeneity, dynamic expert-level concurrency, and temporal expert reuse during batched inference. This paper presents DynaNDE, a dynamic near-data expert scheduling framework that exploits NPU-NDP collaboration to accelerate batched MoE inference. DynaNDE introduces an analytical performance model that captures hardware heterogeneity, data-movement costs, and communication-computation overlap in cooperative NPU-NDP execution. Guided by this model, DynaNDE determines per-layer expert scheduling across the NPU and NDP while accounting for expert-level concurrency. DynaNDE also incorporates a reuse-aware runtime that avoids redundant parameter movement when experts reside in NPU memory. Experimental results show that DynaNDE achieves substantial throughput improvements over the state-of-the-art NPU-NDP MoE serving framework, with average speedups of 2.6$\times$ and 2.2$\times$ for the prefill and decoding stages, respectively.

## Metadata
- **Published**: 2026-08-31T21:38:59Z
- **Authors**: Xiaoyang Lu, Belthangady Akash Vi Narayana Pai, Xian-He Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00407v1)