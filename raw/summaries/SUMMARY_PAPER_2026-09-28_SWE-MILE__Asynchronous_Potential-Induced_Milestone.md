---
title: SWE-MILE: Asynchronous Potential-Induced Milestone Credit Assignment for Long-Horizon Software Engineering Agents
url: http://arxiv.org/abs/2609.32631v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-26_13-49-14Z_SWE_MILE_AsynchronousPotential_InducedMilestoneCre.md
generated_at: 2026-09-28 20:50
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces SWE-MILE, a framework that addresses the credit assignment problem in long-horizon software engineering agents by deriving fine-grained process supervision directly from workflow runtime without relying on external evaluators or auxiliary reward models. By quantifying navigation and verification potentials, SWE-MILE attributes milestone progress and regressions to individual actions and propagates this credit backward through discounted propagation. Experiments demonstrate that augmenting terminal outcome advantages with these runtime-derived signals leads to substantial performance improvements in long-horizon SWE tasks.

## Key Takeaways
- SWE-MILE utilizes asynchronous potential-induced milestone credit assignment to quantify task-relevant file exposure as navigation potential and test-state alignment as verification potential; differences in these potentials allow the system to attribute progress or functional regressions to specific agent actions without auxiliary models.
- To minimize latency, the framework employs asynchronous shadow probing that replays repository-changing actions in an isolated sandbox and runs verification processes in parallel with the agent's primary interaction, effectively hiding verification overhead while acquiring intermediate states.
- The system implements discounted backward credit to propagate supervision from identified milestones to preceding steps, creating a rich learning signal that augments terminal outcome advantages and yields substantial improvements in agent performance on representative long-horizon software engineering benchmarks.

## Context
Reinforcement learning with verifiable rewards

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.32631v1)
