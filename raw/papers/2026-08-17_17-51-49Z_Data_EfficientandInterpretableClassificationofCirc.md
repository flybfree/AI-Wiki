---
title: Data-Efficient and Interpretable Classification of Circulating Tumor Cell Phenotypes in Microfluidic Devices via Deep Learning
published: 2026-08-17T17:51:49Z
authors: Serena Su, Yifan Wang, Senwei Liang
url: http://arxiv.org/abs/2608.16870v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Data-Efficient and Interpretable Classification of Circulating Tumor Cell Phenotypes in Microfluidic Devices via Deep Learning

## Abstract
Accurate classification of circulating tumor cell (CTC) phenotypes can provide valuable information for assessing metastatic potential. Label free microfluidic devices provide a hydrodynamic obstacle course that transforms subtle biophysical characteristics of CTCs, including size and deformability, into distinct kinematic trajectories. However, the highly nonlinear fluid structure interactions governing these trajectories make the inverse problem of inferring cellular phenotype from trajectory data analytically intractable. While deep neural networks (DNNs) have emerged as a powerful approach for addressing this inverse problem, their effectiveness is constrained by the limited availability of trajectory data and the lack of physical interpretability.   To address these challenges, we propose an interpretable and data efficient DNN framework for trajectory based CTC classification. To mitigate the scarcity of data, we develop Subsequence (SubSeq), a targeted augmentation strategy that randomly extracts informative local trajectory segments during training to promote learning from localized patterns. We further apply Gradient Weighted Class Activation Mapping to identify the trajectory features and physical regions of the microfluidic device that drive model predictions. Experimental results demonstrate that SubSeq improves classification accuracy over the evaluated baseline and augmentation methods. Furthermore, interpretability analysis suggests that localized trajectory segments contain substantial biophysical information relevant to accurate classification. This provides justification for SubSeq and also highlights the redundancy of full-length trajectories. More broadly, the proposed framework views microfluidic geometries as physical encoders of cellular mechanical properties, providing mechanistic insights that may inform the future design of diagnostic devices.

## Metadata
- **Published**: 2026-08-17T17:51:49Z
- **Authors**: Serena Su, Yifan Wang, Senwei Liang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16870v1)