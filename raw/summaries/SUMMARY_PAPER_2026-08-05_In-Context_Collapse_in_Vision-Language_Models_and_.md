---
title: In-Context Collapse in Vision-Language Models and How to Mitigate it?
url: http://arxiv.org/abs/2608.02830v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-03_19-44-45Z_In_ContextCollapseinVision_LanguageModelsandHowtoM.md
generated_at: 2026-08-05 01:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates a surprising phenomenon called in‑context collapse that occurs when vision‑language models receive many demonstration pairs for few‑shot learning. The authors demonstrate that instead of improving with more examples, some models experience a sharp drop in performance, sometimes falling below chance while still producing syntactically correct outputs. They identify the failure as an integration problem at the vision‑language interface and propose a lightweight fix called CircA.

## Key Takeaways
- In‑context collapse is a graded degradation across synthetic classification, natural image classification, and VQA tasks for VLMs ranging from 0.5B to 11B parameters and even in Claude Sonnet 4.5.  
- The phenomenon is caused by the interaction between robustness to accumulating demonstrations and the ability to learn a novel rule, producing three distinct regimes that can be observed independently.  
- A lesion‑and‑rescue experiment shows that adding an adapter on the early/mid connector layers restores learning (accuracy jumps from 0.39 to 0.91 with 16 shots) whereas an equal‑capacity readout adapter does not.

## Context
The rise of few‑shot vision‑language models has driven expectations for seamless adaptation without fine‑tuning, yet this work reveals a hidden instability that can undermine performance. Understanding the root cause in the integration pathway is crucial because it affects how models generalize across diverse tasks and datasets.

## Implications
For practitioners, this research suggests that simple readout modifications may be more effective than full model retraining to prevent catastrophic forgetting during inference‑driven adaptation. Industry adoption of lightweight interventions like CircA could lead to more reliable deployment of VLM systems in real‑world applications where consistent accuracy is essential.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02830v1)
