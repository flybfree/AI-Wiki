---
title: PastForward: Faster On-Device GUI Agents via Computational Experience Reuse
published: 2026-09-26T02:41:56Z
authors: Taehwan Park, Changmin Lee, Hayeon Lee, Taesik Gong
url: http://arxiv.org/abs/2609.32166v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PastForward: Faster On-Device GUI Agents via Computational Experience Reuse

## Abstract
Running GUI agents on edge devices can keep sensitive screens and interaction histories local, but the computational cost of inference at every action step makes deployment challenging. Existing GUI agent systems either perform full vision-language model (VLM) inference at each action step or reuse coarse-grained knowledge matched to prior tasks. However, dynamic mobile environments and user tasks make it difficult to fully utilize prior task executions without additional fine-tuning or task-specific offline exploration. To address this challenge, we present PastForward, a system that accelerates GUI agents through validated, fine-grained reuse of computational experience accumulated during ordinary task execution. During decoding, PastForward retrieves prior output sequences as device-adaptive multi-token proposals and verifies them in a single VLM forward pass. Across action steps, it uses prior GUI transitions to begin next-step inference while the device executes the current action, retains the early computation only when the predicted screen matches the observed screen, and carries reusable KV states forward. We evaluate PastForward on AndroidWorld workloads derived from real mobile usage patterns using multiple VLM backbones across server and edge platforms. On device, PastForward achieves action-step latency speedups of 1.63-2.36$\times$ while maintaining task success rates.

## Metadata
- **Published**: 2026-09-26T02:41:56Z
- **Authors**: Taehwan Park, Changmin Lee, Hayeon Lee, Taesik Gong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32166v1)