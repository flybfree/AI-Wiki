---
title: When Does Trace-Driven Evaluation Mislead MoE Expert Caching? Replay Semantics, Workload Contamination, and Operating Regimes
published: 2026-08-08T04:29:20Z
authors: Yu Zhang
url: http://arxiv.org/abs/2608.07911v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Does Trace-Driven Evaluation Mislead MoE Expert Caching? Replay Semantics, Workload Contamination, and Operating Regimes

## Abstract
Mixture-of-Experts (MoE) models have outgrown accelerator memory, and offloading expert weights to host memory is now standard. This makes expert cache management an attractive lever: a policy that raised the hit rate would cut expert traffic per token. Evaluating that is a measurement problem, and we find the measurement fragile.   With a trace-driven, event-atomic simulator over three MoE models (40, 64, 128 experts), we isolate three evaluation axes that change conclusions, not just numbers. Replay semantics: under a fused-event traffic contract, an inconsistent per-access replay inflates recency-based policies by 27-29% while leaving frequency-based and static ones within 4%, inverting the policy ranking. Workload contamination: probe sets using one instruction template per category produce verbatim-identical generation prefixes; a matched-pair rendering intervention moves the measured early-window effect by 19.4-31.9 points and reverses which workloads look most cache-friendly. Operating regimes: normalized miss fractions do not transfer across models, so the per-step expert union relative to per-layer capacity must be reported -- yet permuting only the temporal order of an identical event stream moves the offline-optimal gap from 44.9% to 30.8%, so it is not sufficient.   Corrected, a stable gap to the offline optimum remains (44.2-45.9% over 13 frozen workload compositions). A forced-admission oracle attributes 84.3-96.6% of it to knowing which resident expert is used furthest in the future. A causal next-use predictor, used as an eviction rule, recovers -11.4% of the gap; it picks an optimal victim 3.4% of the time, against 2.4% for a random resident block and 20.6-22.1% for LRU and LFRU. Our position is narrow: in our evaluated settings a large offline-optimal gap substantially overstates the gains recovered by representative lightweight causal mechanisms.

## Metadata
- **Published**: 2026-08-08T04:29:20Z
- **Authors**: Yu Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07911v1)