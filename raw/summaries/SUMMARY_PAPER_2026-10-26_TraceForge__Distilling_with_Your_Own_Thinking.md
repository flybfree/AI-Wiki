---
title: TraceForge: Distilling with Your Own Thinking
url: http://arxiv.org/abs/2610.29680v2
type: paper-summary
date: 2026-10-26
source_paper: 2026-10-21_12-57-29Z_TraceForge_DistillingwithYourOwnThinking.md
generated_at: 2026-10-26 11:33
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
TraceForge proposes a method for generating synthetic reasoning traces in the style of a target model family, enabling knowledge distillation from frontier LLMs whose providers restrict access to detailed reasoning chains. The approach uses a two-stage training pipeline—a supervised generator followed by an adversarial critic—to produce reasoning traces that closely mimic authentic model outputs, achieving authenticity scores comparable to or exceeding real traces. On coding benchmarks, the generated reasoning traces outperform the teacher model's own thinking content, yielding measurable improvements on HumanEval+ and MBPP+.

## Key Takeaways
- Frontier model providers increasingly restrict access to detailed reasoning traces, returning only final answers or short summaries. While recent work attempts to recover hidden reasoning by replaying encrypted blocks across models, this approach violates providers' terms of service and is not viable for long-term product development, creating a practical bottleneck for distillation pipelines.
- TraceForge's two-stage training involves a generator that learns to regenerate reasoning traces in the student model's own family style from a given context and teacher answer, followed by an adversarial critic that evaluates how realistic a reasoning trace appears. An independent judge scores trace authenticity on a 0-to-1 scale: generated traces average 0.68, real traces score 0.66, and critic-selected traces from four candidates reach 0.82, demonstrating the method produces traces indistinguishable from genuine ones.
- On coding benchmarks with identical 5,000 questions and teacher answers, HumanEval+ improves by 3.7 points and MBPP+ by 7.1 points at the final checkpoint, with the MBPP+ advantage sustained across every checkpoint. The authors hypothesize that reasoning written in the student's own family style is more learnable for that model, explaining the performance gains over using the teacher's native reasoning content.

## Context
Knowledge distillation from large language models has become a foundational technique for training smaller or specialized models, and it has historically relied on transferring detailed reasoning traces from teacher models to students. As frontier labs tighten API terms and obscure their internal reasoning chains, the community faces a growing gap between the need for rich training data and the availability of authentic reasoning content. TraceForge addresses this gap by shifting the burden of trace generation to the student side, making distillation feasible even when the teacher's internal thought process is inaccessible.

## Implications
For practitioners building products on top of frontier APIs, TraceForge offers a terms-of-service-compliant pathway to distill reasoning capability without violating provider restrictions, potentially unlocking training pipelines that were previously blocked by licensing constraints. The finding that family-style reasoning traces outperform the teacher's own thinking content suggests a broader principle for model training: data fidelity to the learner's inductive biases may matter more than data fidelity to the source model, which could reshape how synthetic training data is generated across the industry.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.29680v2)
