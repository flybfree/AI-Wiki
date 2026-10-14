---
title: Autonomous Science Bench: Evaluating AI Agents for Autonomous Scientific Discovery
url: http://arxiv.org/abs/2610.18449v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_14-18-56Z_AutonomousScienceBench_EvaluatingAIAgentsforAutono.md
generated_at: 2026-10-14 00:41
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
The paper introduces Autonomous Science Bench, a benchmark comprising six budgeted design-build-test-learn campaigns grounded in real published experiments across biology, chemistry, and materials science, designed to evaluate AI agents that must autonomously select experimental batches under constrained budgets. In a pilot evaluation across eight agent-model configurations and 144 trials, the best configuration achieved a 67% success rate, while the hardest campaign was solved in only three of 24 attempts, revealing that overall success rates obscure distinct failure modes between discovery and learning capabilities.

## Key Takeaways
- The benchmark enforces a dual-gate evaluation system: a discovery gate assesses whether the agent actually measured promising designs within its budget, while a learning gate evaluates whether the agent's predictive model correctly ranks held-out designs. This two-gate design exposes fundamentally different weaknesses—some agents build accurate rankings but fail to explore enough of the design space to find promising candidates, while others discover good designs but cannot generalize predictions to unseen candidates. These failure modes are invisible when only aggregate success rates are reported.
- The campaigns are grounded in published experimental literature rather than simulations, requiring agents to interact with a real lab service that returns measurements, making the benchmark a more faithful test of autonomous scientific workflows than prior simulation-based or fixed-dataset evaluations. Agents must iteratively select batches of designs, receive measurements, update their strategy, and ultimately deliver a predictive model, all under a fixed experimental budget.
- The pilot results demonstrate that current agent-model configurations remain far from reliable autonomous science: the hardest campaign was solved in only 3 out of 24 attempts (12.5%), indicating that even the best-performing configurations struggle with the most challenging experimental design problems, and that no single configuration dominates across all six campaigns spanning three scientific domains.

## Context
Most existing benchmarks for AI science agents either provide static datasets for post-hoc analysis or rely on simulated environments that do not capture the noise, cost constraints, and iterative decision-making inherent to real laboratory work. Autonomous Science Bench fills this gap by grounding its six campaigns in published experiments and introducing a budgeted, interactive experimentation loop with a real lab service. This positions the benchmark as a critical step toward evaluating whether AI agents can genuinely perform closed-loop scientific discovery rather than merely fitting models to pre-collected data.

## Implications
For AI researchers and practitioners building autonomous science agents, the dual-gate evaluation framework provides a diagnostic tool to identify whether an agent's bottleneck lies in exploration strategy or in model generalization, enabling targeted improvements rather than blind optimization of aggregate scores. For the broader scientific community and industry, the public leaderboard and open release of version 0.1 campaigns establish a shared, reproducible standard for tracking progress toward AI-driven experimental design, which could accelerate the adoption of autonomous agents in drug discovery, materials development, and chemical synthesis pipelines where experimental budgets are a primary constraint.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.18449v1)
