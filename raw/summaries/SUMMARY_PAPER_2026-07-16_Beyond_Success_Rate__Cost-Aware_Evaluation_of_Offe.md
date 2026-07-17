---
title: Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security Agents
url: http://arxiv.org/abs/2607.15263v1
type: paper-summary
date: 2026-07-16
source_paper: 2026-07-16_17-54-47Z_BeyondSuccessRate_Cost_AwareEvaluationofOffensivea.md
generated_at: 2026-07-16 23:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes a cost‑aware evaluation framework that measures the economic efficiency of language‑model security agents beyond their peak success rates. By fixing inference budgets and separating spending on reasoning versus tool usage, the authors find that offensive CTF performance scales with additional compute while defensive SOC investigation remains limited by disciplined tool use and telemetry navigation.

## Key Takeaways
- Offensive CTF performance improves when more test‑time compute is allocated, indicating a strong scaling regime for red‑team tasks.  
- Open‑weight models can achieve scores comparable to proprietary frontier systems while staying cost‑competitive under fixed budgets.  
- Defensive SOC investigation does not benefit proportionally from larger reasoning budgets; success hinges on careful tool selection and selective enrichment rather than raw compute.

## Context
The prevailing security‑agent benchmarks focus solely on task completion, ignoring the operational costs of inference and external calls. This narrow view obscures how models behave under realistic resource constraints in SOC environments where budget is limited and every query matters.

## Implications
Cost‑aware evaluations guide practitioners toward agents that deliver value per dollar spent, ensuring tools are not over‑used or misallocated. The findings suggest a shift from pure success metrics to economic efficiency benchmarks for both offensive red‑team and defensive blue‑team workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.15263v1)
