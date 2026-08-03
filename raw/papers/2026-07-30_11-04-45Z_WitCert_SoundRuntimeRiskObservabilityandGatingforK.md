---
title: WitCert: Sound Runtime Risk Observability and Gating for KV-Cache Quantization
published: 2026-07-30T11:04:45Z
authors: Fanzhe Wei, Li Liu
url: http://arxiv.org/abs/2607.28699v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# WitCert: Sound Runtime Risk Observability and Gating for KV-Cache Quantization

## Abstract
KV-cache quantization is validated today by offline benchmark averages; a deployed system cannot tell whether compression is damaging the request it is serving right now. We give it a provably sound runtime meter, a "DTrace for KV quantization": a per-(layer, head, step) upper bound on the total variation between exact and compressed attention. The meter has two tiers: a deterministic band-norm-witness bound, sound for any cache-preserving black-box quantizer and for any query (adaptive-safe, worst-case Cauchy-Schwarz plus RoPE band-unitarity), and a tighter probabilistic certificate for a controlled subtractively-dithered INT8 quantizer under an explicit request-level failure budget (stated for non-adaptive queries; core theorems machine-checked in Lean 4). Three results. Observability: the meter enters SGLang through an environment-guarded patch, and any scheme registered as one tensor function is measured in live serving. Repair: meter-driven gating, risk-ranked where the witness is saturated and certified where it is informative, empirically restores the quality floor at benchmark scale. For example, raw-cast FP8 improves from 22.8 back to 79.7 on hard RULER tasks, with the difference from uncompressed bounded at [+0.0, +0.8] by a paired test. Analysis: aggressive schemes survive on cross-layer error cancellation, not per-step fidelity. In a 28-layer sweep, no single layer's pollution alone loses anything (0/28), and the certified INT8 cache serves 1.88 times more KV tokens at the same memory in SGLang.

## Metadata
- **Published**: 2026-07-30T11:04:45Z
- **Authors**: Fanzhe Wei, Li Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28699v1)