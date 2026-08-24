---
title: TreeWY: Speculative Verification for Gated DeltaNet Hybrids
url: http://arxiv.org/abs/2608.20961v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_10-31-15Z_TreeWY_SpeculativeVerificationforGatedDeltaNetHybr.md
generated_at: 2026-08-23 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces TreeWY, a speculative verification method for gated delta net hybrids that avoids storing full recurrent states per draft node. By replacing state snapshots with a triangular solve and a small pseudo-value matrix, the approach reduces memory usage while preserving correctness. Experiments on Qwen3.5 models show lower memory pressure and faster TTFT without sacrificing acceptance length.

## Key Takeaways
- TreeWY eliminates per-node recurrent state snapshots in gated delta nets, replacing them with a triangular solve that computes each draft node's output from the gated delta rule alone.
- The method stores only a pseudo-value matrix instead of full states, cutting memory and KV-cache pressure while maintaining identical acceptance length across scales.
- Wider draft trees become feasible because memory is freed, though throughput gains are modest.

## Context
Speculative decoding in large language models often suffers from high memory demands due to storing recurrent states at every draft position. Current solutions rely on costly snapshots that limit tree width and speed. This paper addresses the bottleneck by rethinking verification without state storage, aligning with trends toward efficient hybrid architectures.

## Implications
Practitioners can implement TreeWY to deploy wider speculative decoding trees within current hardware limits, improving TTFT especially when memory is binding. The approach offers a lightweight alternative that does not require architectural changes beyond the gated delta rule, encouraging more aggressive tree expansion in future models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20961v1)
