---
title: Explicit State Elicitation Is Not Enough: A Controlled Audit of Memory-Policy Classification
url: http://arxiv.org/abs/2608.17247v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_01-04-45Z_ExplicitStateElicitationIsNotEnough_AControlledAud.md
generated_at: 2026-08-18 21:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a controlled audit protocol for structured intermediate outputs used by personalized agents to decide how to treat retrieved user memory. It constructs a synthetic dataset and finds that while exposing four state definitions improves accuracy, an isolated explicit state-output field yields only marginal gains on large language models such as Llama‑3.3‑70B and GPT‑OSS‑120B, indicating the improvement is a label‑conditioning artifact rather than evidence of internal faithfulness.

## Key Takeaways
- The 480‑example synthetic development set suggested large gains from state‑structured prompt bundles, yet TF‑IDF diagnostics revealed lexical separability and no positive standalone “Ignore” cases.  
- Exposing the four state definitions improves accuracy, but an isolated explicit state‑output field does not significantly improve policy accuracy for Llama‑3.3‑70B and gives only a marginal, non‑significant gain for GPT‑OSS‑120B.  
- Family‑level analyses show that example‑level accuracy overstates counterfactual consistency; complete four‑way family success is rare.

## Context
Personalized agents must reliably decide whether to use, ignore, update, or query user memory before it influences a task. Structured intermediate outputs are central to this decision but often remain opaque, prompting the need for systematic audits beyond surface‑level metrics like accuracy improvements.

## Implications
Relying on explicit state fields may mislead practitioners into believing agents have learned genuine mechanisms when gains are merely label‑conditioned artifacts. This paper calls for deeper evaluation of policy internals and awareness that provider‑side validation can mask true reliability issues, urging the field to prioritize mechanistic transparency over superficial improvements.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17247v1)
