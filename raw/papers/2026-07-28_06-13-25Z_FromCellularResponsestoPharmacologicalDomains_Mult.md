---
title: From Cellular Responses to Pharmacological Domains: Multimodal Zero-Shot Drug Representation Learning
published: 2026-07-28T06:13:25Z
authors: Jintao Huang, Lu Leng, Ziyuan Yang
url: http://arxiv.org/abs/2607.25322v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Cellular Responses to Pharmacological Domains: Multimodal Zero-Shot Drug Representation Learning

## Abstract
Multimodal drug discovery enables drug representation learning beyond chemical structure by incorporating cellular responses such as gene expression and cell morphology. However, direct fusion and instance-level contrastive alignment may mix mechanism-related signals with modality-specific noise and incorrectly separate structurally dissimilar but biologically related compounds. This limitation can obscure transferable mechanism patterns required for predicting the properties of unseen compounds. We introduce PMRD, a pharmacological response domain-guided framework for multimodal zero-shot drug property prediction. PMRD separates mechanism-consistent factors from modality-specific information and constructs a consensus response domain across three modalities. Mechanism candidate augmentation identifies locally stable factors, while retrieval-geometry attribution dynamically reweights the alignment and augmentation objectives according to whether their updates preserve inter-drug discriminability.This feedback suppresses training signals that conflict with mechanism-discriminative retrieval. PMRD further combines complementary representations through reliability-aware multiview retrieval. Experiments on public datasets show improved zero-shot property prediction and more biologically coherent drug neighborhoods. Hard-negative analysis further indicates fewer conflicts between structurally dissimilar but response-related compounds. These results support PMRD as an effective framework for mechanism-aware multimodal drug representation learning.\footnote{The code will be released upon publication.}

## Metadata
- **Published**: 2026-07-28T06:13:25Z
- **Authors**: Jintao Huang, Lu Leng, Ziyuan Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25322v1)