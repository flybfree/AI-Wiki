---
title: Recursive Experiential-Working Memory Evolution for Long-Horizon Agent Harnesses
url: http://arxiv.org/abs/2608.24876v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_17-56-35Z_RecursiveExperiential_WorkingMemoryEvolutionforLon.md
generated_at: 2026-08-25 21:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Recuris, a recursive Experiential-Working Memory architecture that helps long‑horizon agents maintain task state and select skills effectively. By coupling working memory with experiential memory, the system generates structured evidence that localizes failures and drives updates to skill memory. Across benchmarks and models, Recuris boosts success rates by up to 32 points on the longest tasks.

## Key Takeaways
- Working Memory tracks task progress and directs skill selection from Experiential Memory, preventing history‑obscured misalignment in long‑horizon tasks.
- Structured execution evidence localizes failures to specific memory components, enabling precise updates that reshape Skill Memory.
- The bounded recursive loop of meta‑agent feedback yields frontier model gains, such as +17.8 points on GPT‑5.6 Sol and +32.2 points on the longest tasks.

## Context
Long‑horizon reinforcement learning suffers from memory decay and skill misalignment, limiting progress toward recursive self‑improvement. This work addresses these issues with a novel memory architecture that can be integrated into existing agent frameworks without major redesign.

## Implications
Recuris demonstrates that recursively evolving memory is scalable for RSI, offering a practical path to higher performance in complex tasks. Practitioners can adopt this framework to improve long‑term planning and reduce catastrophic forgetting in deployed agents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24876v1)
