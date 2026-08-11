---
title: A Controlled Study of Feature-Based Knowledge Distillation Across Student Designs
published: 2026-08-08T19:10:17Z
authors: Abhinand Balachandran, Praveen Prashant
url: http://arxiv.org/abs/2608.08294v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Controlled Study of Feature-Based Knowledge Distillation Across Student Designs

## Abstract
Knowledge distillation trains a smaller student to match the outputs of a larger teacher. Feature-based methods also align intermediate representations, but this extra constraint may affect students differently. We study this question on CIFAR-100 using a ResNet-50 teacher, a width-controlled CustomResNet family and MobileNetV2 as a cross-design comparison. For each student, we evaluate each feature method against a matched logit-KD run using the same teacher, optimizer settings, training schedule and seed. We repeat the main comparisons across multiple seeds.   Logit KD improved every tested student over its scratch baseline. Attention Transfer showed no clear relationship with size inside the CustomResNet family, but its average effect was negative for that family and positive for MobileNetV2. FitNets was below logit KD in all 15 paired runs. Within the constant-depth width sweep, its gap increased for wider students, although the different-depth w=48 student did not follow this trend. Finally, the same auxiliary coefficient produced different gradient scales across students, showing that a fixed coefficient does not create a uniform training condition.

## Metadata
- **Published**: 2026-08-08T19:10:17Z
- **Authors**: Abhinand Balachandran, Praveen Prashant
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08294v1)