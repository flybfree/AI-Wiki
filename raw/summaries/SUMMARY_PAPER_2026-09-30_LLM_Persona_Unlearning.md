---
title: LLM Persona Unlearning
url: http://arxiv.org/abs/2609.39882v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_14-55-52Z_LLMPersonaUnlearning.md
generated_at: 2026-09-30 22:16
model: qwen3.6-35b-a3b
---

## Summary
This paper addresses the challenge of persona unlearning in large language models, aiming to perform weight-level edits that prevent specific behavioral modes from being elicited by prompts while preserving general utility. The authors introduce PersonaUnlearnBench to evaluate existing methods, revealing that standard unlearning techniques fail to remove target personas without degrading model performance. To overcome this limitation, they propose PaCE, a method that learns internal behavior directions by contrasting target and desirable responses, successfully suppressing unwanted personas with high response quality and minimal utility loss.

## Key Takeaways
- Standard unlearning methods are insufficient for persona removal; the benchmark demonstrates that current approaches cannot reliably erase designated personas without causing significant sacrifices in meaningful generation capabilities and overall model utility, highlighting a gap in existing weight-editing techniques.
- The proposed PaCE method operates by comparing target and desirable responses to identical questions to identify an internal behavior direction, then updates model weights to shift the target-prompt states away from the unwanted mode toward the matched desirable response, achieving effective suppression with moderate utility costs.
- PersonaUnlearnBench provides a rigorous evaluation framework spanning six LLMs across three families and five personas, utilizing aligned forget/retain sets, held-out instruction paraphrases, and a four-axis evaluation metric to establish persona unlearning as a distinct behavior-level editing problem requiring persistent control over latent response policies.

## Context
As large language

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.39882v1)
