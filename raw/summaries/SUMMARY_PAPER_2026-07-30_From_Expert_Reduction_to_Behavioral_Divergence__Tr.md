---
title: From Expert Reduction to Behavioral Divergence: Tracing Numerical State through Sparse MoE Inference
url: http://arxiv.org/abs/2607.28097v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_12-07-56Z_FromExpertReductiontoBehavioralDivergence_TracingN.md
generated_at: 2026-07-30 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how mathematically equivalent expert‑reduction orders can lead to different outcomes in sparse MoE inference by freezing local state and varying aggregation semantics. Experiments on DeepSeek‑V4‑Flash reveal that operand representation, accumulator precision, and reduction order affect continuation basins, token boundaries, and downstream predictions across 192 persistent trajectories.

## Key Takeaways
- At layer‑5 forks, A‑mode orders produce 10 continuation basins while B‑mode orders yield 360 exact structural classes and 11 basins, showing that reduction order changes the state space.  
- The C scheme preserves native MoE routes, token sequences, and texts, indicating that some reductions are invariant under evaluation of six‑term states.  
- Post‑hierarchical‑caching (post‑mHC) is identified as an intra‑token boundary, while full persistent state spans across tokens; identical tokens do not guarantee identical autoregressive state.

## Context
The findings highlight a subtle numerical compatibility issue in MoE runtimes that can affect model behavior without altering the underlying architecture. Understanding these effects is crucial for reliable scaling of large language models and for debugging intermittent performance drops.

## Implications
For practitioners, the paper stresses that expert operand conversion and accumulator precision must be treated as part of a contract between software and hardware. This awareness can prevent unexpected divergences in inference pipelines, especially when deploying MoE models across different backends or scheduling strategies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28097v1)
