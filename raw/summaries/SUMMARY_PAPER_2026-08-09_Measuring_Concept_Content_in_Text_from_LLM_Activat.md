---
title: Measuring Concept Content in Text from LLM Activations: ESG Evidence from Concept Vectors and Linear Probes
url: http://arxiv.org/abs/2608.07208v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_13-21-50Z_MeasuringConceptContentinTextfromLLMActivations_ES.md
generated_at: 2026-08-09 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether the internal activations of a frozen LLM can serve as an alternative to task‑specific fine‑tuning for measuring concept content in text, using financial ESG data. It compares two extraction methods — Recursive Feature Machine (RFM) vectors and linear probes — against surface baselines and the model’s own answer, finding that a simple linear probe achieves accuracy within 0.6 points of a fine‑tuned domain classifier without any fine‑tuning and outperforms the model’s self‑generated response in eleven out of twelve comparisons.

## Key Takeaways
- The internal activations reveal a knowledge gap: the model knows about ESG concepts even though its surface output does not explicitly mention them.  
- Linear probing provides a continuous score that better reflects concept presence than RFM vectors, which only yield classification‑level outputs.  
- The best probe’s performance matches that of a fine‑tuned classifier without any task‑specific training, demonstrating the utility of activation monitoring.

## Context
Current AI research focuses on surface representations such as word embeddings and topic proportions to gauge concept relevance. However, these methods ignore latent knowledge stored in model activations, which may be more aligned with human judgments. This work extends that discussion by showing that frozen‑model activations can capture deeper understanding without additional training.

## Implications
For practitioners, monitoring activations offers a low‑cost way to assess whether an LLM truly grasps domain concepts like ESG factors, potentially improving compliance and reporting accuracy. In industry, this could enable automated audits of model behavior without costly fine‑tuning pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07208v1)
