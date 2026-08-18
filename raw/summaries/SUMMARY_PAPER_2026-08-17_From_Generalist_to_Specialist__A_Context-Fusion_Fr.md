---
title: From Generalist to Specialist: A Context-Fusion Framework for Endoscopic Polyp Reporting with a Frozen VLM
url: http://arxiv.org/abs/2608.15580v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_07-11-00Z_FromGeneralisttoSpecialist_AContext_FusionFramewor.md
generated_at: 2026-08-17 21:33
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a context-fusion framework that specializes a frozen general-purpose vision-language model for endoscopic polyp reporting without altering its pretrained weights. By combining implicit instruction tokens with explicit transduction evidence retrieved from a self-supervised encoder, the method improves both unified reporting and specialist performance while adding minimal trainable parameters.

## Key Takeaways
- The framework corrects 70.5% of errors made by weight-adaptation baselines when the top‑1 retrieved case matches the target category.
- It adds only 0.006% of the frozen VLM’s parameter count as trainable, demonstrating high adaptation efficiency.
- Across numerical, categorical, and report‑generation metrics, the approach outperforms general‑purpose VLMs, task‑specific predictors, and weight‑adaptation methods.

## Context
Vision‑language models have become powerful for multimodal tasks but often require costly fine‑tuning or weight updates to specialize. This work shows that lightweight, parameter‑efficient adaptation can be achieved through context fusion, preserving the model’s universal capabilities while injecting domain expertise.

## Implications
Clinicians and developers can deploy highly accurate endoscopic reports using a single frozen VLM with minimal computational overhead. The method offers a scalable template for other medical imaging specializations where fine‑tuning is impractical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15580v1)
