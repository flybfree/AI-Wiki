---
title: OrthKD: Extracting Generalized Clinical Knowledge from Heterogeneous Teachers for Lightweight Deployment
published: 2026-07-28T10:24:40Z
authors: Yi Xu, Cheng Chen, Mufan Cao
url: http://arxiv.org/abs/2607.25545v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# OrthKD: Extracting Generalized Clinical Knowledge from Heterogeneous Teachers for Lightweight Deployment

## Abstract
Deploying diabetic retinopathy (DR) screening models in primary care requires edge-efficient systems that remain accurate, safe, and reliable under domain shift. Multi-teacher knowledge distillation (KD) is a natural compression strategy, but existing approaches largely assume that all teachers provide equally trustworthy supervision. In our setting, this assumption fails: a strong CNN teacher (EfficientNet-B3, 0.876 QWK) and a weaker Transformer teacher (Swin-Base, 0.830 QWK) are complementary, yet the Transformer's logits can still mislead the student. We therefore propose OrthKD, a selective-trust distillation framework that transfers full supervision from the strong CNN, uses feature-only distillation from the weak ViT, and enforces orthogonality between teacher-specific student projections to encourage complementary rather than redundant evidence. This design preserves local lesion precision, injects global structural context, and improves robustness to distribution shift. On 132,049 retinal images, a 5.4M-parameter MobileNetV3 student reaches 0.885 QWK on EyePACS and improves zero-shot Messidor-2 performance from 0.507 to 0.728 QWK, while also achieving strong referral AUC and calibration. These results show that selectively distilling heterogeneous teachers can enable practical DR screening on resource-constrained devices.

## Metadata
- **Published**: 2026-07-28T10:24:40Z
- **Authors**: Yi Xu, Cheng Chen, Mufan Cao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25545v1)