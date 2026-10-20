---
title: Design and Cross-Domain Evaluation of an Agent Execution Harness
url: http://arxiv.org/abs/2610.25568v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-18_22-08-15Z_DesignandCross_DomainEvaluationofanAgentExecutionH.md
generated_at: 2026-10-20 00:20
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper presents an agent execution harness architecture that separates the user's original objective from a revisable plan and execution record, coordinating planner, worker, and reviewer roles to complete complex tasks across multiple domains. The authors evaluate their system on Terminal-Bench 2.1 (achieving 93.26% pass rate), HealthBench Professional (scoring 69.63 on a length-adjusted rubric across 525 tasks), and a 53-task paired comparison showing a 19.89-point aggregate improvement over direct completion, while documenting the associated cost increase from $0.29 to $2.13 per task. The work emphasizes evaluating not just outcomes but also execution trajectories, instruction revisions, reviewer decisions, and resource consumption to understand where coordination helps and where it introduces regressions.

## Key Takeaways
- The harness architecture enforces a strict separation between the original user objective, a revisable execution plan, and a persistent execution record, with distinct roles for planning, working, and reviewing. This separation prevents drift from the user's stated goal while allowing iterative refinement of the plan through domain-specific instructions that are refined using task inputs and execution trajectories without relying on official grading feedback.
- On Terminal-Bench 2.1, the harness passes 83 of 89 instances (93.26%), demonstrating strong performance on terminal-based tasks. On HealthBench Professional, a Fable-configured system achieves a length-adjusted rubric score of 69.63 across 525 clinical tasks, showing applicability in high-stakes professional domains.
- The paired HealthBench comparison reveals a critical nuance: while the aggregate score improves by 19.89 points over direct completion, the median task-level change is actually negative (-1.46 points), indicating that the harness helps on average but can regress on individual tasks. Mean inference cost rises from $0.29 to $2.13 per task, highlighting a substantial cost tradeoff that practitioners must weigh against quality gains.

## Context
As language-model agents move from simple single-turn completions toward multi-step task execution, the field faces increasing pressure to coordinate planning, execution, and quality review within a single pipeline. Most existing agent frameworks treat planning and execution as monolithic processes, making it difficult to audit whether the final output actually addresses the user's original request. This paper contributes to the growing body of work on agent orchestration architectures by formalizing a harness pattern that makes coordination explicit, auditable, and measurable across heterogeneous domains including software engineering, clinical reasoning, application development, and scientific inquiry.

## Implications
For practitioners deploying agent systems in production, this work provides a concrete template for building multi-role agent pipelines with built-in review stages, while also quantifying the real cost of such coordination in both latency and monetary terms. The finding that aggregate improvements can mask per-task regressions is particularly important for safety-critical applications like healthcare, where a system-level score improvement does not guarantee that any individual task is handled better. The documented instruction revision process and reviewer decision logging offer a path toward transparent, auditable agent systems that can be refined over time without ground-truth grading, which is valuable for domains where labeled evaluation data is scarce or expensive to obtain.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.25568v1)
