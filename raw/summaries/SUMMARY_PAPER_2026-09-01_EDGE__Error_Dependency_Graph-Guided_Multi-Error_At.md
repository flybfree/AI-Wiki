---
title: EDGE: Error Dependency Graph-Guided Multi-Error Attribution in Multi-Agent LLM Systems
url: http://arxiv.org/abs/2609.01360v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_15-00-54Z_EDGE_ErrorDependencyGraph_GuidedMulti_ErrorAttribu.md
generated_at: 2026-09-01 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces EDGE, a framework that models error dependency graphs to attribute multiple related errors in multi-agent LLM systems more accurately than single‑error methods. By constructing and validating an inference graph through counterfactual rollouts, EDGE enables a two‑stage LLM‑as‑judge detector that improves category‑level attribution across various models and prompting strategies.

## Key Takeaways
- EDGE constructs an error dependency graph from observed error events and validates a reliable causal subset using counterfactual rollout.  
- The inference graph guides a two‑stage LLM‑as‑judge detector for multi‑error attribution.  
- Experiments on TRAIL and MAST demonstrate that EDGE improves category‑level multi‑error attribution across most evaluated models and settings, even with adapted Who&When‑style prompts.

## Context
Current attribution methods often focus on identifying a single responsible agent or root cause, overlooking the interconnections among multiple errors. In complex LLM interactions, errors frequently arise together, making isolated analysis insufficient for effective debugging and repair. This work addresses that gap by introducing a dependency‑aware approach.

## Implications
Understanding error dependencies can lead to more precise explanations and targeted fixes, reducing unnecessary system downtime. Practitioners can leverage EDGE’s graph to prioritize interventions, enhancing reliability in production LLM agents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01360v1)
