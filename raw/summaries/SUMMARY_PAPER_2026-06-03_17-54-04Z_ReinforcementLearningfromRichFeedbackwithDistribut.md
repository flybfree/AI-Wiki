---
title: Reinforcement Learning from Rich Feedback with Distributional DAgger
url: http://arxiv.org/abs/2606.05152v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-03_17-54-04Z_ReinforcementLearningfromRichFeedbackwithDistribut.md
generated_at: 2026-06-11 10:52
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes DistIL, a distributional version of the DAgger algorithm that leverages rich feedback such as execution traces and expert corrections to improve reinforcement learning. The authors demonstrate that their forward cross‑entropy objective yields monotonic policy improvement with regret guarantees, outperforming prior self‑distillation methods across scientific reasoning, coding, and mathematical problem solving.

## Key Takeaways
- The forward cross‑entropy loss captures the full distribution of expert feedback, enabling credit assignment to earlier decisions rather than just final outcomes.  
- Prior RL approaches using reverse KL or Jensen‑Shannon may increase probability on worse actions even when the expert has a higher reward, breaking monotonic improvement.  
- DistIL optimizes a teacher‑weighted likelihood lower bound and achieves better Pass@N scores than RLVR and self‑distillation baselines.

## Context
The field of reinforcement learning from verifiable rewards is limited by single‑bit feedback, which cannot capture the detailed information available in execution traces. This work addresses that gap by integrating richer data streams into a standard imitation‑learning framework, highlighting the potential for more expressive training signals.

## Implications
DistIL offers practitioners a practical path to higher accuracy without requiring full access to expert trajectories, making it applicable across domains where feedback is abundant but costly to collect. The monotonic improvement guarantee provides confidence that policy updates will not regress, encouraging wider adoption in safety‑critical AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.05152v1)
