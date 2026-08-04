---
title: xMICD: Explainable Representation of Multiple ICD Codes
published: 2026-08-02T02:24:57Z
authors: Pat Vatiwutipong, Kumkup Keeratisiwakul, Albert Phuoc Kien Van Truong, Nutcha Yodrabum, Wasin Pansiritanachot, Marvin N. Wright, Thanapon Noraset
url: http://arxiv.org/abs/2608.00935v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# xMICD: Explainable Representation of Multiple ICD Codes

## Abstract
Electronic Health Records (EHRs) are widely used for clinical risk prediction using machine learning. International Classification of Diseases (ICD) codes provide structured information about patient diagnoses, but representing them effectively remains challenging. Existing approaches often face a trade-off between predictive performance and interpretability: grouping-based representations are interpretable but may lose information, while embedding-based representations achieve strong predictive performance but are difficult to interpret. We propose Explainable Representation of Multiple ICD Codes (xMICD), a method for constructing low-dimensional patient representations from sets of ICD codes. xMICD combines clinically meaningful diagnostic groupings with similarity in a pre-trained ICD embedding space. Instead of using binary group membership, the method assigns codes to groups via similarity-based relative assignments, yielding features that reflect how closely a patient's diagnoses align with each clinical group. Experiments on large-scale EHR datasets demonstrate that xMICD achieves predictive performance comparable to embedding-based representations such as ICD2Vec across multiple clinical prediction tasks. At the same time, the resulting features remain clinically interpretable because each dimension corresponds to a recognizable diagnostic group. xMICD therefore provides a practical way to integrate embedding-based semantic relationships into interpretable clinical feature spaces for machine learning models.

## Metadata
- **Published**: 2026-08-02T02:24:57Z
- **Authors**: Pat Vatiwutipong, Kumkup Keeratisiwakul, Albert Phuoc Kien Van Truong, Nutcha Yodrabum, Wasin Pansiritanachot, Marvin N. Wright, Thanapon Noraset
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00935v1)