---
title: Proof-or-Stop: Don't Trust the Agent, Trust the Evidence -- Loop Engineering for Verifiable Evidence-Gated Lifecycle Control
url: http://arxiv.org/abs/2607.14890v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-16_12-06-21Z_Proof_or_Stop_Don_tTrusttheAgent_TrusttheEvidence_.md
generated_at: 2026-07-23 23:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Proof-or-Stop Lifecycle Control, a method that gates autonomous agent transitions only when fresh, tracked‑source‑state‑bound, mechanically verifiable evidence is produced. It achieved zero false‑DONE transitions in 10 scenarios and cut visible‑pass/hidden‑fail amplification by 1.6 percentage points in an ablation study. The approach is presented as model‑agnostic and host‑neutral.

## Key Takeaways
- Proof-or-Stop treats agent outputs as claims that must be backed by fresh, tracked-source-state-bound, mechanically verifiable evidence before any lifecycle transition can occur.
- In a 9240‑cell ablation the gated loop reduced visible‑pass/hidden‑fail amplification from 31 to 2 cells (1.6 ppt improvement) compared with a naive loop.
- The self‑application corpus resolved 94.8 % of stories and found one high/critical cross‑vendor exhibit, showing robust evidence handling.

## Context
Autonomous coding agents perform multi‑step tasks but lack reliable lifecycle management; without verification claims can be falsified leading to unsafe merges. This work offers a framework that ties trust decisions directly to observable evidence rather than subjective correctness.

## Implications
By enforcing evidence‑gated reviews as mandatory gates, teams can prevent hidden failures from propagating through codebases and reduce the risk of false completions in large AI‑driven pipelines. The approach scales across model families and deployment environments, encouraging broader adoption of verifiable lifecycle controls.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.14890v1)
