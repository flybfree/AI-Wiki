---
title: Scaling Inference-Time Compute with Teams of Coding Agents
url: http://arxiv.org/abs/2610.17471v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-12_22-35-08Z_ScalingInference_TimeComputewithTeamsofCodingAgent.md
generated_at: 2026-10-14 00:46
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper formulates multi-agent team design as a compute allocation problem, asking where additional inference compute should be directed across a team of coding agents to maximize reward while minimizing cost. Through systematic experiments on ProgramBench, the authors demonstrate that a heterogeneous 17-agent team can match a strong homogeneous 5-agent team at 70% lower cost, provided compute is allocated strategically to planning rather than implementation or verification stages.

## Key Takeaways
- Planning delegation is the highest-value use of additional agents: a lead agent that delegates only the planning stage to its workers, while handling implementation and verification itself, achieves the same reward as a lead that delegates all three stages to workers, but at half the cost. This finding reframes team design around stage-specific allocation rather than uniform delegation.
- Model heterogeneity is a powerful cost lever: a strong lead paired with cheap planner agents recovers 47.5% of the reward gain of an all-strong team for only 13.9% of the additional cost, whereas substituting cheap models as implementers actively degrades reward. This asymmetry suggests that reasoning-heavy tasks like planning tolerate cheaper models, while execution-heavy tasks like coding do not.
- Scaling behavior differs sharply by role: adding more planner agents continues to improve reward as team size grows, but implementers and verifiers plateau beyond four workers. This means that naively increasing team size yields diminishing returns unless the additional agents are assigned to planning roles, and that the optimal team composition depends on the specific task, budget, and latency constraints a user faces.

## Context
The broader AI research landscape has increasingly explored inference-time scaling through techniques like chain-of-thought reasoning, tree-of-thought search, and self-consistency sampling, all of which concentrate compute within a single agent. This paper introduces a complementary axis—parallel multi-agent coordination—and rigorously characterizes its cost-reward tradeoffs. By building a minimal harness from scratch and varying one factor at a time (delegation stage, model composition, team size), the authors provide a controlled experimental foundation that distinguishes genuine coordination benefits from the noise of duplicate work and coordination failures that plague ad hoc multi-agent systems.

## Implications
For practitioners deploying coding agents in production, this work offers a concrete playbook for spending an agent budget efficiently: invest in diverse planners, keep implementation and verification under a strong lead, and cap implementer/verifier teams at four workers. For the field, it signals that heterogeneous team composition is not merely a cost-cutting trick but a principled strategy for reaching the reward-cost Pareto frontier, which could reshape how organizations architect agentic pipelines under real-world latency and budget constraints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.17471v1)
