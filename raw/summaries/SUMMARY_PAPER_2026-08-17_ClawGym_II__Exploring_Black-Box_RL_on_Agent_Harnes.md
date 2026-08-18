---
title: ClawGym II: Exploring Black-Box RL on Agent Harness
url: http://arxiv.org/abs/2608.16798v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_16-53-03Z_ClawGymII_ExploringBlack_BoxRLonAgentHarness.md
generated_at: 2026-08-17 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a unified black‑box reinforcement learning framework that enables stable and scalable optimization of general agents when interacting with complex harnesses. By building a sandbox‑based execution infrastructure, the authors isolate environments and harnesses within temporary sandboxes for large‑scale concurrent rollouts. The framework improves Pass@1 on ClawGym‑Bench by 9.98 points using OpenClaw and 14.81 points with Claude Code while remaining stable over 200–400 optimization steps.

## Key Takeaways
- A sandbox‑based execution infrastructure isolates task environments and harnesses within temporary sandboxes, allowing large‑scale concurrent rollouts without interference.
- Policy optimization is decoupled from opaque harness execution by placing a serving proxy at the model boundary that captures all model calls.
- Mix‑harness training lets a single model be jointly optimized by heterogeneous harnesses, enabling consistent performance across different execution systems.

## Context
Long‑horizon reinforcement learning with opaque harnesses remains a bottleneck because training scales poorly and stability degrades as optimization proceeds. This work addresses that bottleneck by providing a unified, black‑box approach that maintains consistency throughout the optimization process.

## Implications
For practitioners, the framework means they can train a single model across multiple execution systems without customizing each harness, accelerating development and reducing engineering overhead.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16798v1)
