---
title: Test-Time Training for Modality Order Consistency in Vision-Language Models
url: http://arxiv.org/abs/2607.20351v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_16-37-02Z_Test_TimeTrainingforModalityOrderConsistencyinVisi.md
generated_at: 2026-07-23 23:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why vision-language models perform better when the image is presented before the question and proposes a test‑time training method that aligns both prompt orders. Experiments across three models and benchmarks show that image‑first prompting consistently beats question‑first, revealing a repeatable modality order failure. The proposed adaptation repairs this misalignment and even improves the stronger branch.

## Key Takeaways
- Image‑first prompting outperforms question‑first prompting in all evaluated settings, indicating a systematic bias toward image presentation.  
- Activation patching identifies a narrow mid‑network region where representations diverge sharply between prompt orders, pinpointing the circuit‑level source of the failure.  
- Test‑time training repairs this misalignment across layers and yields consistent improvements for both ordering approaches.

## Context
Vision‑language models are increasingly used to generate multimodal responses, yet subtle presentation details can affect performance. This work highlights a previously overlooked artifact that persists even when model architectures are identical, underscoring the need for robust evaluation protocols beyond simple accuracy metrics.

## Implications
For practitioners, this research suggests that training data and inference pipelines should consider prompt ordering as a design variable to avoid hidden biases. It also offers a practical fix—test‑time adaptation—that can be applied without retraining large models, promoting more reliable multimodal systems in industry applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20351v1)
