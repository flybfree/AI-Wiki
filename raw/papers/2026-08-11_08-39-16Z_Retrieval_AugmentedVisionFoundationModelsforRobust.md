---
title: Retrieval-Augmented Vision Foundation Models for Robust Leukemia Cell Classification across Multiple Microscopy Datasets
published: 2026-08-11T08:39:16Z
authors: Carlos Zamora, Hiram Zuniga, Ulises Orozco-Rosas, Kenia Picos
url: http://arxiv.org/abs/2608.10657v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Retrieval-Augmented Vision Foundation Models for Robust Leukemia Cell Classification across Multiple Microscopy Datasets

## Abstract
Leukemia cell image classification is challenged by real-world domain shifts from acquisition, staining, illumination, and site protocols, causing single-dataset models to generalize poorly in real clinical scenarios. This work presents a robust framework for leukemia classification across multiple heterogeneous datasets using a two-stage pipeline with a pretrained vision foundation model. Stage 1 performs binary classification (leukemia vs. non-leukemia) and is trained using 122,167 single-cell images. Stage 2 is conditionally applied to Stage 1 positives to perform subtype classification into Acute Lymphoblastic Leukemia (ALL) and Acute Myeloid Leukemia (AML), trained using 69,400 single-cell images. Labels are harmonized across five heterogeneous datasets to enable cross-dataset training, and performance is evaluated on a held-out dataset protocol to assess domain-shift generalization. Within this pipeline, three encoders are benchmarked (DinoBloom, pretrained on single-cell images; BiomedCLIP, pretrained on biomedical data; and CLIP as a general-purpose model) under linear probing, Low-Rank Adaptation (LoRA), and a Retrieval-Augmented Classification (RAC) module that retrieves the top-k most similar cell images to provide cytomorphological grounding. The objective is to quantify how much domain-specific pretraining contributes to performance under domain shift, and whether cost-effective adaptation and retrieval can be a viable alternative to expensive domain-specialized pretraining. The held-out protocol additionally serves as a diagnostic tool, revealing when classification performance is attributable to dataset-specific artifacts rather than to cytomorphological features.

## Metadata
- **Published**: 2026-08-11T08:39:16Z
- **Authors**: Carlos Zamora, Hiram Zuniga, Ulises Orozco-Rosas, Kenia Picos
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10657v1)