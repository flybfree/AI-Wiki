---
title: EviSafe: Evidence-Grounded Safety Evaluation for Vision-Language Models
url: http://arxiv.org/abs/2608.23313v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_14-32-25Z_EviSafe_Evidence_GroundedSafetyEvaluationforVision.md
generated_at: 2026-08-24 21:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
EviSafe is a new framework that evaluates vision‑language model safety beyond simple refusal counts. It measures natural user responses, evidence grounding in visual and textual data, and how models handle counterfactual safety changes. The study uses an evidence‑aware judge to score models on these dimensions.

## Key Takeaways
- Natural severity accuracy ranges from 27.6% to 52.8%, indicating that most models fail to detect the correct level of risk in real scenarios.
- Relaxed diagnostic consistency varies between 6.1% and 29.3%, showing inconsistent handling of benign‑sensitive inputs across prompts.
- Unsafe‑to‑safe counterfactual transition success rates are only 30.4% to 58.4%, revealing limited ability to adapt safety behavior when evidence changes.

## Context
Current VLM benchmarks focus on final compliance decisions, which can mask unsafe reasoning that occurs earlier in the interaction. Such evaluations are needed as multimodal systems increasingly impact real‑world safety.

## Implications
This gap forces researchers and developers to adopt more nuanced evaluation methods beyond binary outputs in practice.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23313v1)
