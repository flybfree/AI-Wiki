---
title: Beyond Naturalness: Probing Automated Text-To-Speech Evaluators on Linguistically Grounded Dimensions
url: http://arxiv.org/abs/2608.09930v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_17-59-51Z_BeyondNaturalness_ProbingAutomatedText_To_SpeechEv.md
generated_at: 2026-08-10 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how automated TTS evaluation methods align with human perception by decomposing naturalness into ten linguistically grounded perceptual dimensions and creating a benchmark dataset of 860 utterances annotated by trained linguists. The study shows that Mean Opinion Score predictors focus mainly on acoustic quality, while Audio-LLM judges detect speech errors selectively based on prompt wording and do not generalize across all dimensions.

## Key Takeaways
- MOS predictors collapse onto acoustic signal quality, indicating they ignore linguistic aspects of naturalness.
- Audio‑LLM judges exhibit selective detection that varies with the evaluation prompt rather than providing a consistent assessment.
- Neither class reliably captures the full range of linguistically structured speech errors present in the benchmark.

## Context
The research addresses a longstanding gap in TTS evaluation where automated tools often treat all perceived flaws as equivalent, overlooking subtle linguistic cues. This work contributes to more nuanced AI systems that understand how humans actually listen and perceive speech quality.

## Implications
For practitioners, this study suggests moving beyond single‑dimensional scores toward multi‑dimensional benchmarks that reflect real perceptual complexity. Industry adoption of such benchmarks could lead to TTS products that better match human expectations across diverse linguistic contexts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09930v1)
