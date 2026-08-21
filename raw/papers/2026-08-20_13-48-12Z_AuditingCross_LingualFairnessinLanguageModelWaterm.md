---
title: Auditing Cross-Lingual Fairness in Language Model Watermarking
published: 2026-08-20T13:48:12Z
authors: Alexander Nemecek, Osama Zafar, Debargha Ganguly, Vikash Singh, Vipin Chaudhary, Erman Ayday
url: http://arxiv.org/abs/2608.20047v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Auditing Cross-Lingual Fairness in Language Model Watermarking

## Abstract
Watermarking schemes for large language model output are evaluated almost exclusively on English text using each scheme's detection threshold and a narrow set of quality measurements. Multilingual deployment exposes evaluation-design choices that are inconsequential on English but determine conclusions cross-lingually. We propose an evaluation framework with four components: detection thresholds calibrated empirically per deployment context, a threshold-independent companion measurement that distinguishes calibration failures from detection failures, three disjoint quality measurement paradigms (distributional, paired-semantic, and reference-perplexity), and a generalized-entropy decomposition of cross-language disparity over a typological family partition. Applied to six watermarking schemes, three open-weight generators, eleven languages spanning four scripts and eight typological families, and both base and instruction-tuned regimes, the framework reveals failure modes that single-language single-paradigm evaluation cannot surface. Across detection and quality, observed disparity is predominantly between-family on the typological partition, indicating that cross-lingual fairness gaps in watermarking are structural to language properties rather than idiosyncratic to particular languages.

## Metadata
- **Published**: 2026-08-20T13:48:12Z
- **Authors**: Alexander Nemecek, Osama Zafar, Debargha Ganguly, Vikash Singh, Vipin Chaudhary, Erman Ayday
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20047v1)