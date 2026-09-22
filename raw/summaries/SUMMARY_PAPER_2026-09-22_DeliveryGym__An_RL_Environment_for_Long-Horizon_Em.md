---
title: DeliveryGym: An RL Environment for Long-Horizon Embodied Agent Planning with Adaptive Curriculum
url: http://arxiv.org/abs/2609.19801v1
type: paper-summary
date: 2026-09-22
source_paper: 2026-09-17_07-13-55Z_DeliveryGym_AnRLEnvironmentforLong_HorizonEmbodied.md
generated_at: 2026-09-22 00:10
model: freedomaisvr/gemma-4-12b-it
---

## Summary
The paper introduces DeliveryGym, a 3D environment specifically designed to train and evaluate embodied agents on complex, long-horizon courier tasks where resources like time, energy, and money are finite. By providing a framework that computes rewards based on complete trajectory outcomes rather than isolated task success, the authors demonstrate how reinforcement learning can improve an agent's ability to sequence work and manage costs effectively over a full shift.

## Key Takeaways
- DeliveryGym incorporates persistent world dynamics where actions have cumulative consequences; for example, completing one delivery might consume energy or money required for future tasks, forcing agents to learn long-term resource management rather than just immediate task completion.
- The environment utilizes a unique reward structure that computes rewards from simulator events across an entire trajectory, allowing agents to learn the trade-offs between immediate success and overall shift efficiency under coupled constraints.
- An adaptive curriculum mechanism was developed to tailor training by focusing on the agent's observed weaknesses while maintaining a fixed evaluation suite; this approach improved test income by 16.5% over uniform sampling methods at the same rollout budget, proving that targeted practice is crucial for complex planning.

## Context
This research addresses a critical gap in current embodied AI: the ability of agents to plan across long horizons where immediate success does not guarantee overall goal completion due to resource depletion. It moves beyond simple navigation by incorporating economic and logistical constraints that are vital for real-world applications like autonomous logistics, warehouse management, and automated delivery services.

## Implications
For the AI research community, this work provides a standardized benchmark for evaluating how agents manage complex dependencies and multi-step planning in dynamic environments. For practitioners, it highlights the importance of curriculum learning and trajectory-based rewards over simple task completion metrics to build truly autonomous systems capable of operating efficiently in resource-constrained, real-world environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.19801v1)
