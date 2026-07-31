---
title: VESTIGE: A Knowledge-Guided Masking Strategy for Corruption-Aware Fine-Tuning of Genomic Transformers, Validated on Ancient DNA Reconstruction
published: 2026-07-30T05:47:47Z
authors: Angshuman Chakravertty, Rahul Maheshwari
url: http://arxiv.org/abs/2607.27712v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VESTIGE: A Knowledge-Guided Masking Strategy for Corruption-Aware Fine-Tuning of Genomic Transformers, Validated on Ancient DNA Reconstruction

## Abstract
Standard masked-language-model fine-tuning applies a uniform masking probability across every token position, assuming reconstruction difficulty is position-agnostic. When the degradation process is characterised and concentrated at predictable positions, this assumption fails: at peak damage sites the model can underperform a frequency-matched random predictor. We introduce VESTIGE, a parameter-free, drop-in replacement for the standard MLM collator that aligns the masking distribution with an empirically measured per-position corruption profile. We apply it to ancient DNA (aDNA) reconstruction, where cytosine deamination produces a position-dependent C-to-T / G-to-A gradient quantified per-position by mapDamage2. Rescaling so the mean C/G masking rate equals 15% - identical to standard MLM - isolates spatial redistribution as the sole variable, with model, data, seed, and hyperparameters held fixed across both DNABERT-2 runs on a mammoth CDS corpus (two specimens, seven genes). Across six terminal-zone widths and 626 paired windows, VESTIGE leads standard MLM at every width (Delta = +4.18 to +10.35 pp, all p < 10^-8), cuts validation cross-entropy by 13% (3.274 vs. 3.757), and yields ESMFold reconstructions with TM-score > 0.95 across all six reconstructions (three genes) even under damage amplified 10-30x beyond authentic PMD rates. A 1D CNN biosecurity classifier returns AUC = 0.935 and clears 98.2% of reconstructed windows, the 1.76% remainder attributable to reference-genome features, not reconstruction artefacts. The principle is domain-agnostic: any measurable position- or context-specific corruption profile - FFPE, bisulfite, metagenomic, or nanopore - substitutes directly for the PMD array, making VESTIGE a knowledge-guided training routine for intelligent systems operating on degraded or noisy sequence inputs.

## Metadata
- **Published**: 2026-07-30T05:47:47Z
- **Authors**: Angshuman Chakravertty, Rahul Maheshwari
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27712v1)