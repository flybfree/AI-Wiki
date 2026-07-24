---
title: Hypothesis-and-Refinement Learning of Organic Structures from Multimodal Spectroscopic Data
published: 2026-07-22T06:50:53Z
authors: Chengchun Liu, Zhiyuan Yan, Li Yuan, Hao Li, Boxuan Zhao, Yonghong Tian, Bartosz A. Grzybowski, Fanyang Mo
url: http://arxiv.org/abs/2607.19816v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hypothesis-and-Refinement Learning of Organic Structures from Multimodal Spectroscopic Data

## Abstract
Determining molecular structures from spectroscopic data remains fundamentally challenging because the inverse problem is intrinsically underdetermined: individual spectra are sparse, low-dimensional, and encode only partial structural evidence relative to the vast space of possible molecules. We address this challenge by formulating automated structure elucidation as a scalable hypothesis-refinement paradigm that tightly integrates spectral evidence with large-scale molecular priors. To supply structure-resolving NMR signals for multimodal learning, we construct \textbf{QM9SPIN}, a DFT-derived dataset comprising diverse 1D and 2D spectra, including J-coupling, DEPT experiments, and explicit spin--spin interactions. On this foundation, we introduce \textbf{SpectroMol}, a spectrum-to-structure model that proposes chemically valid molecular hypotheses conditioned on multimodal spectral inputs. Complementarily, we develop \textbf{MS-Mol2Mol}, a high-resolution mass-constrained molecular generator that integrates molecular formula, exact mass, and degree of unsaturation within a conditional generative prior trained on 400 million molecules, ensuring global compositional consistency and chemically realistic refinement. The integrated system achieves 93.8\% top-1 accuracy on the simulated benchmark, adapts effectively from simulated to experimental spectra with limited experimental fine-tuning, and further improves experimental predictions through mass-guided refinement, establishing a scalable route toward automated, data-driven organic structure elucidation.

## Metadata
- **Published**: 2026-07-22T06:50:53Z
- **Authors**: Chengchun Liu, Zhiyuan Yan, Li Yuan, Hao Li, Boxuan Zhao, Yonghong Tian, Bartosz A. Grzybowski, Fanyang Mo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19816v1)