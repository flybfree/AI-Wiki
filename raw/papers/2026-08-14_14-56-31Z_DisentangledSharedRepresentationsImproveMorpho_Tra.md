---
title: Disentangled Shared Representations Improve Morpho-Transcriptomic Integration
published: 2026-08-14T14:56:31Z
authors: Julian Ostermaier, Swann Ruyter, Reuben Dorent, Daniel Racoceanu
url: http://arxiv.org/abs/2608.14355v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Disentangled Shared Representations Improve Morpho-Transcriptomic Integration

## Abstract
Spatial transcriptomics (ST) enables the simultaneous profiling of gene expression and tissue morphology, creating an opportunity to learn multimodal representations capturing shared morpho-transcriptomic structure. However, standard multimodal models often compress modalities into a common latent space without explicitly separating shared and modality-specific sources of variation, which may limit downstream utility. We investigate whether explicit disentanglement of shared and private latent components improves multimodal representation learning for paired Hematoxylin \& Eosin (H\&E) and ST data. We compare VAE-based and contrastive approaches, each in standard and disentangled variants, across two cancer cohorts under matched experimental conditions. Representations are evaluated using cross-modal reconstruction, downstream probing and cross-modal probe transfer. The experiments suggest two main trends. First, contrastive objectives yield higher downstream probing performance than VAE-based models. Second, disentangled variants improve the selected reconstruction and probing metrics, although the gains depend on the model family, task, direction, and disentanglement strength. Overall, our results suggest that explicitly factorizing shared and modality-specific information can improve multimodal representation learning for spatial transcriptomics and provides a useful evaluation framework for future foundation models.

## Metadata
- **Published**: 2026-08-14T14:56:31Z
- **Authors**: Julian Ostermaier, Swann Ruyter, Reuben Dorent, Daniel Racoceanu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14355v1)