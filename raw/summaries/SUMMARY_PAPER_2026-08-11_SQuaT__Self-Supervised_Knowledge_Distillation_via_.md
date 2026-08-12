---
title: SQuaT: Self-Supervised Knowledge Distillation via Student-Aware Quantized Teacher Features
url: http://arxiv.org/abs/2608.10709v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_09-29-30Z_SQuaT_Self_SupervisedKnowledgeDistillationviaStude.md
generated_at: 2026-08-11 22:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SQuaT, a label‑free quantization‑aware training framework that combines knowledge distillation with quantized teacher features to eliminate the residual lower bound observed in prior QAT‑KD methods. By applying the student’s quantization parameters to quantize the teacher’s features during distillation, SQuaT theoretically removes the unattainable residual and improves performance, especially at extreme low‑bit settings such as 1‑ and 2‑bit.

## Key Takeaways
- The residual lower bound in QAT‑KD arises from a mismatch between the teacher’s full‑precision features and the quantized student output.  
- SQuaT resolves this by using the student’s quantization scheme to re‑quantize the teacher’s features, thus aligning both representations.  
- Experiments show consistent gains over strong baselines across diverse architectures and model designs.

## Context
Quantization is essential for deploying models on resource‑constrained devices, yet it often requires labeled data that may be unavailable due to privacy or cost limits. Knowledge distillation offers a way to transfer knowledge without labels, but its effectiveness is limited by the residual lower bound in QAT‑KD approaches. This paper addresses that limitation with a novel student‑aware method.

## Implications
SQuaT enables high‑quality inference from quantized models even when labeled data cannot be obtained, expanding the scope of label‑free training. For industry practitioners, this means more reliable deployment of low‑bit models without sacrificing accuracy or requiring costly labeling pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10709v1)
