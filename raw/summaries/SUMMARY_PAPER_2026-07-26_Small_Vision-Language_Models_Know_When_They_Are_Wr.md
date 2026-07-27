---
title: Small Vision-Language Models Know When They Are Wrong But Cannot Say So: A Two-Model Study of Stated versus Internal Confidence Under Realistic Image Degradation
url: http://arxiv.org/abs/2607.22034v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-24_07-00-32Z_SmallVision_LanguageModelsKnowWhenTheyAreWrongButC.md
generated_at: 2026-07-26 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether small vision-language models can detect errors in degraded images and whether their stated confidence reflects that knowledge. It compares verbalized confidence with internal token probability across six degradations, finding a large gap: verbal confidence is unreliable while internal probability works well. The study concludes that internal signals are better for deferral.

## Key Takeaways
- Verbalized confidence from Qwen2-VL remains near 0.87–0.90 and detects errors only at chance level (AUROC ~0.5).  
- Internal token probability separates correct from incorrect answers with high AUROC (0.92–0.99) across all conditions.  
- Under severe underexposure both confidence signals stay flat while accuracy drops sharply, indicating internal error detection also fails at chance.

## Context
Vision-language models deployed on consumer devices must provide reliable uncertainty cues to avoid harmful outputs when images are compressed or poorly lit. This study highlights that small open-weight VLMs encode self‑knowledge in their token probabilities but fail to translate it into natural language confidence. The findings underscore a gap between model introspection and user‑facing signals.

## Implications
For practitioners, relying on verbalized confidence can lead to false confidence and unsafe deferral decisions, especially in low‑light scenarios. Integrating internal probability as a fallback metric is advisable for robust deployment of small VLMs where accuracy may degrade but uncertainty must be signaled accurately.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22034v1)
