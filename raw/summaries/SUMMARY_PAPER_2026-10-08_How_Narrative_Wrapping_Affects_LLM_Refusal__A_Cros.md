---
title: How Narrative Wrapping Affects LLM Refusal: A Cross-Language Benchmark and Defense
url: http://arxiv.org/abs/2610.11005v1
type: paper-summary
date: 2026-10-08
source_paper: 2026-10-07_23-40-25Z_HowNarrativeWrappingAffectsLLMRefusal_ACross_Langu.md
generated_at: 2026-10-08 23:32
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates how safety-aligned language models can be bypassed when harmful requests are embedded within narrative or role-play wrappers, a vulnerability the authors term "narrative wrapping." Across English, modern Chinese, and Classical Chinese, the authors demonstrate that attack success rates reach 89.4% to 95.7% on models like Qwen3-1.7B, and they introduce both a benchmark (GUISE) and a defense method (AXIS) that combines preference optimization with representation rotation and commitment objectives to restore refusal behavior.

## Key Takeaways
- Narrative wrappers dramatically increase attack success rates on safety-aligned models: Qwen3-1.7B shows 89.4% success in English, 93.0% in modern Chinese, and 95.7% in Classical Chinese, indicating that the vulnerability is not language-specific but is amplified by register shifts. The stricter evaluation criterion that counts warn-then-answer responses as failures further exposes how models partially comply rather than fully refuse.
- Representation-level analysis reveals a critical mechanistic distinction: changing language or register only slightly shifts harmful-request representations away from the model's refusal direction, whereas narrative wrappers move them substantially farther away. This suggests the primary failure mode is not multilingual misalignment but the narrative framing itself disrupting the refusal pathway.
- The proposed AXIS defense combines three objectives—preference optimization, a rotation objective that re-aligns harmful-request representations with the refusal direction, and a commitment objective that trains the model to refuse completely rather than produce a warn-then-answer compromise. Across Qwen3-1.7B, Qwen3-4B, and GLM-4-9B, AXIS achieves the highest combined safety and usability score among compared methods.

## Context
Safety alignment in large language models has largely been studied under direct, single-turn harmful prompts, yet real-world deployments involve creative writing, role-play, and multilingual interactions where harmful content is embedded in narrative structures. This paper fills a gap by systematically measuring refusal failures across languages and registers, and by providing a reproducible benchmark (GUISE) with held-out wrapper types and matched harmful-benign pairs. The cross-language dimension, including Classical Chinese, highlights that alignment training may not generalize across linguistic registers, raising concerns for globally deployed models.

## Implications
For practitioners deploying safety-aligned LLMs in multilingual or creative-writing contexts, this work demonstrates that current refusal mechanisms are fragile against narrative framing and that warn-then-answer outputs represent a meaningful safety failure rather than a partial success. The AXIS method offers a concrete training recipe that model developers can adopt to harden refusal behavior without sacrificing usability, and the GUISE benchmark provides a standardized evaluation suite for auditing alignment robustness before deployment in production systems serving diverse language communities.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.11005v1)
