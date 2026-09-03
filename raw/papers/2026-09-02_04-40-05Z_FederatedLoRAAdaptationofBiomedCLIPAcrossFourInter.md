---
title: Federated LoRA Adaptation of BiomedCLIP Across Four International Chest X-Ray Cohorts
published: 2026-09-02T04:40:05Z
authors: Sanjaya Poudel, Nirajan Kunwor, Manish Dhakal, Debesh Jha, Sunil Kumar Gaire
url: http://arxiv.org/abs/2609.02101v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Federated LoRA Adaptation of BiomedCLIP Across Four International Chest X-Ray Cohorts

## Abstract
Federated learning (FL) lets institutions train a shared model without exchanging data, and Low-Rank Adaptation (LoRA) makes this practical at scale by communicating only compact low-rank updates. Biomedical imaging is a compelling setting for this combination: patient data are archived behind privacy regulations, and institutions differ widely in scanners, protocols, and compute. Such heterogeneity raises the question of how federated LoRA updates should be aggregated, increasingly pressing as multimodal vision-language models become central to medical image analysis. We benchmark federated Parameter-efficient fine-tuning (PEFT) of BiomedCLIP for chest radiograph classification across four public cohorts on three continents (USA, Vietnam, Spain). Federated LoRA adaptation improves shared-class AUC on all four cohorts over the unadapted BiomedCLIP backbone (mean 0.687 to 0.802), showing that the gains come from federated adaptation rather than from the pretrained model's zero-shot ability. Relative to isolated single-cohort training, federation improves the weaker cohorts while largely preserving the strongest and approaches a centralized reference (0.812) that pools all data. The singular value decomposition (SVD)-based product-space aggregation introduced by FlexLoRA is essential to this gain (naive factor averaging drops mean AUC by 0.097), whereas a drift-correcting optimizer (FedProx) shows no benefit over FedAvg in our single-seed runs, consistent with LoRA's low-rank updates already limiting client drift. Biomedical vision-language models can thus be adapted collaboratively across heterogeneous, geographically distributed institutions without centralizing data.

## Metadata
- **Published**: 2026-09-02T04:40:05Z
- **Authors**: Sanjaya Poudel, Nirajan Kunwor, Manish Dhakal, Debesh Jha, Sunil Kumar Gaire
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02101v1)