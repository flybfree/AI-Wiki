---
title: Text Capability Loss in Vision-Language Adaptation: An Attention-Sink Diagnosis
url: http://arxiv.org/abs/2609.00746v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_05-24-37Z_TextCapabilityLossinVision_LanguageAdaptation_AnAt.md
generated_at: 2026-09-01 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
Fine‑tuning a pretrained language model into a vision‑language model (VLM) often degrades its ability to follow strict output rules such as instruction following or chain‑of‑thought reasoning. The authors attribute this loss to “attention‑sink corruption,” where fine‑tuning perturbs the early sink position that normally anchors most of the attention probability, and they introduce Sink Strength—a single scalar computed on the base LLM—that predicts post‑VL degradation without any VL training.

## Key Takeaways
- Attention sink position perturbation concentrates the damage on tasks requiring exact output rules, indicating a loss in fine‑grained reasoning.  
- The scalar Sink Strength consistently tracks relative degradation across six VLM‑LLM pairs and multiple format‑sensitive tasks, offering an early diagnostic tool.  
- QK‑RMSNorm injection does not replicate the protection of native QK‑RMSNorm, and many off‑the‑shelf weight‑merging settings fail to recover lost capability after VL training.

## Context
The paper addresses a growing challenge in multimodal AI: preserving core language capabilities when models are adapted for vision tasks. Attention mechanisms act as “sinks” that route most of the model’s focus, and any disruption can impair downstream performance. Understanding these sinks helps researchers design more robust adaptation pipelines.

## Implications
Screening backbones with Sink Strength before VL training narrows the space of viable interventions, encouraging head‑selective or training‑time protections rather than post‑hoc fixes. This insight can guide industry practitioners to maintain high‑quality language performance across multimodal applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00746v1)
