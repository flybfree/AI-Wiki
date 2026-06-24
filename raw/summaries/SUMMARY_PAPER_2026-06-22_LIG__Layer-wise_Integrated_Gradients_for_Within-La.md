---
title: "Summary: LIG: Layer-wise Integrated Gradients for Within-Layer Flow Analysis in Transformers"
url: http://arxiv.org/abs/2606.21564v1
type: paper-summary
date: 2026-06-22
source_paper: 2026-06-19_16-02-22Z_LIG_Layer_wiseIntegratedGradientsforWithin_LayerFl.md
generated_at: 2026-06-22 21:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces LIG, a method for analyzing within‑layer flow in Transformers using set‑to‑set Integrated Gradients across module boundaries, achieving agreement with layer‑whole attribution and revealing token‑to‑token contributions without retraining.

## Key Takeaways
- LIG applies set‑to‑set IG to map from input tokens to output representations at attention and MLP boundaries, evaluating token‑to‑token contributions.
- It composes within‑layer contributions while conserving total gradient via an L2 scalarization, similar to Layer‑wise Relevance Propagation.
- Experiments on BERT‑base show best consistency when using embedding as ATT baseline and either zero or ATT output at a=0 as MLP baseline.

## Context
Understanding internal attention flows is crucial for XAI; prior methods treat each layer as a black box. LIG provides a diagnostic tool that works across models without fine‑tuning, aligning with demand for interpretable AI.

## Implications
Practitioners can diagnose why certain layers dominate attribution, improving model debugging and trust. This supports responsible deployment by offering transparent insights into attention mechanisms.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.21564v1)
