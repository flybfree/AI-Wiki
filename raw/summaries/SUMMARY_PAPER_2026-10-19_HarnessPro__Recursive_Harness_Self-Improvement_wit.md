---
title: HarnessPro: Recursive Harness Self-Improvement with Pareto Optimization for Performance-Cost Trade-offs
url: http://arxiv.org/abs/2610.26770v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-19_17-27-38Z_HarnessPro_RecursiveHarnessSelf_ImprovementwithPar.md
generated_at: 2026-10-19 22:54
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
HarnessPro introduces a label-free recursive self-improvement method for evolving AI agent harnesses that simultaneously improves task performance and reduces execution cost. Rather than optimizing for a single objective, it produces three tiers of harnesses—lite, medium, and heavy—selected via normalized weighted squared-distance to match different deployment budgets. Experiments on Terminal-Bench 2, SWE-Bench Pro, and ProgramBench show the heavy mode achieves a 2.0 percentage-point average pass-rate gain and a 26.1% per-task cost reduction compared to the RHO baseline.

## Key Takeaways
- HarnessPro operates without ground-truth labels or official test suites. Candidate harnesses are evaluated using LLM-generated tests, and specialized agents diagnose execution trajectories, plan updates with varying performance-cost priorities, and implement them as new candidate harnesses. This label-free evaluation loop makes the method broadly applicable to environments where gold-standard test cases are unavailable or expensive to obtain.
- The method employs a normalized weighted squared-distance selection mechanism to produce three distinct harness variants: a cost-focused "lite" version, a balanced "medium" version, and a performance-focused "heavy" version. This multi-objective Pareto-style approach lets practitioners choose the appropriate trade-off for their specific budget constraints rather than being locked into a single optimization target.
- Across multiple benchmarks and model backends (GPT-5.5 with Codex, GLM-5.2 with Claude Code), the heavy mode consistently outperforms the RHO baseline, delivering both higher pass rates and substantially lower per-task execution costs. The fact that gains hold across different model-provider combinations suggests the harness-evolution strategy is model-agnostic and transferable.

## Context
AI agent harnesses—the scaffolding code that orchestrates tool use, planning, and execution for large language model agents—are a critical bottleneck in agent capability. Prior recursive self-improvement approaches such as RHO have demonstrated that harnesses can evolve themselves, but they typically sacrifice efficiency for raw performance, inflating token usage and latency. HarnessPro addresses this gap by formalizing the performance-cost trade-off as a multi-objective optimization problem within the RSI loop, reflecting a broader industry shift toward sustainable, budget-aware AI deployment.

## Implications
For practitioners deploying coding agents in production, HarnessPro offers a practical path to reduce operational costs by over a quarter while still improving task success rates, directly impacting cloud spend and latency budgets. The label-free evaluation design lowers the barrier for teams that lack curated test suites, making harness optimization accessible to smaller organizations. For the research community, the Pareto-based selection framework suggests a template for future agent-evolution work where resource constraints are treated as first-class design parameters rather than afterthoughts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.26770v1)
