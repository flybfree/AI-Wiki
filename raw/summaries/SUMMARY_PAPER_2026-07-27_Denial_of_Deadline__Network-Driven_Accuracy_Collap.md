---
title: Denial of Deadline: Network-Driven Accuracy Collapse in Distributed Inference Pipelines
url: http://arxiv.org/abs/2607.24692v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_17-34-09Z_DenialofDeadline_Network_DrivenAccuracyCollapseinD.md
generated_at: 2026-07-27 23:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a new attack called shaped workload attacks that exploit contention on shared resources in distributed inference pipelines. It shows that benign users' slow‑path predictions can be delayed beyond their deadline, causing the merger to discard them and leading to accuracy collapse. In an autonomous driving multi‑object tracking simulation, burst requests increase p99 latency from 92 ms to 2 s, eliminating cloud benefits and dropping HOTA by about 7 points.

## Key Takeaways
- Shaped workload attacks such as Yo‑Yo bursts can push slow‑path predictions past their latency deadlines without accessing model weights or victim data.  
- The merger discards delayed predictions, resulting in a loss of the accuracy benefit from the cloud path and a measurable drop in tracking quality.  
- Accuracy degradation varies widely (2–18.7 HOTA points) depending on targeted video intervals, with rare classes like stop signs losing nearly half their pre‑attack accuracy.

## Context
Distributed inference pipelines combine fast local predictions with high‑accuracy cloud computation to meet latency constraints. This architecture is common in edge‑cloud applications where reliability and quality are both critical. The paper highlights a previously unexploited vulnerability in the coordination layer that could undermine system performance.

## Implications
For practitioners, defenses must address routing, scheduling, and resource isolation to prevent latency‑driven accuracy loss. For researchers, this work opens avenues for studying adversarial workloads against emerging AI inference architectures.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24692v1)
