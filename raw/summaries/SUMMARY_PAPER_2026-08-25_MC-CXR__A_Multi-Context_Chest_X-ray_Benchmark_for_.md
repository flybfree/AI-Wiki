---
title: MC-CXR: A Multi-Context Chest X-ray Benchmark for Context-Induced Disruption in Vision-Language Models
url: http://arxiv.org/abs/2608.24118v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_06-28-17Z_MC_CXR_AMulti_ContextChestX_rayBenchmarkforContext.md
generated_at: 2026-08-25 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MC‑CXR, a benchmark that tests vision‑language models on chest X‑rays when context such as text reports or prior images conflicts with the image. It shows that models often switch to incorrect predictions under misleading context, even if their image‑only decision is correct. The study evaluates ten VLMs and finds high rates of misalignment, especially with textual sources.

## Key Takeaways
- MC‑CXR creates 2,522 paired instances by fixing the image while varying reliable and misleading text or prior CXR, isolating context‑induced disruption.
- Switch‑to‑wrong rates are higher for misleading textual sources (45.6–78.1%) than for visual cues (35.7–61.7%), indicating a 57‑point gap in error alignment between the two types of context.
- Among switched predictions, only 17.6% align with the misleading label when visual context is wrong versus 74.6% for text, highlighting a strong asymmetry.

## Context
Vision‑language models are used in clinical settings where imaging must be interpreted alongside textual reports and prior scans. Existing benchmarks ignore how context can corrupt image‑only decisions, making it difficult to assess robustness under realistic interference.

## Implications
Clinicians and developers need reliable models that do not change their core diagnosis when irrelevant or misleading information is present. MC‑CXR provides a standardized way to measure this vulnerability, guiding safer deployment of AI in medical imaging workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24118v1)
