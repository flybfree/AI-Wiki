---
title: DCFA: Dual-view Causal-inspired Attribution for Failure Reasoning in LLM-based Multi-agent Systems
url: http://arxiv.org/abs/2609.04749v1
type: paper-summary
date: 2026-09-06
source_paper: 2026-09-04_05-29-31Z_DCFA_Dual_viewCausal_inspiredAttributionforFailure.md
generated_at: 2026-09-06 21:31
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces DCFA, a training‑free framework for attributing failures in LLM‑based multi‑agent systems by identifying the earliest decisive error that could reverse system failure. Experiments on the Who&When benchmark show DCFA improves step‑level accuracy by up to 8.27% over existing baselines.

## Key Takeaways
- DCFA tackles shallow attribution by constructing a global causal‑inspired dependency graph from full system traces, capturing the decisive error that minor issues miss.
- The framework also addresses contextual degradation through a local counterfactual module that refines causal reasoning as trace length grows.
- On six LLMs across Who&When, DCFA achieves up to 8.27% higher step‑level accuracy than state‑of‑the‑art methods.

## Context
LLM‑driven multi‑agent systems are increasingly deployed for complex tasks but suffer from fragile reasoning and coordination failures that degrade performance as interaction histories lengthen. This research advances failure analysis beyond simple error detection toward causal attribution, a key need for robust AI agents.

## Implications
Practitioners can leverage DCFA to design more reliable agent pipelines without retraining models, reducing costly system outages. The approach also informs future work on self‑diagnosing AI systems and improving long‑term reasoning stability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04749v1)
