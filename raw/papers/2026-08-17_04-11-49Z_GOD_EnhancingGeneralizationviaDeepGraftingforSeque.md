---
title: GOD: Enhancing Generalization via Deep Grafting for Sequential Recommendation
published: 2026-08-17T04:11:49Z
authors: WooJoo Kim, JunYoung Kim, JaeHyung Lim, HwanJo Yu
url: http://arxiv.org/abs/2608.16073v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GOD: Enhancing Generalization via Deep Grafting for Sequential Recommendation

## Abstract
Sequential recommenders often struggle with sparse and noisy histories, limiting generalization to unseen interactions. Knowledge distillation mitigates this by transferring dense supervision from a teacher to a student. However, most distillation methods run teacher and student independently, then match student outputs or representations to the teacher. Such supervision entangles student-component effects, blurring whether weak generalization stems from unreliable embeddings, overfitted encoding, or co-adaptation to sparse histories. In this paper, we propose Graft-Oriented Distillation (GOD), a component-level distillation framework for improved generalization through grafting. Grafting denotes replacing selected frozen-teacher components with trainable student counterparts to build hybrid source models. GOD uses these hybrid models to evaluate student embeddings with the teacher encoder and the student encoder with teacher embeddings, providing component-level feedback. At inference, GOD uses only the student, incurring no additional cost. Across three real-world datasets, GOD outperforms state-of-the-art baselines by up to 13.92%.

## Metadata
- **Published**: 2026-08-17T04:11:49Z
- **Authors**: WooJoo Kim, JunYoung Kim, JaeHyung Lim, HwanJo Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16073v1)