---
title: Offline-to-Online Creative Optimization with Generative Models and Adaptive Testing
url: http://arxiv.org/abs/2607.23696v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_14-45-15Z_Offline_to_OnlineCreativeOptimizationwithGenerativ.md
generated_at: 2026-07-27 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes an offline‑to‑online workflow that leverages generative models and a predictive model to create and rank creative variants for A/B testing. In a field experiment with 50 arms the method produced a best creative that outperformed human authors by up to 46 % engagement, demonstrating that predictive guidance can yield high‑performing candidates despite noisy offline predictions.

## Key Takeaways
- The workflow uses historical A/B test data to train a predictive model that ranks generative variants, allowing generation of a limited slate for online testing.  
- Although the predictive model is too noisy to pinpoint the single best creative offline, it steers the generator toward strong candidates that can be evaluated efficiently in an adaptive experiment.  
- The method reduces traffic loss by selecting promising arms early, achieving lifts of 45.1 %, 46.7 % and 36.2 % across three experiments.

## Context
Creative optimization traditionally relies on costly online evaluations that limit the number of tested variants. Generative AI can produce many plausible creatives, but without a reliable offline signal, only a small batch is tested, leading to suboptimal results. This work bridges the gap by using offline predictive signals to guide generation, aligning with broader trends in AI‑assisted decision making.

## Implications
Practitioners can adopt this approach to generate larger, higher‑quality creative slates without increasing experiment cost. The design principle of using a noisy but informative predictor to steer generative models could be applied across marketing, product testing and any scenario where offline data informs online selection.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23696v1)
