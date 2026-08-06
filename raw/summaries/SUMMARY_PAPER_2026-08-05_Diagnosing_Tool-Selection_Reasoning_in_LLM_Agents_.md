---
title: Diagnosing Tool-Selection Reasoning in LLM Agents with Canary Tools
url: http://arxiv.org/abs/2608.04719v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_11-38-33Z_DiagnosingTool_SelectionReasoninginLLMAgentswithCa.md
generated_at: 2026-08-05 20:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces canary tools, diagnostic probes embedded in an agent’s tool set to reveal the specific reasons behind incorrect tool selection by large language models. Evaluating eight diverse models across 120 tasks under varying canary densities reveals a stark increase in susceptibility as model capability rises, a decoupling between capability tier and safety performance, and a taxonomy that stratifies reasoning weaknesses along six distinct dimensions.

## Key Takeaways
- Susceptibility drops sharply with higher capability: the per‑task canary susceptibility rate (CSR) varies roughly 36× from the most robust model to the least capable, with Claude Opus 4.8 showing the lowest CSR and Llama 3.1 8B the highest.  
- Capability tier alone does not predict safety: the most vulnerable hosted model is mid‑tier, while within a provider the cheaper model can be safer than the pricier one, indicating that cost or deployment constraints affect robustness more than raw capability.  
- The six‑type taxonomy (semantic decoys, parameter traps, capability mirages, prerequisite blindness, temporal decoys, granularity traps) is capability‑stratified: capability mirages reliably trap frontier models, whereas the other types are largely inert on strong models but fire on small open models, showing that the probes discriminate by model strength rather than merely exposing weak phrasing.

## Context
Understanding why LLMs choose suboptimal tools is crucial for reliable agent design and deployment. Current evaluations often report only the outcome of tool selection without probing the underlying reasoning mechanisms, limiting insights into how to improve robustness across diverse models.

## Implications
These findings suggest that diagnostic probes can systematically expose model weaknesses, guiding developers to prioritize safety improvements where they are most needed. For industry practitioners, integrating such canary‑based assessments could prevent costly failures in real‑world agents and promote more equitable performance across model tiers.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04719v1)
