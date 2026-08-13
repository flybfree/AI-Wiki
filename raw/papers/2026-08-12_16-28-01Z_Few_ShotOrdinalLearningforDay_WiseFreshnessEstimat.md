---
title: Few-Shot Ordinal Learning for Day-Wise Freshness Estimation with Hyperspectral Fish Images
published: 2026-08-12T16:28:01Z
authors: Kazi Nabiul Alam, Pooneh Bagheri Zadeh, Akbar Sheikh-Akbari
url: http://arxiv.org/abs/2608.12230v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Few-Shot Ordinal Learning for Day-Wise Freshness Estimation with Hyperspectral Fish Images

## Abstract
Non-destructive food quality assessment has increasingly benefited from hyperspectral imaging (HSI), which captures spectral signatures linked to biochemical changes during storage. Estimating day-wise freshness, however, remains challenging owing to strong inter-fillet variability and scarce labelled data per product. All existing deep learning approaches for HSI-based freshness prediction operate under full supervision, requiring densely annotated training sets that are costly to obtain at the individual-product level. We introduce, to the best of our knowledge, the first few-shot learning framework for HSI-based food quality estimation. Each fillet defines a distinct episodic task, and a CORAL-style ordinal prediction head captures the ranked nature of freshness progression through cumulative threshold modelling. Biologically grounded monotonicity and embedding smoothness constraints further guide predictions toward plausible trajectories. On a 16-day salmon HSI dataset under a strict unseen-fillet protocol, our method achieves a mean absolute error of 1.58 days and 2-day accuracy of 72.3% with only three labelled days per fillet, substantially outperforming scalar regression and label-distribution baselines under an identical unseen-fillet protocol.

## Metadata
- **Published**: 2026-08-12T16:28:01Z
- **Authors**: Kazi Nabiul Alam, Pooneh Bagheri Zadeh, Akbar Sheikh-Akbari
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12230v1)