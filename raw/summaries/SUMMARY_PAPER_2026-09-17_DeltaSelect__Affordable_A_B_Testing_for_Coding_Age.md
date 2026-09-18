---
title: DeltaSelect: Affordable A/B Testing for Coding Agents
url: http://arxiv.org/abs/2609.19607v1
type: paper-summary
date: 2026-09-17
source_paper: 2026-09-17_02-42-02Z_DeltaSelect_AffordableA_BTestingforCodingAgents.md
generated_at: 2026-09-17 20:13
model: freedomaisvr/gemma-4-12b-it
---

## Summary
The paper introduces DeltaSelect, an open-source method designed to facilitate frequent and affordable A/B testing for coding agents by selecting specific tasks that correlate well with overall benchmark performance. It addresses the high costs of full-suite evaluations by using Pearson correlation and linear regression to identify a representative subset of tasks that fit within a specific dollar budget.

## Key Takeaways
- Current coding agent benchmarks are primarily designed for broad, comprehensive comparisons rather than frequent development decisions; however, individual runs often vary significantly, and only about 19.5% of tasks in the DeepSWE dataset showed a high correlation with full-benchmark performance.
- DeltaSelect identifies specific tasks where one-run results consistently track full-benchmark performance using Pearson correlation, allowing developers to evaluate model changes without running every test in a large suite.
- The methodology includes a mechanism to map fractional verifier results to a common score and selects a task set based on a fixed dollar budget, providing a practical framework for cost-constrained experimentation.
- A case study involving the gpt-5.6-luna model demonstrated that DeltaSelect allowed researchers to reduce costs by 58.1% while maintaining high performance, proving its effectiveness in refining specific agent skills and instructions.

## Context
As AI agents become more complex and expensive to evaluate, researchers need ways to iterate quickly without running exhaustive benchmarks every time a small change is made. This paper addresses the practical infrastructure gap between "one-off" leaderboard rankings and the day-to-day engineering required to improve agentic behavior in production environments.

## Implications
For practitioners, this means that high-quality A/B testing for coding agents can be achieved at a fraction of the cost by using smarter selection methods rather than simply scaling up compute. It provides a framework for teams to iterate on specific skills and instructions more rapidly, democratizing the ability to refine agent performance in resource-constrained environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.19607v1)
