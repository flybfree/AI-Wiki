---
title: NegT2IBench: When Negation Changes the Picture. A Polarity Benchmark for Text-to-Image Models
url: http://arxiv.org/abs/2610.03084v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-02_10-03-56Z_NegT2IBench_WhenNegationChangesthePicture_APolarit.md
generated_at: 2026-10-04 21:47
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
NegT2IBench introduces a benchmark of 4,800 prompts designed to evaluate whether text-to-image models can correctly satisfy negated constraints, such as generating "a non-red cup," rather than only confirming that requested content appears. The authors find that across eleven T2I models and 211,200 generated images, nine models score lower on a single negated statement than on a single positive one, revealing that rendering what a prompt asks for and withholding what it forbids are fundamentally distinct capabilities that existing compositional benchmarks fail to separate.

## Key Takeaways
- The benchmark is structured by polarity, independently varying the number of positive statements (0 to 2) and negated statements (0 to 2) across two attribute types and four relation categories. This design isolates the effect of negation from the effect of prompt complexity, enabling controlled diagnosis of where models fail specifically due to negation rather than general compositional difficulty.
- The detector-based scoring system is reproducible, auditable, and pinpoints which specific requirement failed. Validated on 600 images with three-annotator labels, it agrees with human judgments as closely as vision-language judges up to 30 times larger while consuming only a fraction of their GPU memory, making it a practical and scalable evaluation tool.
- Per-statement analysis reveals that negation failures are largest for color attributes and near zero for proximity relations, and that 41.5% of failed statements cause the model to render exactly what the prompt forbids. This suggests models do not simply ignore negation but actively produce the prohibited content, pointing to a representational failure rather than a mere omission.

## Context
Existing text-to-image benchmarks such as T2I-CompBench and GenEval measure compositional accuracy by checking whether requested objects, attributes, and spatial relations appear in generated images. However, they largely ignore the complementary ability to exclude content, a capability critical for safety filtering, brand compliance, and user intent adherence. NegT2IBench fills this gap by providing a controlled testbed that separates negation handling from general prompt-following, addressing a blind spot in the evaluation ecosystem for generative models.

## Implications
For practitioners deploying T2I systems in commercial settings—advertising, product design, content moderation—the inability to reliably honor negated constraints means generated outputs may violate explicit user or regulatory requirements, creating legal and brand-safety risks. The finding that models actively render forbidden content rather than merely omitting it suggests that current training objectives and architectures do not adequately represent exclusionary semantics, motivating new training strategies, negative-prompt conditioning methods, and evaluation pipelines that explicitly test what a model must not produce.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.03084v1)
