---
title: EcoAgent-Bench: Evaluating Economic Decision-Making in Budget-Constrained LLM Agents
url: http://arxiv.org/abs/2608.05519v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_01-47-47Z_EcoAgent_Bench_EvaluatingEconomicDecision_Makingin.md
generated_at: 2026-08-06 20:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces EcoAgent-Bench, a benchmark that evaluates economic decision‑making in budget‑constrained LLM agents by assigning priced actions and explicit budgets to tasks. The study shows that while micro‑averaged accuracy rewards one‑sided policies such as always escalating, these strategies often fail on save‑oriented tasks, highlighting the need for separate evaluation of completion under a budget versus economical action selection.

## Key Takeaways
- The benchmark includes 304 real‑derived tasks with priced actions and budgets, testing decisions like avoiding unnecessary escalation or selecting a model tier.  
- Tool‑API agents achieve only 3.9–24.0% micro strict success at best, often stopping before warranted escalation or overspending on cheap tasks.  
- A budget sweep changes GPT‑5.4’s escalation rate from 0 % to 3 %, demonstrating that completion under a budget and economical action selection are distinct properties.

## Context
The work expands beyond traditional task‑completion benchmarks by incorporating resource constraints, which are increasingly relevant as LLM agents operate in real‑world workflows where cost matters. By treating decision choices as part of the task rather than auxiliary metrics, EcoAgent-Bench aligns evaluation with deployment realities.

## Implications
For practitioners, this research underscores that optimizing for accuracy alone can lead to economic inefficiencies, prompting a shift toward multi‑objective benchmarks. Industry adoption may require tools that enforce budget limits and reward cost‑effective actions without sacrificing task success.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05519v1)
