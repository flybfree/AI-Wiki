---
title: CAPT: A Multi-task Continuous Autoregressive Transformer enabling Cross-dataset and Cross-species Transfer for Calcium Population Dynamics
url: http://arxiv.org/abs/2607.23258v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-25_15-53-55Z_CAPT_AMulti_taskContinuousAutoregressiveTransforme.md
generated_at: 2026-07-27 23:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CAPT, a continuous autoregressive transformer designed to model calcium population dynamics across multiple species and experimental conditions. By pretraining on a large mouse dataset and freezing the backbone while updating only adaptation modules, CAPT demonstrates strong transfer performance in forecasting neural activity and decoding behavior in zebrafish and C. elegans data. The results show that embeddings from different datasets occupy a shared functional space, indicating reusable representations.

## Key Takeaways
- CAPT uses continuous patch tokenization to directly model calcium traces as an autoregressive sequence enabling end-to-end pretraining.
- The frozen backbone allows adaptation across independent mouse, zebrafish, and C. elegans datasets collected by different labs without retraining the entire model.
- Multimodal NeuroPAL annotations reveal that CAPT embeddings form a shared functional space capturing anatomical cell‑identity structure across species.

## Context
Foundation models in neuroscience aim to learn universal representations from large biological datasets, but most are task‑specific and fail to generalize beyond their original experimental setup. CAPT addresses this limitation by providing a continuous autoregressive architecture that can be pretrained once and then fine‑tuned for diverse downstream tasks across species.

## Implications
These findings suggest that calcium imaging data could serve as a source of general‑purpose neural foundation models, reducing the need for separate model development per dataset. Practitioners may leverage CAPT to accelerate cross‑species analysis and improve interpretability by using shared embeddings in multimodal pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23258v1)
