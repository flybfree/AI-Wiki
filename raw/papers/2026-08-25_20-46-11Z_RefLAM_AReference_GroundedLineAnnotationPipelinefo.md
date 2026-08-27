---
title: RefLAM: A Reference-Grounded Line Annotation Pipeline for Historical Arabic Manuscripts
published: 2026-08-25T20:46:11Z
authors: Mohamed Guechaoui, Mohamed Diaa Zellagui, Souleyman Chaib, Sahraoui Dhelim
url: http://arxiv.org/abs/2608.25140v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RefLAM: A Reference-Grounded Line Annotation Pipeline for Historical Arabic Manuscripts

## Abstract
Existing approaches to building line-level Arabic handwritten-text-recognition (HTR) training data either rely on fully manual annotation, which does not scale, or on automatic OCR-to-reference alignment methods not yet extended to multi-script, two-zone (main-plus-margin) manuscript layouts with a provable correctness guarantee. We present RefLAM (Reference-grounded Line Annotation for Manuscripts), a pipeline converting manuscript page images and clean transcriptions into validated, line-level ground truth without sacrificing human oversight. RefLAM couples a deep-learning page-segmentation model with a multimodal large language model (MLLM) for structured OCR and a diacritic-agnostic fuzzy alignment engine that grounds each OCR line in a contiguous span of the reference text, with a character-level confidence score in $[0,100]$. A perfect score is provably equivalent to character-for-character identity of the normalised strings (the Confidence-100 rule), verified with no counterexample across the released corpus. A reviewer can thus trust a perfect score, confirming most lines at a glance rather than retyping them, so annotation becomes triaged, with attention concentrated on uncertain alignments. Across 7 fully page-validated books we measured a 75$\times$ throughput gain over manual annotation (3,000 vs. 40 lines/hr); applying the same guarantee to 7 further books, we retained 16,533 confidence-100 main-text lines within one week, excluding sub-100 lines rather than manually correcting them. Using RefLAM, we release AraMS-28k: 14 historical Arabic manuscript books, 3,043 pages, and 27,971 main-text and 629 margin-line annotations with bounding boxes, layout labels, and insertion anchors for 191 margin entries (30.4%). We also finetune Muharaf-pretrained baselines (including HATFormer) on AraMS-28k and report CER results confirming its practical utility for downstream HTR training.

## Metadata
- **Published**: 2026-08-25T20:46:11Z
- **Authors**: Mohamed Guechaoui, Mohamed Diaa Zellagui, Souleyman Chaib, Sahraoui Dhelim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25140v1)