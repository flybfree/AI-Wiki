---
title: Locked at the Entrance, Open Inside: Where RLVR Narrows the Solution Space
url: http://arxiv.org/abs/2608.29188v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-29_10-46-57Z_LockedattheEntrance_OpenInside_WhereRLVRNarrowsthe.md
generated_at: 2026-08-31 20:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why reinforcement learning with verifiable rewards narrows the solution space in reasoning tasks, showing that breadth loss occurs early in a trajectory. It finds that alternative solutions remain executable but are not initiated because the policy fails to explore different entrance families. The intervention of late-layer parameter interpolation restores coverage significantly.

## Key Takeaways
- Solution coverage drops up to 67% across PPO and GRPO, halving problems solved at all checkpoints, indicating a severe contraction near the start of reasoning.
- Per-token likelihood shifts are 11x–16x larger before the first arithmetic operation than later, showing entrance-level information loss dominates over execution failure.
- Supplying only an unselected entrance prefix restores completion rates in low-access families by more than an order of magnitude, proving alternative solutions exist but are not initiated.

## Context
In AI research, scaling performance often relies on expanding solution space to handle diverse inputs. This work reveals that early-stage optimization can inadvertently prune viable reasoning branches, limiting the benefits of test-time scaling and prompting strategies.

## Implications
For practitioners, targeting interventions at the entrance rather than downstream layers could preserve diversity without sacrificing pass@1 accuracy. Early-step entropy collapse is not inevitable; alternative pipelines like SFT–DPO–RLVR maintain breadth, offering a path to broader reasoning capabilities.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29188v1)
