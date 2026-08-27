---
title: CaSKG: Counterfactual-Causal Skill Graphs for Scalable Agent Skill Retrieval
url: http://arxiv.org/abs/2608.25500v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_08-12-41Z_CaSKG_Counterfactual_CausalSkillGraphsforScalableA.md
generated_at: 2026-08-26 20:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CaSKG, a counterfactual‑causal skill graph framework designed to improve the retrieval of reusable procedural skills for large language model agents. By calibrating skill relationships before retrieval, CaSKG builds high‑recall directed graphs that preserve workflow context and reduce memory access costs. Experiments on twelve model‑benchmark pairs show state‑of‑the‑art gains in task scores and efficiency.

## Key Takeaways
- CaSKG constructs a candidate graph using semantic, lexical, input/output, and structural evidence, then refines it with an optional LLM judge to produce calibrated edge scores.
- The framework applies direction‑conditioned textual counterfactual probes that remove, substitute, or reorder skill pairs, aggregating the results via Bayesian smoothing for task‑specific graphs.
- Compared with Graph‑of‑Skills, CaSKG lifts ScienceWorld macro‑average scores by 7.88 points and ALFWorld success rates to 86.79 %, while cutting mean environment steps.

## Context
Current skill libraries suffer from high retrieval latency or loss of workflow context when skills are treated as independent text snippets. Efficient, executable skill retrieval is essential for scaling LLM agents across diverse tasks without altering downstream policies.

## Implications
The results demonstrate that edge‑confidence calibration can yield compact yet effective skill graphs, offering a practical path to scalable agent design and reducing computational overhead in large language model applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25500v1)
