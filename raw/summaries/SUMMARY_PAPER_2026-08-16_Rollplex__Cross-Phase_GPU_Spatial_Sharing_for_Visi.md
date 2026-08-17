---
title: Rollplex: Cross-Phase GPU Spatial Sharing for Vision Language Model Post-Training
url: http://arxiv.org/abs/2608.14498v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_17-13-34Z_Rollplex_Cross_PhaseGPUSpatialSharingforVisionLang.md
generated_at: 2026-08-16 20:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
Rollplex is a runtime that reorganizes the phases of reinforcement learning for vision-language models to overlap prefix processing with rollout decoding. This reduces GPU memory pressure and improves compute utilization while keeping on-policy semantics intact. The method achieves 1.23×–1.30× speedup over serial colocation and up to 2.24× speedup over disaggregated setups.

## Key Takeaways
- Phase‑aware memory management lets HBM be used for both prefix tensors and rollout activations, cutting peak GPU usage from ~165 GiB to a more balanced load.
- Parallelism‑aware weight sharing reuses the same physical storage across tensor‑parallel degrees without copying the full actor model each time.
- The approach preserves synchronous on‑policy updates while delivering large speedups under identical GPU budgets.

## Context
Vision‑language models face massive compute demands from video and prompt prefixes, which dominate training time. Current RL pipelines treat these phases sequentially, leaving idle GPU resources. Rollplex’s phase‑level scheduling addresses this bottleneck by aligning independent computation windows.

## Implications
For practitioners deploying VLMs at scale, Rollplex offers a practical way to squeeze more performance out of existing hardware without redesigning the model. It can lower cost and power consumption while maintaining high‑fidelity RL training, accelerating research iteration cycles.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14498v1)
