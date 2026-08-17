---
title: Style or Signature? Artist-Disjoint Evaluation of Style Classification in Frozen Vision Embeddings
url: http://arxiv.org/abs/2608.14435v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_16-18-11Z_StyleorSignature_Artist_DisjointEvaluationofStyleC.md
generated_at: 2026-08-16 20:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper evaluates style classification in frozen vision embeddings under an artist‑disjoint protocol to determine whether models recognize artistic movements or individual artists. It reports a significant drop in 5‑nearest‑neighbor accuracy when works by the same painter appear on both sides of validation, from 0.87 to 0.77. The degradation is uneven across movements, with Surrealism suffering the largest loss.

## Key Takeaways
- Artist‑disjoint evaluation reveals that many classifiers succeed by recognizing the painter rather than the movement, indicating a lack of true style understanding.  
- The accuracy drop is pronounced for Surrealism (≈20 points) while Impressionism and Cubism change little, suggesting different levels of visual structure capture in each movement.  
- The effect persists across four image encoders, including vision‑only self‑supervised models, placing the issue in visual representation rather than textual language.

## Context
Frozen embeddings from large multimodal models like CLIP are widely used for art style classification, yet most studies rely on random splits that mix works by the same artist. This can inflate performance artificially and misrepresent model capabilities. The paper’s focus on a strict artist‑disjoint protocol provides a more honest benchmark for evaluating stylistic knowledge.

## Implications
For practitioners developing or deploying frozen embeddings, this work underscores the need to report results under conditions that prevent painter‑specific shortcuts. It also suggests that certain artistic styles may be less robustly encoded in visual features than others, guiding future research on improving style representation and evaluation fairness.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14435v1)
