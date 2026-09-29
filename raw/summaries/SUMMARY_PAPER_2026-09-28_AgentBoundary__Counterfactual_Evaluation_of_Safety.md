---
title: AgentBoundary: Counterfactual Evaluation of Safety in Tool-Using LLM Agents
url: http://arxiv.org/abs/2609.33658v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-27_15-19-52Z_AgentBoundary_CounterfactualEvaluationofSafetyinTo.md
generated_at: 2026-09-28 21:50
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces AgentBound, a novel four-way counterfactual framework designed to evaluate safety in tool-using LLM agents by decoupling apparent risk from action permissibility. The authors demonstrate that current models struggle with agentic over-refusal, often blocking authorized tasks due to perceived risk while failing to distinguish competence from permission constraints. Through extensive evaluation and a runtime calibration module, the study reveals that effective agent alignment requires tracking execution evidence regarding permissions rather than relying solely on refusal mechanisms.

## Key Takeaways
- AgentBound provides the first four-way counterfactual evaluation framework that independently varies apparent risk and action permissibility within executable workflows, enabling precise diagnosis of agentic over-refusal and unsafe compliance while controlling for task competence.
- Evaluation across 17 model configurations reveals a significant trade-off where high safety often correlates with poor task execution; for instance, GPT-5.5 blocks nearly all routine unauthorized actions but completes only 28.7% of risky-looking authorized tasks, highlighting severe over-refusal issues.
- A lightweight runtime calibration module was developed that simultaneously improves authorized-task completion by an average

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.33658v1)
