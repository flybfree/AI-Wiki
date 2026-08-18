---
title: CytoBERT: A Foundation Model for Cytometry Data
published: 2026-08-14T15:57:35Z
authors: Syed Abdul Haseeb Qadri, Bjarne C. Hiller, Felix Blanke, Vanja Sophie Cangalovic, Kutalmış Coşkun, Amin Mirzaei, Tom Siegl, Sebastian Bader, Thomas Kirste, Martin Becker
url: http://arxiv.org/abs/2608.14414v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CytoBERT: A Foundation Model for Cytometry Data

## Abstract
Cytometry measures the complex characteristics of single cells (e.g., counts and protein expression of immune cells) and is widely used across immunological research and clinical settings. However, cytometry data is highly heterogeneous and unstandardized due to experimental protocols and the choice of measured features. While machine learning methods hold the potential to gain deeper insights into cell biology, these challenges make them difficult to apply and transfer across studies. Recent advances in foundation models can alleviate these issues, but corresponding approaches are still scarce in this field. To address this, we provide CytoBERT, a publicly available, open-source, open-weight foundation model for single-cell cytometry data with variable marker panels. CytoBERT is pretrained in a self-supervised manner on a large-scale cytometry corpus (15 human datasets with heterogeneous marker panels and more than 50 million cells) curated through marker standardization, enabling it to learn transferable inter-marker relationships within cells. Fine-tuning CytoBERT for sample-level classification demonstrates that transfer learning across heterogeneous cytometry datasets is feasible, providing a starting point for scalable, generalizable cytometry analysis. Code is available at GitHub.

## Metadata
- **Published**: 2026-08-14T15:57:35Z
- **Authors**: Syed Abdul Haseeb Qadri, Bjarne C. Hiller, Felix Blanke, Vanja Sophie Cangalovic, Kutalmış Coşkun, Amin Mirzaei, Tom Siegl, Sebastian Bader, Thomas Kirste, Martin Becker
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14414v1)