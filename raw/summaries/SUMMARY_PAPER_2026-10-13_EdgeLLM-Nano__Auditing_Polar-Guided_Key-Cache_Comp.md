---
title: EdgeLLM-Nano: Auditing Polar-Guided Key-Cache Compression and Consistency-Anchored Pruning on a 33.6 MB On-Device Language Model
url: http://arxiv.org/abs/2610.14475v1
type: paper-summary
date: 2026-10-13
source_paper: 2026-10-10_02-09-08Z_EdgeLLM_Nano_AuditingPolar_GuidedKey_CacheCompress.md
generated_at: 2026-10-13 21:45
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces EdgeLLM-Nano, a measurement study that evaluates KV-cache compression methods on a nano-scale 8.39M-parameter (33.6 MB) decoder-only transformer deployed on edge hardware, specifically a Raspberry Pi 5. The authors deliver a negative verdict on two popular compression techniques—polar-guided key-cache quantization and consistency-anchored progressive weight pruning—finding that simpler baselines perform comparably or better. They also propose Long-Context Decode Fidelity (LCDF), a token-by-token evaluation metric that reveals quality differences invisible to standard perplexity scoring.

## Key Takeaways
- Polar-guided key-cache quantization performs significantly worse than a simple round-to-nearest (RTN) control, with RTN causing an order of magnitude less damage to model quality. This challenges the assumption that sophisticated polar-guided quantization schemes offer meaningful advantages for KV-cache compression on resource-constrained devices.
- Consistency-anchored progressive weight pruning does not outperform one-shot magnitude-based pruning; the simpler approach performs as well as or better than the more complex progressive strategy, suggesting added complexity does not yield practical benefits in edge deployment scenarios.
- The authors introduce LCDF, a token-by-token teacher-forced log-loss evaluation that uses paired statistics across seeds and effect sizes to distinguish compression backends. Standard perplexity assigns an identical 5.461 score to all tested methods, masking critical quality differences. Only KIVI approaches lossless behavior under LCDF, while all tested compression backends proved less energy-efficient per token than uncompressed FP16 inference on a Raspberry Pi 5.

## Context
KV-cache compression has become a dominant strategy for scaling large language models to edge and mobile deployments, yet most published evaluations rely on perplexity on server-class hardware and do not actually exercise the compressed KV-cache during inference. This gap means practitioners deploying quantized caches on constrained devices may be operating under unvalidated quality assumptions. EdgeLLM-Nano fills this gap by constructing a deliberately tiny transformer testbed that permits exhaustive end-to-end measurement across backends, random seeds, and power samples, making it feasible to audit compression claims rigorously rather than relying on aggregate perplexity numbers.

## Implications
For practitioners deploying LLMs on edge devices, this work warns that KV-cache compression can simultaneously degrade output quality and increase per-token energy consumption compared to uncompressed FP16 inference, undermining the primary motivation for compression. The introduction of LCDF provides a practical, reproducible evaluation protocol that exposes quality regressions hidden by perplexity, enabling more honest benchmarking in the rapidly growing on-device AI ecosystem. Industry teams building edge inference stacks should re-examine their compression pipelines using token-level fidelity metrics rather than trusting aggregate perplexity scores, and should consider whether simpler quantization baselines like RTN or magnitude-based pruning offer better quality-energy trade-offs than more elaborate schemes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.14475v1)
