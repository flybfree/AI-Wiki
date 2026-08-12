---
title: Share First, Route What Remains: A Unified Framework for Token-Adaptive MoE Computation
url: http://arxiv.org/abs/2608.10392v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_02-40-58Z_ShareFirst_RouteWhatRemains_AUnifiedFrameworkforTo.md
generated_at: 2026-08-11 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
Mixture-of-experts (MoE) models have moved beyond fixed expert routing to shared‑expert designs and dynamic adapters that vary computation per token. This paper introduces UniF-MoE, a unified framework that treats sharing and routing as interdependent processes. By decomposing experts into key‑value channels and applying the share‑first principle, it reduces residual expert demand while improving performance on benchmark tasks. The results demonstrate that the unified design outperforms both static and dynamic MoE baselines while cutting activation count and inference time.

## Key Takeaways
- Extracting reusable computation via aligned value positions changes both the remaining tasks and the capacity needed by other experts.
- Greater shared coverage leads to lower residual expert demand because many tokens are processed together in shared blocks.
- The framework uses a shared‑demand score, key prototypes, and cumulative routing mass to allocate block counts and pathway weights.

## Context
Mixture-of-experts models have evolved from static routing to dynamic adapters that adjust the number of active experts per token. However, most designs treat sharing and routing as independent decisions, which can cause inefficiencies in computation and memory usage. As models grow, efficient routing becomes critical for deployment on limited hardware.

## Implications
This unified approach offers a principled way to balance knowledge reuse with computational efficiency, potentially lowering latency and hardware demands for large language models. Practitioners can adopt UniF-MoE to build more scalable inference pipelines without sacrificing accuracy.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10392v1)
