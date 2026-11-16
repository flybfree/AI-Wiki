---
title: Contain, Conform, Compare (Extended Version): A Red-Teamed Evaluation Kit for Small Coding Agents and the Full Record of Its Experiments
url: http://arxiv.org/abs/2611.16485v1
type: paper-summary
date: 2026-11-15
source_paper: 2026-11-12_08-54-03Z_Contain_Conform_Compare_ExtendedVersion__ARed_Team.md
generated_at: 2026-11-15 21:27
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces drydock-eval, a local evaluation kit designed to replicate the hosted scoring environment of the Gemma 4 Developer Agent competition for small coding agents, specifically the Gemma 4 E4B model. The extended version publishes the complete experimental record—9,660 agent-run rows, 2,494 grading controls, and 72 serving measurements—demonstrating that prompt-level and agent-configuration changes produced no statistically confirmed improvements in solve rates, while a large fraction of tasks remained unsolved across repeated runs.

## Key Takeaways
- The evaluation kit is structured around three pillars: Contain executes each job in a fresh, network-isolated container validated by 200 scripted escape tests; Conform provides eight granular checks that align a local stack's request rendering with the hosted scorer's configuration down to token-level fidelity; Compare applies paired statistical methods that respect repository clustering to avoid inflated significance. Together these components enable approximately 250 evaluation runs per hour on a single RTX 5090 GPU.
- A pre-registered five-arm experiment spanning 231 tasks and 4,620 jobs tested four distinct prompt divergences against the E4B agent and detected no meaningful change in solve rate, with the largest estimated effect at −2.1 percentage points (95% confidence interval −4.4 to +0.4). Three subsequent agent modifications showed apparent gains of +1.0 to +6.2 points on screening tasks but failed to replicate under a frozen pass rule on held-out tasks, yielding results of −0.35, −0.39, and +4.10 points.
- The unchanged baseline, re-run on the same 128 tasks, shifted by 1.17 points, and 65% of those tasks were solved in none of eight independent runs, underscoring substantial run-to-run variance and the difficulty small coding agents face on the benchmark. Serving measurements on four L4 GPUs showed the 31B model decoding at 38.1 tokens per second versus 105.8 for E4B, and six configurations of the 31B agent solved between 37 and 44 of 70 development tasks with no pairwise difference detected.

## Context
As hosted leaderboard scores for coding-agent competitions become the primary signal for model development, practitioners increasingly need local evaluation harnesses that faithfully mirror the hosted scorer's prompts, sandboxing, and grading logic. This paper addresses a gap in the small-model evaluation ecosystem by providing a fully open, reproducible kit that lets researchers iterate quickly on constrained hardware while preserving statistical rigor through pre-registered designs and paired comparisons. The work also reflects a growing methodological shift toward red-teaming evaluation tooling itself—having AI agents build and attack the kit before human approval—signaling a maturation of evaluation infrastructure as a first-class research artifact.

## Implications
For practitioners building or tuning small coding agents, the findings caution against over-interpreting single-run or screening-task improvements: apparent gains from prompt engineering or agent configuration changes frequently vanish under held-out testing, and high task-unsolved rates across repeated runs suggest that current small models remain brittle on realistic coding benchmarks. The fully released run-level data and the transparent failure to confirm agent modifications provide a template for honest, reproducible agent evaluation that industry teams can adopt to avoid chasing noise on leaderboards. The open release of prompts and agent bundles, combined with withheld proprietary components, also offers a practical model for balancing transparency with competitive confidentiality in future agent competitions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.16485v1)
