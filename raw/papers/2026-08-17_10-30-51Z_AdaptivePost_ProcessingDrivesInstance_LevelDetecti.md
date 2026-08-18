---
title: Adaptive Post-Processing Drives Instance-Level Detection in Stroke Lesion Segmentation
published: 2026-08-17T10:30:51Z
authors: Qinghui Liu, Jon André Ottesen, Atle Bjørnerud, Kyrre Eeg Emblem
url: http://arxiv.org/abs/2608.16377v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Adaptive Post-Processing Drives Instance-Level Detection in Stroke Lesion Segmentation

## Abstract
Instance-level lesion detection has been an increasingly larger focal point in medical image segmentation besides the more standard voxel-level overlap. Still, most pipelines are trained and post-processed for voxel overlap alone. In particular, the mismatch is most pronounced for small lesions, where a near-miss prediction---substantial overlap that falls just short of the instance-matching threshold---scores the same as a complete miss. In our ISLES'26 submission, we found that closing this gap mattered far more in post-processing than in architecture design. Our Volume-Conditioned Adaptive Post-Processing (VCAP) scheme adjusts component-size thresholds to each case's predicted lesion burden, improving Lesion-F1 by 0.032 (unbiased cross-fold estimate)---approximately 6 times larger than any architectural change we tested. A resolution-aware attention architecture (Viola2Plus), designed for small-lesion segmentation, shows why the distinction matters: it left small-lesion Dice unchanged but raised small-lesion detection rate by 3.7\%, a real effect voxel-overlap metrics alone would have missed. Under 5-fold cross-validation on the 1,453-case training set, our post-processed two-architecture ensemble achieves Dice 0.651 and Lesion-F1 0.614, versus 0.644 and 0.573 for the unprocessed single-model baseline.

## Metadata
- **Published**: 2026-08-17T10:30:51Z
- **Authors**: Qinghui Liu, Jon André Ottesen, Atle Bjørnerud, Kyrre Eeg Emblem
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16377v1)