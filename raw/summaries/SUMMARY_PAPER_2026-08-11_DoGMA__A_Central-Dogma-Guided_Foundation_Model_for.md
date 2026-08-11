---
title: DoGMA: A Central-Dogma-Guided Foundation Model for Multi-Omics Alignment and Multi-Task Learning in Oncology
url: http://arxiv.org/abs/2608.08148v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-08_14-15-43Z_DoGMA_ACentral_Dogma_GuidedFoundationModelforMulti.md
generated_at: 2026-08-11 13:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces DoGMA, a central-dogma-guided foundation model for pan-cancer multi-omics analysis. It uses directed attention in a Transformer-MoE architecture to enforce directionality of biological information flow and pretrains it with masked hierarchical omics reconstruction. Across tasks like cancer representation learning, survival prediction, and metastasis prediction, DoGMA outperforms prior models.

## Key Takeaways
- The model incorporates directed attention that biases inter‑omics communication toward the central dogma’s unidirectional flow, creating a domain‑specific inductive bias.
- Masked hierarchical omics reconstruction is used as pretraining to guide learning of biologically consistent interactions across modalities.
- These two components together improve performance on downstream tasks such as cancer representation, survival prediction, and metastasis prediction.

## Context
Current multi‑omics foundation models rely on unrestricted bidirectional attention, which can produce representations that lack biological directionality. This limits their ability to transfer knowledge between heterogeneous cancers or incomplete data sets. The central dogma provides a natural constraint that could be encoded into model architecture for more robust learning.

## Implications
By aligning attention with the central dogma, DoGMA offers a biologically informed design principle that can enhance cross‑omics generalization and reduce overfitting in limited datasets. Practitioners may adopt similar inductive biases to improve model reliability in oncology research and drug discovery pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08148v1)
