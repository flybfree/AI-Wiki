---
title: Two-Step Occupation Coding
published: 2026-07-22T12:55:34Z
authors: Alexander M. Esser, Jens Dörpinghaus
url: http://arxiv.org/abs/2607.20101v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Two-Step Occupation Coding

## Abstract
Occupation coding links job titles in free text to occupational taxonomies and is a core task in labor market research. Existing approaches typically address this problem in a single end-to-end step, jointly identifying job titles and assigning occupational codes. This paper presents a novel two-step approach that separates these tasks. In the first step, a domain-specific Named Entity Recognition (NER) model identifies occupational titles in continuous text, even under noise such as OCR errors. In the second step, the extracted job titles are mapped to a taxonomy, enabling the classifier to focus exclusively on this mapping. We demonstrate that this separation improves accuracy, robustness, and interpretability compared to single-step approaches. The method has been developed for German documents but is transferable to other languages. We further introduce a margin-based confidence criterion for occupation coding, replacing common absolute thresholds. To support reproducibility, we publish the source code and evaluation scripts.

## Metadata
- **Published**: 2026-07-22T12:55:34Z
- **Authors**: Alexander M. Esser, Jens Dörpinghaus
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20101v1)