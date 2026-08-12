---
title: UniMod: Enhancing Multi-Modal Medical Diagnosis through Cross-Modality and Within-Modality Alignment
published: 2026-08-10T23:39:49Z
authors: Zijian Gu, Weikai Lin, Shuang Zhou, Zihan Chen, Song Wang
url: http://arxiv.org/abs/2608.10316v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# UniMod: Enhancing Multi-Modal Medical Diagnosis through Cross-Modality and Within-Modality Alignment

## Abstract
Multi-modal learning combining medical images and clinical text is promising for disease diagnosis. However, standard multi-modal training leads to shortcut learning: models exploit the easier modality (e.g., diagnostic cues in text) while neglecting harder-to-learn features (e.g., subtle visual patterns). We propose UniMod, a framework that mitigates shortcut learning by requiring each modality to predict the diagnosis on its own. It supervises image-only, text-only, and multi-modal classification simultaneously, so each modality must extract diagnostic features. We add cross-modality alignment for knowledge transfer and within-modality supervised contrastive alignment over same-diagnosis patients. On Harvard-Glaucoma, UniMod reaches 0.850 AUC, outperforming OGM-GE and Gradient Blending by 1.6-1.8%; on CheXpert Plus, it reaches 0.966 AUC, surpassing them by over 5%. UniMod also extends to 5-class multi-label diagnosis without architectural change, improving mean AUC by 0.097 over CGGM.

## Metadata
- **Published**: 2026-08-10T23:39:49Z
- **Authors**: Zijian Gu, Weikai Lin, Shuang Zhou, Zihan Chen, Song Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10316v1)