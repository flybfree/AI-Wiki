---
title: Beyond Classification: Pathology Foundation Models as Detection Encoders for Mitotic Figures
published: 2026-07-30T10:56:38Z
authors: Sweta Banerjee, Alireza Teimoury, Nils Porsche, Alexandra K. Stoll, Viktoria Weiss, Niklas Hargarter, Jonas Ammeling, Thomas Conrad, Christoph Stroblberger, Christopher Kaltnecker, Robert Klopfleisch, Christof A. Bertram, Katharina Breininger, Marc Aubreville
url: http://arxiv.org/abs/2607.28007v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Classification: Pathology Foundation Models as Detection Encoders for Mitotic Figures

## Abstract
Pathology foundation models (FMs) are models trained on vast amounts of typically unlabeled data and have been shown to yield regularized latent spaces that can be used effectively in downstream classification tasks. This is also true for the classification of mitotic figures vs. other cells. However, it is so far unclear if the latent space of current FMs provides features that are discriminant and spatially suitably resolved to also serve as a backbone for dense object detection paradigms. In this work, we investigate this question for common current pathology FMs (UNI, UNI2-h, Virchow, Virchow2, H-optimus-0, H-optimus-1) and compare their performance against a fully end-to-end trained baseline based on a ResNet50 architecture. We combine FM backbones with representatives of single stage, dual stage and self-attention-based detectors (RetinaNet, Faster R-CNN, Deformable DETR respectively) on the multi-domain MIDOG++ dataset, and on the TUPAC16 dataset as an out-of-domain case. We show that the H-optimus-0 and Virchow models yielded competitive performance, indicating that the latent spaces of current FMs, all trained on image-level self-supervision, are suitable for direct mitotic figure detection and may be slightly more robust on our out-of-domain test case. All code is made available publicly at https://github.com/DeepMicroscopy/FM4MFdet.

## Metadata
- **Published**: 2026-07-30T10:56:38Z
- **Authors**: Sweta Banerjee, Alireza Teimoury, Nils Porsche, Alexandra K. Stoll, Viktoria Weiss, Niklas Hargarter, Jonas Ammeling, Thomas Conrad, Christoph Stroblberger, Christopher Kaltnecker, Robert Klopfleisch, Christof A. Bertram, Katharina Breininger, Marc Aubreville
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28007v1)