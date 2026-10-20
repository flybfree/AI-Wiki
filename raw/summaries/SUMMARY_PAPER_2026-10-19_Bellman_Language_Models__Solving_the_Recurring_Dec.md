---
title: Bellman Language Models: Solving the Recurring Decisions of LLM Agents
url: http://arxiv.org/abs/2610.24871v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-17_21-19-20Z_BellmanLanguageModels_SolvingtheRecurringDecisions.md
generated_at: 2026-10-19 20:36
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper proposes reframing LLM agent decision-making as a Markov Decision Process (MDP) optimization problem rather than re-deriving decisions from context on every turn. The authors introduce "Discretize, Then Decide," a method that reads agent conversations into discrete states, estimates outcome probabilities and move costs, solves the resulting MDP once, and then deploys the solved policy as a lightweight controller around the LLM. The approach, called a Bellman Language Model (BLM), dramatically reduces model calls and cost while improving task success rates on bounded agentic workflows.

## Key Takeaways
- The authors observe that in bounded agentic workflows, the LLM's decision space approaches saturation: agents repeatedly encounter the same states and stop encountering new ones after sufficient conversations. Despite this, LLMs typically re-derive decisions from their prompt context on every turn rather than treating them as a solved optimization problem, wasting compute and introducing inconsistency.
- The "Discretize, Then Decide" pipeline converts agent logs or self-generated runs into discrete states, estimates transition probabilities and action costs, and solves the MDP once the state space stabilizes. The resulting policy acts as a controller: for states where the correct move is fixed (e.g., a specific tool call or templated reply), it executes directly without invoking the LLM; only unseen states are routed back to the model.
- Empirical results are striking: on τ²-bench telecom, the solved controller alone (no model) achieves 79% task success. Running Qwen3.8-27B as a BLM raises success from 29% to 96% while cutting model calls by 93%. For Claude Opus 5.5, which already achieves 96%, BLM deployment reduces model calls and per-task cost by approximately 98% while solving two additional tasks. On InventoryBench, the solved policy outperforms every published method. However, the authors acknowledge a clear limitation: when the hard part is generating novel content (e.g., resolving SymPy issues) rather than selecting among discrete moves, few decisions can be pre-solved and BLMs provide little benefit.

## Context
This work sits at the intersection of reinforcement learning theory and practical LLM agent engineering. Agentic AI systems increasingly rely on multi-step tool use, planning, and state tracking, yet most current implementations treat each step as a fresh generation problem conditioned on a growing prompt. The paper draws on Richard Bellman's foundational dynamic programming framework to argue that bounded decision spaces should be solved once and cached, analogous to how classical RL agents learn optimal policies. This connects to broader research on agent memory, workflow caching, and the economics of inference in production AI systems.

## Implications
For practitioners deploying LLM agents in production, this approach offers a path to drastically lower inference costs and latency for repetitive or bounded workflows—such as customer support triage, inventory management, or structured tool-use pipelines—without sacrificing reliability. The 98% cost reduction on Claude Opus 5.5 suggests that many current agentic deployments are paying for redundant reasoning that a solved policy could eliminate. The paper also sets a boundary for where such optimization applies, guiding teams to reserve full LLM reasoning for open-ended generation tasks while automating the decision layer where state spaces are enumerable, potentially reshaping how agent architectures are designed for cost-sensitive applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.24871v1)
