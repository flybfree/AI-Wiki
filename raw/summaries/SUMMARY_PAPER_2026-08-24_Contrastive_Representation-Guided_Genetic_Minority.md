---
title: Contrastive Representation-Guided Genetic Minority Oversampling for Imbalanced Time-Series Classification
url: http://arxiv.org/abs/2608.22804v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_05-03-51Z_ContrastiveRepresentation_GuidedGeneticMinorityOve.md
generated_at: 2026-08-24 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces FreMGP, a contrastive representation‑guided genetic minority oversampling method for imbalanced time‑series classification. Experiments on benchmark datasets show that FreMGP outperforms interpolation‑based oversampling and deep generative models, consistently boosting classifier performance across both general machine learning and deep learning approaches.

## Key Takeaways  
- Frequency‑domain class‑discriminative representation module based on contrastive learning guides the evolutionary search toward high‑quality synthetic time‑series samples.  
- Each individual in the genetic programming represents a set of synthetic minority‑class time‑series samples, enhancing diversity and reducing redundancy.  
- FreMGP consistently outperforms existing oversampling methods and improves performance for diverse classifiers.

## Context  
Time‑series classification often suffers from severe class imbalance where minority classes are scarce. Conventional sampling techniques either distort temporal structure or produce unrealistic synthetic data, limiting model generalization. This work tackles these challenges by merging contrastive learning with genetic programming to generate realistic, temporally coherent samples.

## Implications  
The method offers a scalable framework for generating diverse synthetic samples without compromising temporal dependencies, enabling robust classification on imbalanced datasets. Practitioners can adopt FreMGP to enhance performance of both traditional and deep models, reducing false negatives in critical applications such as anomaly detection or medical monitoring.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22804v1)
