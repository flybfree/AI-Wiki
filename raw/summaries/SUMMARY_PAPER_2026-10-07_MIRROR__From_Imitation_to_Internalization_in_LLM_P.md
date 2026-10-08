---
title: MIRROR: From Imitation to Internalization in LLM Personalization
url: http://arxiv.org/abs/2610.09795v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-07_10-10-01Z_MIRROR_FromImitationtoInternalizationinLLMPersonal.md
generated_at: 2026-10-07 21:15
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
The paper introduces MIRROR (Meta-personalization by Internalizing Reference-Revealed On-policy Reflections), a self-distillation framework that shifts LLM personalization away from surface-level style imitation toward deeper preference internalization. By aligning a model's next-token distributions along its own generation trajectories with those of its reference-conditioned self, MIRROR enables models to internalize user preferences rather than merely reproducing reference wording. The framework, including its focal plug-in MIRROR-F, achieves leading personalization performance and superior text quality across multiple benchmarks while reducing catastrophic forgetting compared to supervised fine-tuning baselines.

## Key Takeaways
- MIRROR replaces traditional reference-token imitation with reference-revealed on-policy self-distillation, meaning the model learns from its own generated trajectories rather than copying reference text verbatim. This shifts the alignment target from reproducing specific wording to matching distributional preferences, allowing the model to internalize what a user values in content rather than mimicking how a reference expresses it.
- The MIRROR-F focal plug-in augments the on-policy distributional alignment with selective supervision over informative reference tokens, which strengthens content generation quality while preserving user-specific expression. This addresses a key tension in personalization: maintaining individual voice while improving substantive output quality.
- Across three personalized generation benchmarks, two model scales, and both reference-based and LLM-based evaluation methods, MIRROR and MIRROR-F demonstrate consistent gains in overall personalization performance and text quality. Critically, they exhibit less catastrophic forgetting than SFT-based baselines on three unseen personalized generation tasks, suggesting the internalization approach generalizes more robustly than imitation-based fine-tuning.

## Context
The broader AI landscape is witnessing a paradigm shift in personalization research, moving from superficial style matching toward content-aware adaptation that respects user intent and quality expectations. Existing fine-tuning paradigms often rely on supervised imitation of reference outputs, which can entangle style with substance and lead to brittle generalization. MIRROR addresses this gap by leveraging self-distillation—a technique already proven in knowledge distillation and reinforcement learning—to create a more principled pathway for embedding user preferences into model parameters without overfitting to specific reference phrasings.

## Implications
For practitioners building personalized LLM applications, MIRROR offers a training paradigm that reduces the risk of catastrophic forgetting, a persistent problem when adapting models to individual users without degrading general capability. The consistency of gains across model scales and application scenarios suggests this approach is practical for deployment in diverse settings, from consumer assistants to domain-specific tools. Industry teams can expect improved content quality and more faithful preference adherence without the computational overhead of maintaining multiple reference-conditioned models, making scalable personalization more feasible.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.09795v1)
