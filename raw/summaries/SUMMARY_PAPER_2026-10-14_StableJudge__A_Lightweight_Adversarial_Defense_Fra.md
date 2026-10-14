---
title: StableJudge: A Lightweight Adversarial Defense Framework for LLM-as-a-Judge
url: http://arxiv.org/abs/2610.16814v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-12_14-00-13Z_StableJudge_ALightweightAdversarialDefenseFramewor.md
generated_at: 2026-10-14 01:14
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
StableJudge addresses the vulnerability of LLM-as-a-Judge pipelines to score-hijacking prompt injection attacks embedded in evaluated content, which corrupt scoring signals and distort downstream rankings. The authors propose a lightweight defense framework that decouples safety from the judge model itself by introducing a compact 0.13B parameter "Sentry" model that localizes and sanitizes injected spans before evaluation, achieving robust judging without requiring modifications to the underlying judge model.

## Key Takeaways
- StableJudge externalizes prompt-injection mitigation as a reusable pre-scoring capability rather than embedding defenses into the judge model itself. This architectural choice means that when a judge model is updated, replaced, or scaled, the defense layer remains intact and transferable, eliminating the need to retrain or reconfigure safety mechanisms with every model swap. The Sentry component operates as a standalone 0.13B model that identifies adversarially injected spans in input text and performs targeted sanitization before the judge ever sees the content.
- The defense is trained using adversarially evolving attacks rather than a fixed set of prompt templates, enabling the Sentry to generalize beyond the specific injection patterns it was trained on. This adversarial training strategy improves robustness against out-of-distribution attack variants, as demonstrated on held-out scientific abstracts and unseen injection strategies, showing that the framework does not merely memorize known attack patterns but learns transferable detection and sanitization behavior.
- StableJudge stabilizes measurement by deriving deterministic, fine-grained scalar scores from the judge's output distribution rather than relying on single-pass scoring. This approach reduces variance in scoring outcomes and improves score recovery under attack conditions while largely preserving the judge's general-purpose evaluation performance, demonstrating that robustness gains do not come at the cost of baseline accuracy.

## Context
As LLMs become increasingly embedded in automated evaluation pipelines for academic peer review, content moderation, and recommendation systems, their susceptibility to adversarial prompt injection represents a critical reliability gap in production AI systems. Prior defense strategies have typically required modifying or retraining the judge model itself, coupling safety guarantees to a specific model's architecture and training data. StableJudge contributes to the broader research effort on modular, composable AI safety by demonstrating that adversarial robustness can be achieved through lightweight, model-agnostic defense layers that operate independently of the primary evaluation model.

## Implications
For practitioners deploying LLM-based scoring systems in academic publishing, content curation, or automated decision-making, StableJudge offers a practical path to hardened evaluation pipelines without the cost and complexity of retraining or fine-tuning large judge models. The framework's emphasis on decoupling safety from judge scale suggests that organizations can upgrade or swap their underlying LLM judges freely while maintaining consistent adversarial defenses, reducing operational overhead and enabling safer adoption of LLM-as-a-Judge in high-stakes evaluation workflows. The release of code and data further supports reproducibility and community-driven extension of the defense approach.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.16814v1)
