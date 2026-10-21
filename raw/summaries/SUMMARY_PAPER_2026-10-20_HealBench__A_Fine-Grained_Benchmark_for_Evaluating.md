---
title: HealBench: A Fine-Grained Benchmark for Evaluating Psychological Comfort in Text-to-Image Generation
url: http://arxiv.org/abs/2610.27516v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-20_02-31-31Z_HealBench_AFine_GrainedBenchmarkforEvaluatingPsych.md
generated_at: 2026-10-20 22:55
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces HealBench, a fine-grained benchmark of 30,000 high-quality image-text pairs designed to evaluate whether text-to-image generation outputs feel psychologically comforting to viewers, a dimension largely ignored by existing benchmarks focused on photorealism, semantic fidelity, and aesthetics. Grounded in cognitive evaluation theory, the authors define psychological comfort as an affective response shaped by restorative and emotionally supportive visual cues, and demonstrate through evaluations of 14 image generation models that strong semantic alignment and aesthetic quality do not guarantee emotionally restorative outputs. The work further shows that a learned reward signal, HealScorer, can be used in reinforcement learning to improve the emotional and restorative quality of generated images.

## Key Takeaways
- HealBench comprises 30,000 image-text pairs spanning 19 categories and 92 subcategories, curated from 100,000 candidates through a multi-stage pipeline involving vision-language model matching, human preference models, expert filtering, and exemplar-guided augmentation, establishing a rigorous and reproducible foundation for affect-aware evaluation in generative image research.
- Evaluations across 14 representative image generation models and prompt-rewriting strategies reveal a measurable gap between conventional visual quality metrics and perceived psychological comfort, indicating that current models optimize for technical fidelity while failing to produce images that viewers find emotionally restorative or supportive.
- The authors introduce HealBench-Eval, a feature-clustered evaluation set of 1,095 instances, and demonstrate that reinforcement learning guided by HealScorer as a reward signal can measurably improve the emotional and restorative quality of generated images, positioning psychological comfort as a trainable and optimizable objective rather than a subjective afterthought.

## Context
Text-to-image generation has advanced rapidly in photorealism, prompt adherence, and aesthetic scoring, yet the human-centered question of whether generated images evoke feelings of calm, restoration, or emotional support remains largely unaddressed in benchmarking literature. By grounding psychological comfort in cognitive evaluation theory and constructing a large-scale, expert-curated benchmark, HealBench fills a critical gap between technical image quality assessment and affective human experience, extending the evaluation paradigm of generative models into the domain of emotional well-being and therapeutic visual design.

## Implications
For practitioners in generative AI, this work signals that optimizing for semantic accuracy and visual aesthetics alone is insufficient for applications in mental health, wellness content creation, therapeutic environments, and user-facing creative tools where emotional resonance is paramount. Industry stakeholders in healthcare, education, and digital wellness platforms can leverage HealBench and HealScorer to build affect-aware generative pipelines that prioritize restorative visual outcomes, while researchers gain a standardized benchmark and reward-signal framework to drive the next generation of emotionally intelligent image generation models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.27516v1)
