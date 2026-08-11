---
title: LoRSA: Toward Generalizable Parameter-Efficient Fine-Tuning for Biomedical Downstream Tasks
published: 2026-08-07T20:30:35Z
authors: Saed Moradi, Benyamin Ghojogh, M. Hadi Sepanj, Yimin Yang, Ashirbani Saha
url: http://arxiv.org/abs/2608.07749v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LoRSA: Toward Generalizable Parameter-Efficient Fine-Tuning for Biomedical Downstream Tasks

## Abstract
Parameter-efficient fine-tuning enables the adaptation of vision foundation models to biomedical tasks under limited computational resources, but a single low-rank update can constrain all task-specific changes to one narrow parameter subspace. This restriction may prevent the model from simultaneously representing globally shared task structure and localized residual directions required for generalization to unseen imaging domains. We introduce LoRSA, a global--residual adaptation framework that jointly learns a dense low-rank component and a dynamically structured-sparse low-rank component. The dense component captures globally coordinated task adaptation, while the structured component provides complementary residual corrections whose support evolves during training. We characterize the representational capacity, approximation properties, rank structure, and singular-subspace complementarity of this decomposition. We evaluate LoRSA for four-class breast-density classification using DINOv3-Base, with VinDr-Mammo as the source domain and MammosighTR and RSNA as unseen external domains. LoRSA remains competitive on the internal validation set and achieves the best external macro-F1 on both target datasets, improving upon the strongest competing method by 2.15 percentage points on MammosighTR and 3.09 percentage points on RSNA. Weight-matrix analysis further shows that approximately $92\%$ of the energy of each adaptation component lies outside the bilateral singular subspace of the other, indicating that the two components learn largely complementary update directions. These results suggest that organizing adaptation capacity into distinct global and residual paths can improve the external-domain generalization of parameter-efficiently adapted biomedical vision models.

## Metadata
- **Published**: 2026-08-07T20:30:35Z
- **Authors**: Saed Moradi, Benyamin Ghojogh, M. Hadi Sepanj, Yimin Yang, Ashirbani Saha
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07749v1)