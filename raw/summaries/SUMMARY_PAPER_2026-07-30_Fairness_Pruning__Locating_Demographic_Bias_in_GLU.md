---
title: Fairness Pruning: Locating Demographic Bias in GLU-MLP Layers via Differential Activations
url: http://arxiv.org/abs/2607.28319v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_14-54-33Z_FairnessPruning_LocatingDemographicBiasinGLU_MLPLa.md
generated_at: 2026-07-30 20:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Fairness Pruning, a lightweight method for locating and mitigating demographic bias in GLU-MLP layers of large language models. By capturing differential activations at the down_proj input, it zeroes out neurons that react differently to demographic attributes, showing that such interventions can reduce bias while preserving model capabilities.

## Key Takeaways
- The method identifies neurons that exhibit opposite responses to demographic cues, and zeroing them causes bidirectional bias destabilization because BiasScore is unsigned. - It achieves mitigation with only 40 neurons removed from Llama-3.2-1B, less than 0.031% of total width, retaining 99.49% reasoning performance. - The results confirm that bias processing and general knowledge operate on separate circuits.

## Context
Large language models increasingly exhibit demographic bias, prompting research into fine‑grained interventions that preserve functionality. This work contributes a surgical approach to bias mitigation that does not require retraining or large-scale zeroing of layers.

## Implications
Practitioners can now target specific neurons for bias reduction without sacrificing model utility, enabling more precise fairness tuning. The findings support the shift from blanket pruning toward targeted, direction‑aware interventions in LLM deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28319v1)
