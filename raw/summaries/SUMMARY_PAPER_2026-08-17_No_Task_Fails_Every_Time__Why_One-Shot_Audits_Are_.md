---
title: No Task Fails Every Time: Why One-Shot Audits Are Structurally Blind to Agent Damage
url: http://arxiv.org/abs/2608.15286v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_15-33-32Z_NoTaskFailsEveryTime_WhyOne_ShotAuditsAreStructura.md
generated_at: 2026-08-17 21:37
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces AgentRelBench, an environment-agnostic instrument that measures AI agent reliability by comparing database state diffs without involving LLMs. Across 2,128 evaluation runs and nine models it finds that damage is universal yet not always present on every run, and a single audit often misses the damaging task.

## Key Takeaways
- Damage on irreversible actions appears across all model families and varies stochastically within each family when using fixed provider stacks.
- No task fails every time; among 42 confirmed damage events only zero always-fail cells were observed, indicating that a clean run can miss a damage-producing pair about 80% of the time in the development pool.
- The count of damaging tasks declines with model capability, but this gradient is confounded by family and training, so it reflects observation not causation.

## Context
This work addresses a longstanding challenge in AI safety: verifying that autonomous agents do not cause irreversible harm. By using state diffs instead of human judgments, the study reduces reliance on subjective grading and highlights limitations of one‑shot audit methods.

## Implications
For practitioners, the findings suggest that reliability metrics must account for stochasticity and that single‑run audits are insufficient to guarantee safety. The paper calls for more robust evaluation frameworks that capture damage across runs rather than assuming perfect consistency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15286v1)
