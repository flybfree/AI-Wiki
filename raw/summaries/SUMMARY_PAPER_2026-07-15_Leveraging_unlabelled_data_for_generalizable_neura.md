---
title: Leveraging unlabelled data for generalizable neural population decoding
url: http://arxiv.org/abs/2607.14086v1
type: paper-summary
date: 2026-07-15
source_paper: 2026-07-15_17-58-00Z_Leveragingunlabelleddataforgeneralizableneuralpopu.md
generated_at: 2026-07-15 22:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces MOJO, a training framework that combines self‑supervised learning through masked autoencoding with supervised spike decoding to improve performance on neural data. Experiments show that MOJO outperforms purely supervised models, especially when labeled data are scarce, and its benefits extend beyond spiking signals to human electrocorticography.

## Key Takeaways
- MOJO jointly uses self‑supervised masking and supervised spike decoding, enabling effective training with limited behavioural labels.
- The approach yields superior few‑shot finetuning results compared with SL‑only models, particularly in low‑label scenarios.
- SSL‑augmented representations improve interpretability for brain region classification and spike‑statistics prediction without additional task‑specific optimization.

## Context
Current neurotechnology relies heavily on supervised learning that demands extensive paired behavioural labels, limiting applicability to new sessions or species. Spiking neural networks are powerful but constrained by this label dependency, pushing the field toward more flexible data usage strategies.

## Implications
MOJO demonstrates a scalable path for deploying unlabelled data across tasks and modalities, reducing reliance on costly human labelling. Practitioners can leverage SSL‑enhanced models to achieve state‑of‑the‑art performance with minimal supervision, advancing both research and commercial neurotechnology applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.14086v1)
