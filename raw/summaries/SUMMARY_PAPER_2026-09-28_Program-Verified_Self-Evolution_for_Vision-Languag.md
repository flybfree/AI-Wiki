---
title: Program-Verified Self-Evolution for Vision-Language Models
url: http://arxiv.org/abs/2609.33855v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-27_19-13-38Z_Program_VerifiedSelf_EvolutionforVision_LanguageMo.md
generated_at: 2026-09-28 23:30
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces Verifiable QA Generation for Self-Evolving Models (VQS), a method to improve the reliability of self-evolving vision-language models by replacing error-prone majority voting with program-verified answer generation. VQS leverages structured image parsing into records like scene graphs, allowing fixed programs to compute answers while the model verifies individual factual claims, resulting in significantly higher label accuracy and sustained performance gains across multiple training rounds.

## Key Takeaways
- Prior self-evolution methods rely on majority vote or model judges to label questions generated from unlabeled images, but human evaluation reveals significant error rates, with 24% of majority-vote labels and 18% of model-judge labels found to be incorrect.
- VQS changes the judgment process by having the model parse images into structured records such as scene graphs or chart tables; fixed programs then write questions and compute answers from these records, while the model acts as a visual checker that validates individual claims rather than voting on final answers.
- Human raters confirm 94% accuracy for VQS-generated answers compared to 76% for majority voting, and the method improves Qwen3-VL performance by up to 3.18 points across ten benchmarks at 2B, 4B, and 8B scales, with gains compounding over three training rounds to reach a 3.84-point improvement at the 2B scale.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.33855v1)
