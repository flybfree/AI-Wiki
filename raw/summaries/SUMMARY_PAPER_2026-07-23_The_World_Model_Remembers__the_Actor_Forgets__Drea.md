---
title: The World Model Remembers, the Actor Forgets: Dream Rehearsal for Continual Model-Based RL
url: http://arxiv.org/abs/2607.19749v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_04-46-49Z_TheWorldModelRemembers_theActorForgets_DreamRehear.md
generated_at: 2026-07-23 22:59
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why model‑based reinforcement‑learning agents forget tasks even when an unbounded replay buffer stores all experiences. It finds that the world model retains most information while the actor collapses, attributing forgetting to a channel issue rather than memory loss. Dream rehearsal with graded dreams restores performance across multiple task chains.

## Key Takeaways
- The world model preserves reward discrimination, value estimates and termination structure after training on many tasks, indicating it does not forget.
- The actor’s behavior collapses despite the replay buffer holding all past experiences, showing forgetting is a channel problem.
- Interleaved graded dream rehearsal enables task‑label‑free continual learning, achieving full retention across four‑task chains where plain replay fails.

## Context
Continual reinforcement learning often assumes agents can retain knowledge indefinitely when replay buffers are unlimited. This paper challenges that assumption by measuring component‑level forgetting in a well‑controlled experiment and demonstrates that the actor’s memory is not the bottleneck but its communication channel to the world model is. The findings extend the debate on whether continual learners need explicit memory mechanisms or can rely solely on replay.

## Implications
Practitioners of continual RL can design agents that continuously improve without costly environment interaction by using graded dream rehearsal, reducing reliance on large replay buffers. This approach could lower computational costs and enable deployment in dynamic environments where real‑world data is scarce.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19749v1)
