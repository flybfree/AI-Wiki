---
title: A foundation-model approach to pediatric headache classification from rs-fMRI
published: 2026-08-07T14:46:57Z
authors: Guilherme S. Imai Aldeia, Clara Moon, Julie Shulman, Navil Sethna, Allison Smith, Alyssa Lebel, William G. La Cava, Scott Holmes
url: http://arxiv.org/abs/2608.07287v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A foundation-model approach to pediatric headache classification from rs-fMRI

## Abstract
Headache is the most common neurological disorder in children and substantially affects quality of life. We investigated whether resting-state functional MRI (rs-fMRI) can support pediatric headache classification using machine learning. We encoded rs-fMRI data using NeuroSTORM, a recent foundation model, and fine-tuned it to distinguish healthy controls from children with headache and subsequently classify headache subtypes. We compared NeuroSTORM with a standard neuroscience approach using functional-connectivity (FC) matrices derived from brain activity as predictors. Using 189 rs-fMRI scans from 110 individuals collected across two visits (prevalence of any headache: 74%), NeuroSTORM achieved an area under the receiver operating characteristic curve (AUROC) of 0.82 (95% CI, 0.82-0.82) and an area under the precision-recall curve (AUPRC) of 0.93 (95% CI, 0.93-0.94) for discriminating headache from non-headache. In contrast, models trained on FC matrices showed lower performance (AUROC, 0.67 [95% CI, 0.67-0.67]; AUPRC, 0.85 [95% CI, 0.85-0.85]). In multiclass classification of healthy controls, chronic migraine, and non-chronic headaches (e.g., post-viral headache, new daily persistent headache, post-traumatic headache), NeuroSTORM achieved a macro-AUROC of 0.69 (95% CI, 0.68-0.69). Results suggest that the approach can distinguish chronic migraine but has difficulty differentiating other headache subtypes from chronic migraine. Overall, under limited-data conditions, NeuroSTORM appears to capture latent rs-fMRI representations that transfer to headache-related tasks without relying on FC features. These findings provide proof of concept for fMRI-based prediction of pediatric headache and highlight potential future utility for subtype identification and individualized treatment strategies.

## Metadata
- **Published**: 2026-08-07T14:46:57Z
- **Authors**: Guilherme S. Imai Aldeia, Clara Moon, Julie Shulman, Navil Sethna, Allison Smith, Alyssa Lebel, William G. La Cava, Scott Holmes
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07287v1)