---
title: EASy: Towards Efficient LLM-Based Agentic System
url: http://arxiv.org/abs/2608.04588v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_08-50-36Z_EASy_TowardsEfficientLLM_BasedAgenticSystem.md
generated_at: 2026-08-05 20:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces EASy, a trainable orchestrator that balances task success with computational efficiency in LLM-based agentic systems. Experiments show it outperforms baselines on math reasoning and deep research tasks by achieving better performance‑efficiency trade‑offs.

## Key Takeaways
- The orchestrator learns explicit capability and cost profiles of heterogeneous executors, enabling context‑sensitive routing beyond simple performance optimization.
- It uses a milestone‑plan‑act workflow that builds dependency‑aware execution graphs and parallelizes independent steps while adapting to intermediate outcomes.
- A tree‑structured rollout with multi‑component rewards explores alternative decompositions and plans, optimizing both task correctness and efficiency.

## Context
Agentic AI systems aim to coordinate specialized language models for complex tasks, yet prior approaches focus mainly on success rates without accounting for real‑world resource constraints. This work addresses the gap by integrating efficiency into the learning objective, aligning with trends toward scalable, cost‑aware AI agents.

## Implications
For industry practitioners, EASy demonstrates a practical path to deployable agentic solutions that respect budget and hardware limits. Researchers can leverage its framework to design more robust, resource‑efficient LLM orchestrations in production environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04588v1)
