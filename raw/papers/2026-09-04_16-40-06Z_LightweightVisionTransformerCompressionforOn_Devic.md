---
title: Lightweight Vision Transformer Compression for On-Device Plant Disease Detection in Resource-Constrained Agricultural Field Conditions
published: 2026-09-04T16:40:06Z
authors: Mahadev Sunil Kumar, Bhavika Gondi, Desaisetty Venkata Satya Sai Swapnith, Gangireddy Rahul Jogi, Sudheesh Manalil, Arnab Raha, Amitava Mukherjee, Parthasarathy Seethapathy, G. Gopakumar
url: http://arxiv.org/abs/2609.05334v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Lightweight Vision Transformer Compression for On-Device Plant Disease Detection in Resource-Constrained Agricultural Field Conditions

## Abstract
Chilli (Capsicum annuum) is one of India's most economically significant crops, yet its productivity is persistently threatened by diseases that are difficult to identify without expert intervention. While Vision Transformers (ViTs) have achieved high classification accuracy, their large computational footprint makes deployment on resource constrained devices challenging. Existing compression approaches typically address pruning, quantization, and knowledge distillation in isolation, leaving the potential benefits and interactions of their combined application insufficiently explored. We propose a unified Vision Transformer compression framework that combines Hessian-Balanced Adaptive Block Pruning (H-BAC), guided by second-order sensitivity estimation, with quantization and attention-based knowledge distillation. To systematically identify the most effective configuration within each compression family, each technique is first evaluated independently through controlled ablation studies, after which the best-performing components are integrated into a sequential deployment pipeline tailored to real-world agricultural constraints. On a chilli 3-class village-split dataset with a genuine cross-village, cross-device out-of-distribution test split, the resulting compressed models match or exceed the 95.13% FP32 baseline's accuracy, alongside 74-98% model size reduction, and the fully integrated compression pipeline achieves a 54.5x size reduction (327.42 MB to 6.01 MB) at 95.13 +/- 2.32% accuracy across four tested configurations. A direct comparison further reveals that, on this dataset, a directly-trained student of the same final size, without pruning or distillation, reaches comparable accuracy of 94.87%, at the same 6.01 MB INT8 size, indicating where H-BAC and knowledge distillation are, and are not yet shown to be, worth their computational cost.

## Metadata
- **Published**: 2026-09-04T16:40:06Z
- **Authors**: Mahadev Sunil Kumar, Bhavika Gondi, Desaisetty Venkata Satya Sai Swapnith, Gangireddy Rahul Jogi, Sudheesh Manalil, Arnab Raha, Amitava Mukherjee, Parthasarathy Seethapathy, G. Gopakumar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05334v1)