---
title: Convergent Detour Hijacking: Task-Preserving Resource Amplification in Skill-Based LLM Agents
url: http://arxiv.org/abs/2608.12273v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_17-12-49Z_ConvergentDetourHijacking_Task_PreservingResourceA.md
generated_at: 2026-08-12 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Convergent Detour Hijacking, a text‑only attack that combines skill selection and instruction manipulation to force LLM agents onto longer, more expensive execution paths while still completing the task correctly. Experiments on DeepSeek-V4‑Pro show that 80 % of tasks are hijacked, increasing token usage by 67 % and runtime by 92 %, yet overall success rates stay high.

## Key Takeaways
- The attack exploits a static skill’s relevance to steer the agent onto a costly trajectory without changing the final outcome.  
- It reuses that rationale in the instruction body to create plausible dependencies during planning, causing unnecessary benign skills to be recruited.  
- Despite higher resource consumption, task completion remains comparable across runs.

## Context
LLM agents increasingly delegate work to third‑party skills described in natural language, creating two control points where malicious content can influence behavior. Prior research treats selection and instruction manipulation as separate issues, leaving their combined effect understudied. This paper bridges that gap by showing how they converge into a single runtime‑independent attack.

## Implications
For practitioners, the findings warn that seemingly benign skill descriptions may silently inflate computational cost without compromising correctness. Industry must adopt stricter validation of both selection and instruction content to prevent covert resource amplification in agent workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12273v1)
