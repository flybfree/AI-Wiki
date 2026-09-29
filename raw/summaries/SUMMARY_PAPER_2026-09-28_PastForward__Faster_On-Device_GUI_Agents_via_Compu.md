---
title: PastForward: Faster On-Device GUI Agents via Computational Experience Reuse
url: http://arxiv.org/abs/2609.32166v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-26_02-41-56Z_PastForward_FasterOn_DeviceGUIAgentsviaComputation.md
generated_at: 2026-09-28 20:40
model: qwen3.6-35b-a3b
---

## Summary
PastForward introduces a novel approach to accelerate on-device GUI agents by leveraging fine-grained reuse of computational experience gathered during routine task execution, addressing the high inference costs that hinder edge deployment. The system employs device-adaptive multi-token proposals verified in a single forward pass and pipelines next-step inference using prior GUI transitions while retaining valid computations across action steps. Evaluations on AndroidWorld workloads demonstrate that PastForward achieves latency speedups of 1.63 to 2.36 times on edge devices without compromising task success rates.

## Key Takeaways
- PastForward retrieves prior output sequences as device-adaptive multi-token proposals during decoding and verifies them via a single VLM forward pass, enabling efficient reuse of validated computational experience accumulated from ordinary task execution rather than relying on coarse-grained knowledge or full re-inference at every step.
- The system pipelines inference by initiating next-step computations using prior GUI transitions while the current action executes, selectively retaining early computation only when predicted screens match observed screens and carrying forward reusable KV states to minimize redundant processing across dynamic mobile environments.
- Benchmarked against AndroidWorld workloads derived from real mobile usage patterns across multiple VLM backbones on server and edge platforms, PastForward delivers significant on-device latency reductions ranging from 1.63x to 2.36x while preserving task success rates compared to existing baseline approaches.

## Context
As artificial intelligence moves toward edge computing for privacy-preserving applications like on-device

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.32166v1)
