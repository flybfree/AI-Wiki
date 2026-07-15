---
title: "Summary: Closing the Domain Gap in Biomedical Imaging by In-Context Control Samples"
date: 2026-04-22
tags: ['paper', 'research', 'ai']
---
# Summary: Closing the Domain Gap in Biomedical Imaging by In-Context Control Samples


**Source**: [Original Paper](http://arxiv.org/abs/2604.20824v1)
Saved: 2026-05-07 22:24
Source: 2026-04-22_17-49-00Z_ClosingtheDomainGapinBiomedicalImagingbyIn_Context.md

---

## Summary
This paper addresses batch effects in biomedical imaging, where technical variation across experimental batches degrades reproducibility and causes deep learning models to fail on new batches. The authors propose CS-ARM-BN, a meta-learning adaptation method that uses negative control samples as in-context reference data for stabilization. On MoA classification with the JUMP-CP dataset, the method is reported to close the domain gap better than standard ResNets and foundation models, especially under strong shifts such as cross-lab data.

## Key Takeaways
- Batch effects are presented as the main obstacle to robust biomedical imaging models.
- Negative control samples are used as stable context for adaptation.
- CS-ARM-BN is a meta-learning approach built on batch normalization.
- Reported results show near-training-domain performance on new batches.
- The work argues that in-context adaptation can make biomedical imaging models more practical under domain shift.

## Original Reference
- Title: Closing the Domain Gap in Biomedical Imaging by In-Context Control Samples
- Authors: Ana Sanchez-Fernandez, Thomas Pinetz, Werner Zellinger, Günter Klambauer
- Published: 2026-04-22T17:49:00Z
- URL: http://arxiv.org/abs/2604.20824v1
- Source file: /home/rich/wiki/ai-research/raw/papers/2026-04-22_17-49-00Z_ClosingtheDomainGapinBiomedicalImagingbyIn_Context.md