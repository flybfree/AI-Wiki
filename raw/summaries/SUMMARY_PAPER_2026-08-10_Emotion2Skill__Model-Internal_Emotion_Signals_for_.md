---
title: Emotion2Skill: Model-Internal Emotion Signals for Adaptive Skill Selection and Evolution
url: http://arxiv.org/abs/2608.09248v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_08-09-24Z_Emotion2Skill_Model_InternalEmotionSignalsforAdapt.md
generated_at: 2026-08-10 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Emotion2Skill, a framework that extracts the model’s internal emotion vectors from its residual stream and uses them to guide skill selection and evolution in LLM agents. On WebShop and ALFWorld, the approach raises the success rate by 26.9% and 25.5% compared with a zero‑shot baseline, outperforming all other methods.

## Key Takeaways
- Emotion2Skill extracts a 27‑dimensional emotion state from the LLM’s residual stream at each decision step to create a confidence‑gated summary that is injected into routing prompts.
- The method identifies abrupt internal‑state shifts that signal problematic skill invocations, enabling targeted SOP rewriting instead of coarse binary outcomes.
- Co‑activation analysis confirms semantically coherent emotion–skill pairings, showing the improvements stem from genuine internal signals rather than statistical noise.

## Context
LLM agents increasingly rely on external skill libraries for task execution, yet their routing decisions are limited to observable text cues. Understanding hidden representational dynamics such as linear emotion vectors could unlock more robust and adaptive behavior.

## Implications
This work demonstrates that model‑internal states can be directly leveraged for decision‑level control, moving beyond post‑hoc interpretability toward practical system design. Practitioners may integrate similar signal extraction to improve reliability in complex multi‑skill environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09248v1)
