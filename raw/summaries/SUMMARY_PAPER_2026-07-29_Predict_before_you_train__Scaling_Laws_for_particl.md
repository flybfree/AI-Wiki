---
title: Predict before you train: Scaling Laws for particle physics foundation models
url: http://arxiv.org/abs/2607.23377v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-25_21-46-48Z_Predictbeforeyoutrain_ScalingLawsforparticlephysic.md
generated_at: 2026-07-29 23:01
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a method to forecast the performance of particle physics foundation models before they are trained, using scaling laws derived from small‑scale experiments. The authors fit a joint model‑and‑data scaling law across three orders of magnitude in training compute and then apply it to predict loss for larger models. Their forecasts align closely with downstream physics metrics such as tagging accuracy and quark/gluon rejection.

## Key Takeaways
- A single fitting curve can forecast the loss of models trained with up to one hundred times more compute, accurate within one percent.  
- Lower pretraining loss consistently leads to lower fine‑tuning loss and higher background rejection on two tagging benchmarks.  
- The predicted performance matches published state‑of‑the‑art results across accuracy, AUC, and purity tails.

## Context
Particle physics relies heavily on large transformer models that are costly to train yet crucial for extracting physical insights from data. Traditional scaling laws describe behavior within a single model family but cannot bridge the gap between small experiments and future large systems. This work bridges that gap by providing a universal forecast tool.

## Implications
Researchers can allocate compute budgets with confidence about expected physics outcomes, reducing wasted effort on underperforming models. Practitioners gain a practical framework to prioritize training resources toward higher‑impact performance gains in real‑world experiments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23377v1)
