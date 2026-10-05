---
title: Characterizing the Performance Gap in Human Activity Recognition for Older Adults
url: http://arxiv.org/abs/2610.02711v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-02_02-46-08Z_CharacterizingthePerformanceGapinHumanActivityReco.md
generated_at: 2026-10-04 22:03
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether performance gains in Human Activity Recognition (HAR) models trained on younger-adult datasets transfer to older adults, using a carefully annotated free-living dataset (MyMove, mean age 71) collected from wrist-worn accelerometers. The authors find that benchmark improvements on younger populations do not generalize equally to older adults, producing a persistent and widening performance gap, though self-supervised features pretrained on age-diverse data (UK Biobank) substantially narrow this disparity at modest cost to younger-adult accuracy.

## Key Takeaways
- Benchmark progress in wearable HAR is misleading when evaluated solely on younger-adult datasets: deep-learning architectures and training regimes that show steady improvement on standard benchmarks fail to transfer equivalently to older-adult data, revealing a persistent and often widening performance gap under both leave-one-subject-out and cross-dataset transfer evaluations.
- Richer, age-diverse representations are the key lever for closing the gap: frozen self-supervised features pretrained on the UK Biobank dataset—which spans a broad age range—substantially improve recognition performance on older-adult data and consistently narrow the disparity between age groups, though a residual gap remains even after this intervention.
- Architectural scaling and benchmark gains alone provide an incomplete picture of progress in wearable HAR; the authors argue that meaningful advances require representations that explicitly capture population diversity in movement patterns, combined with personalized adaptation to individual routines rather than one-size-fits-all model improvements.

## Context
Wearable HAR systems are increasingly deployed in clinical monitoring, fall-risk assessment, and behavioral tracking for aging populations, yet the vast majority of training and evaluation datasets are dominated by younger, healthier adults. This paper sits at the intersection of fairness in machine learning, health informatics, and sensor-based AI, directly challenging the assumption that architectural advances on standard benchmarks translate into equitable real-world performance across age groups.

## Implications
For practitioners deploying HAR in geriatric care, rehabilitation, and public-health surveillance, these findings signal that off-the-shelf models trained on younger populations will systematically underperform for older users, potentially leading to missed activity events or inaccurate health assessments. Industry developers and researchers must prioritize age-diverse training data, self-supervised pretraining on heterogeneous populations, and personalized adaptation pipelines to ensure that wearable health technologies deliver equitable accuracy across the full spectrum of users they are intended to serve.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.02711v1)
