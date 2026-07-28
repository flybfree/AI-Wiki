---
title: BioSentinel at EXIST 2026: Soft-Label Optimization with XLM-RoBERTa for Sexism Intent Classification in Memes
url: http://arxiv.org/abs/2607.24137v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_08-18-05Z_BioSentinelatEXIST2026_Soft_LabelOptimizationwithX.md
generated_at: 2026-07-27 23:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The BioSentinel team participated in the EXIST 2026 Task 2.2 Source Intention classification of memes, aiming to detect sexist intent among three categories: direct, judgemental, or non‑sexist. Their model leverages xlm‑roberta‑base and a composite loss that blends KL divergence for soft‑label distributions with weighted cross‑entropy for hard labels, achieving an ICM‑Soft‑Norm of 0.3229 and ranking 40th out of 118 submissions in the soft‑soft evaluation.

## Key Takeaways
- The KL component of the loss function enhances the model’s ability to predict a smooth probability distribution over annotator disagreements, thereby improving soft‑label performance.
- Weighted cross‑entropy contributes specifically to higher hard‑label accuracy, as measured by the 0.4236 F1 score on the official test set.
- The analysis reveals that dataset characteristics and the degree of annotator disagreement directly influence model architecture choices for subjective NLP tasks.

## Context
This work addresses a growing need in AI research for methods that handle ambiguous, human‑annotated data where multiple experts may disagree. By integrating soft labels with hard labels within a Le‑Wi‑Di framework, the study exemplifies how ensemble prediction can be optimized for both consistency and accuracy in subjective classification tasks.

## Implications
For practitioners, the findings suggest that incorporating KL loss is beneficial when annotator variance is high, while cross‑entropy remains essential for precise target prediction. The results also highlight the importance of evaluating models on both soft and hard metrics to capture the full spectrum of performance in real‑world deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24137v1)
