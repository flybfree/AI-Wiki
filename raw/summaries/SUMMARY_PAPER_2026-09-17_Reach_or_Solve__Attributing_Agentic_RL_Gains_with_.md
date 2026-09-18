---
title: Reach or Solve? Attributing Agentic RL Gains with Checkpoint Handoffs
url: http://arxiv.org/abs/2609.19636v1
type: paper-summary
date: 2026-09-17
source_paper: 2026-09-17_03-27-53Z_ReachorSolve_AttributingAgenticRLGainswithCheckpoi.md
generated_at: 2026-09-17 21:23
model: freedomaisvr/gemma-4-12b-it
---

## Summary
The paper introduces "checkpoint handoff," a novel evaluation protocol designed to disentangle whether improvements in agentic Reinforcement Learning (RL) stem from better navigation (reaching a goal state) or superior problem-solving (completing the task once there). By cloning states reached by one checkpoint and handing them to another, the authors demonstrate that current evaluation methods often conflate these two components, which can lead to misleading interpretations of model progress in long-horizon environments.

## Key Takeaways
- The "checkpoint handoff" protocol allows for a clean comparison between different models or training regimes by cloning a state reached by one checkpoint and passing it to another without any retraining.
- The authors define two distinct metrics: REACH, which measures how often a policy arrives at a state that is a fixed number of actions from success, and SOLVE, which measures the frequency of completion from those identical cloned states.
- Experimental results across multiple benchmarks show that RL improves both REACH and SOLVE components; specifically, an RL history provides significantly more value to an RL solver than it does to an SFT (Supervised Fine-Tuning) solver when starting from a shared state.

## Context
As AI agents are increasingly deployed in complex, multi-step environments like ALFWorld, distinguishing between navigation skills and reasoning capabilities becomes essential for understanding model progress. This paper addresses the fact that because agent actions influence subsequent states, standard endpoint success metrics cannot isolate whether an agent is better at "getting there" or "doing something once it arrives."

## Implications
For researchers and practitioners, this framework provides a more nuanced way to interpret agent performance by isolating specific failure points in long-horizon tasks. By identifying whether a model fails due to poor navigation (REACH) or poor execution (SOLVE), developers can better target improvements in either the planning phase or the final action sequence of an AI system.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.19636v1)
