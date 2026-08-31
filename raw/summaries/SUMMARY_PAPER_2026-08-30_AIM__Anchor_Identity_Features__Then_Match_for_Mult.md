---
title: AIM: Anchor Identity Features, Then Match for Multimodal Large Language Model Unlearning
url: http://arxiv.org/abs/2608.28312v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_13-22-22Z_AIM_AnchorIdentityFeatures_ThenMatchforMultimodalL.md
generated_at: 2026-08-30 20:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
Multimodal large language models (MLLMs) can memorize identity-specific facts during fine‑tuning, creating privacy risks when a person requests deletion. The paper introduces AIM, a two‑stage method that suppresses these memories without requiring access to retained images or ground‑truth answers.

## Key Takeaways
- Identity questions cluster by person while perception questions cluster by question type, indicating distinct regions in fine‑tuned hidden states.
- This separation suggests identity knowledge can be suppressed while preserving general visual perception.
- AIM achieves competitive identity forgetting on the same images as it retains non‑deleted identities, prior knowledge, and visual perception.

## Context
MLLMs often memorize personal data during fine‑tuning, raising privacy concerns. Existing unlearning methods require access to retained artifacts, which is unrealistic in many practical scenarios. This work explores identity unlearning when such artifacts are unavailable.

## Implications
The findings show that identity knowledge can be decoupled from visual perception in MLLM representations. Practitioners can adopt similar anchoring techniques to meet deletion regulations without sacrificing model utility or performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28312v1)
