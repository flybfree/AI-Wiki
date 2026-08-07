---
title: Bias Analysis of L2 Speaking Assessment Systems Using Concept Activation Vectors
url: http://arxiv.org/abs/2608.06300v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_17-20-58Z_BiasAnalysisofL2SpeakingAssessmentSystemsUsingConc.md
generated_at: 2026-08-06 23:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes extending Concept Activation Vectors to analyze bias in two L2 speaking assessment systems: a text-based BERT grader and a multimodal Whisper‑based grader. It shows that concept recoverability depends on model architecture and representation, not just the concept itself, and that sensitivity varies across layers.

## Key Takeaways
- Concept recovery is tied to how well CAVs can be mapped back to activation space, which varies by model design.
- Sensitivity metrics indicate whether a concept influences scores, but this effect is weaker in low‑dimensional layers of SAE‑based approaches.
- The study reveals that linear separability assumptions may not hold for complex neural embeddings, limiting straightforward bias detection.

## Context
Automatic L2 speaking assessment relies on deep learning models whose internal representations are opaque, raising fairness concerns. Concept Activation Vectors provide a tool to probe these models for unwanted attribute influence, but their applicability depends on the model’s architecture and representation space.

## Implications
Practitioners must consider both recoverability and sensitivity when auditing bias, as SAEs may hide subtle biases by smoothing activation signals. This distinction guides more reliable fairness evaluations in high‑stakes educational technology.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06300v1)
