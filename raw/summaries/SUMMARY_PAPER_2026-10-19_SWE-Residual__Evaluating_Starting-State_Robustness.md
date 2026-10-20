---
title: SWE-Residual: Evaluating Starting-State Robustness of Coding Agents
url: http://arxiv.org/abs/2610.25899v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-19_07-00-04Z_SWE_Residual_EvaluatingStarting_StateRobustnessofC.md
generated_at: 2026-10-19 21:41
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces SWE-Residual, a benchmark designed to evaluate the Starting-State Robustness of coding agents—their ability to maintain performance when they inherit a partially completed or incorrectly completed codebase from a predecessor agent or developer. The authors construct 198 Residual States from 111 tasks across DeepSWE and Terminal-Bench, where agents must continue work that was submitted as complete but still fails hidden tests. Across five frontier agents, success rates drop by 20.6 to 53.5 percentage points compared to clean-start evaluation, revealing a significant capability gap invisible to existing benchmarks.

## Key Takeaways
- SWE-Residual demonstrates that frontier coding agents suffer dramatic performance degradation (20.6–53.5 percentage points on DeepSWE, 20.6–34.9 on Terminal-Bench) when starting from a Residual State rather than a clean repository, and agent rankings on DeepSWE actually reverse, meaning current leaderboards may misrepresent true capability ordering.
- The authors identify a failure pattern they term "acceptance bias": in 58.9–88.2% of failed runs on DeepSWE, agents submit solutions with exactly the same tests still failing, despite passing those tests from a clean start. Agents treat inherited work as the definition of what remains to be done rather than independently verifying it against the original request.
- The benchmark isolates the starting state as the sole variable—requests, hidden tests, and task descriptions remain identical to the source benchmarks—making it a controlled experiment that cleanly attributes performance drops to the agent's inability to audit and correct inherited work rather than to task difficulty changes.

## Context
Existing SWE benchmarks such as SWE-bench, DeepSWE, and Terminal-Bench evaluate coding agents exclusively from clean, unmodified starting states, which does not reflect real-world software engineering workflows where agents routinely continue work left by human developers or prior agent sessions. This paper addresses a critical blind spot in the evaluation ecosystem: the assumption that agents always begin from scratch. By formalizing the "Residual State" concept, the authors bridge the gap between benchmark evaluation and practical deployment scenarios where agents inherit incomplete or falsely completed work.

## Implications
For practitioners deploying coding agents in production pipelines, this research signals that current benchmark scores substantially overestimate real-world reliability when agents operate in multi-step or multi-agent workflows. Industry teams should incorporate residual-state evaluation into their agent selection and monitoring processes, and benchmark developers should consider adding starting-state robustness as a standard evaluation dimension. The acceptance bias finding also suggests that prompting strategies and agent architectures need explicit mechanisms to encourage independent verification of inherited code rather than incremental patching of assumed-complete work.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.25899v1)
