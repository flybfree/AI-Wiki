---
title: Beyond Shallow Alignment: How Post-Training Methods Determine Refusal Circuits And Steering Robustness
url: http://arxiv.org/abs/2609.03887v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_14-10-17Z_BeyondShallowAlignment_HowPost_TrainingMethodsDete.md
generated_at: 2026-09-03 20:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how different post‑training alignment techniques shape the internal computation of refusals in large language models. It compares supervised fine‑tuning, reasoning‑augmented fine‑tuning and preference optimization across Llama‑3.1‑8B, Gemma‑2‑9B and Qwen3‑8B.

## Key Takeaways
- Reasoning‑augmented training creates a uniform refusal computation that is visible in all three models, indicating that the method influences internal pathways beyond data alone.
- No current post‑training method yields a safe alignment that simultaneously avoids fragile components, preserves general capability and allows small corrective edits.
- Architecture still matters for reliability of steering, showing that safety cannot be decoupled from model design.

## Context
Understanding the internal mechanisms behind refusal generation is crucial because it determines how robust safety can be in real‑world applications. The study highlights a gap between surface‑level alignment outcomes and deep architectural behavior.

## Implications
For practitioners, this suggests that relying solely on post‑training methods may leave security vulnerabilities unaddressed. Future work must integrate alignment with architectural stability to achieve trustworthy AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03887v1)
