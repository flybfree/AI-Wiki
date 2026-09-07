---
title: When Do Internal Probes Beat Reading the Answer? Miscalibrated Readouts and Behavior-Concealed Knowledge in Language Models
url: http://arxiv.org/abs/2609.04582v1
type: paper-summary
date: 2026-09-06
source_paper: 2026-09-04_00-26-45Z_WhenDoInternalProbesBeatReadingtheAnswer_Miscalibr.md
generated_at: 2026-09-06 21:32
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates why a modest language model can mislead both behavior and internal probing despite having accurate hidden‑state representations. It discovers that the discrepancy stems from a single scalar offset in the decision threshold, which erases the correct verdict in generated outputs while leaving probe scores intact. The analysis generalizes across many configurations, showing that behavioral accuracy collapses to a function of this offset, whereas margin ranking remains stable.

## Key Takeaways
- A 0.6B model answers YES to all logical conclusions because its output logits are saturated at a threshold shifted by +4.6 sigma, erasing the true verdict even though linear probes on hidden states achieve high AUC.
- Across 90 semantic‑label configurations, behavioral accuracy follows a single function of the threshold offset (Spearman -0.93), indicating that miscalibration is the dominant failure mode rather than complex knowledge loss.
- In a maze task with no surface cues, the audit correctly identifies a concealed regime where internal probes succeed but behavior fails, revealing three distinct regimes: concealed, miscalibrated, and undetected.

## Context
Understanding how language models encode and retrieve knowledge is crucial for reliable AI systems. This work highlights that model performance can be decoupled from its output, making standard evaluation metrics insufficient to gauge true understanding. The findings prompt a reevaluation of calibration techniques in large‑scale generative models.

## Implications
For practitioners, correcting the threshold offset can restore behavioral accuracy without retraining the entire network, offering an efficient fix for miscalibrated outputs. This insight is valuable across industries that rely on model confidence, such as medical diagnosis and content moderation, where both probe scores and generated text must align with ground truth.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04582v1)
