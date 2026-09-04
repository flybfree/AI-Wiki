---
title: Understanding Autonomous Driving Datasets by Describing Differences between Image Subsets in Natural Language
published: 2026-09-03T11:15:23Z
authors: Julian Truetsch, Felix Hauser, Christoph Stiller, Frank Bieder
url: http://arxiv.org/abs/2609.03677v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Understanding Autonomous Driving Datasets by Describing Differences between Image Subsets in Natural Language

## Abstract
Understanding the composition of large-scale autonomous driving datasets is essential for safety, robustness, and reliable operation across domains. For example, domain shift between locations could lead to the operating environment being misaligned with the training data, resulting in potentially dangerous performance degradation. Yet, existing data analysis pipelines largely rely on metadata, predefined labels, or manual inspection, which provide limited semantic insight or do not scale. This paper studies set difference captioning: given two subsets of images, the goal is to produce a natural-language hypothesis describing differences between the target and reference set. Building on a two-stage formulation, we adapt the method to autonomous driving by focusing on object-centric patches derived from object detection, which simplifies aggregation and enables attribution of differences to specific object instances or categories. To evaluate this setting in-domain, we introduce a new benchmark, AD-Diff Bench. Low-concentration experiments assess the suitability of set-difference-captioning approaches to sparse, real-world differences. We restrict our experiments to open-weight models to support reproducibility and ease of deployment. The proposed benchmark and analysis provide a step towards practical, human-interpretable dataset introspection for autonomous driving datasets. Our implementation and benchmark dataset are available at https://github.com/KIT-MRT/AD-Diff

## Metadata
- **Published**: 2026-09-03T11:15:23Z
- **Authors**: Julian Truetsch, Felix Hauser, Christoph Stiller, Frank Bieder
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03677v1)