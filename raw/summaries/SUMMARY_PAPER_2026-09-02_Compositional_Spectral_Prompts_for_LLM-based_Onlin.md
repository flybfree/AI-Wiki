---
title: Compositional Spectral Prompts for LLM-based Online Time Series Forecasting
url: http://arxiv.org/abs/2609.02093v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_04-34-04Z_CompositionalSpectralPromptsforLLM_basedOnlineTime.md
generated_at: 2026-09-02 20:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CoSPOT, an LLM‑based online time series forecasting framework that addresses the limitations of memory‑buffer approaches in adapting to non‑stationary data. By freezing the LLM and using compositional spectral prompts derived from frequency‑domain bases, CoSPOT enables efficient adaptation with minimal parameter updates while preserving strong few‑shot performance.

## Key Takeaways
- CoSPOT leverages a frozen pre‑trained LLM as the forecaster, reducing computational cost compared to fine‑tuning.  
- The method composes spectral basis prompts according to time series amplitudes, allowing unseen patterns to be expressed as novel prompt combinations.  
- Extensive experiments on real‑world datasets show CoSPOT outperforms baseline methods in extended online phases and cross‑dataset settings with large distribution shifts.

## Context
Online time series forecasting remains a critical challenge for AI systems that must continuously learn from streaming data without retraining the entire model. This work contributes to the growing trend of using language models as versatile function approximators, highlighting their potential beyond static classification tasks.

## Implications
CoSPOT demonstrates that frozen LLMs can be steered by structured prompts, offering a scalable solution for real‑time forecasting applications such as finance and IoT monitoring. Practitioners can adopt this approach to maintain model performance while conserving resources and avoiding catastrophic forgetting.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02093v1)
