---
title: AGM: Achievement-Grounded Memory for Closed-Loop Agents with Frozen VLA Policies
url: http://arxiv.org/abs/2608.29537v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-30_03-50-49Z_AGM_Achievement_GroundedMemoryforClosed_LoopAgents.md
generated_at: 2026-08-31 20:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Achievement-Grounded Memory (AGM), a lightweight closed‑loop framework for frozen vision‑language‑action policies that turns open‑loop execution into a disciplined loop of execution, verification and progress tracking. By using proprioceptive cues and a single 2.43 million‑parameter verification head, AGM updates task memory only after physical evidence confirms subgoal completion, thereby eliminating persistent state errors.

## Key Takeaways
- The framework represents tasks as sequences of subgoals with a progress pointer that is advanced only when the current subgoal is verified by physical evidence.  
- Verification relies on proprioceptive interaction cues and language‑conditioned cross‑view comparison performed by a frozen foundation model’s verification head, avoiding test‑time large‑model inference.  
- On RoboMME Counting, AGM improves PickXTimes and BinFill compared to the strongest memory‑augmented baseline, delivering consistent gains on both simulated and physical robots.

## Context
Closed‑loop reasoning is essential for reliable embodied agents that must decide when to continue, retry or stop. Existing memory‑augmentation methods often treat actions as completed progress, which can corrupt task state. AGM addresses this by grounding updates in concrete verification, aligning with the need for scalable, low‑cost closed loops.

## Implications
AGM shows that disciplined state updates matter more than raw memory capacity, offering a practical path to improve performance of frozen VLA agents without heavy inference costs. This approach can be adopted across robotics and AI systems requiring reliable task completion tracking.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29537v1)
