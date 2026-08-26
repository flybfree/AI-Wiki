---
title: Validation of HRV Studio: A Transparent and Quality-Control-Aware Platform for Heart Rate Variability Analysis
published: 2026-08-25T08:45:05Z
authors: Cyrus Mexon Evrard Djindot, Faliang Liu, Sylvain Laborde, Yinjia Zhang, Jessie Chen, Ming Li, Congrong Wang, Weixiong Rao, Qinpei Zhao
url: http://arxiv.org/abs/2608.24241v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Validation of HRV Studio: A Transparent and Quality-Control-Aware Platform for Heart Rate Variability Analysis

## Abstract
Reproducibility of heart rate variability (HRV) analysis is limited by differences in preprocessing and computational conventions across software platforms. We developed HRV Studio, an open-source PyQt6-based desktop application integrating transparent HRV analysis with automated quality-control (QC) diagnostics. Validation included large-scale agreement with NeuroKit2, targeted Kubios benchmarking, spectral-method comparison, synthetic perturbation testing, recording-duration sensitivity analysis, and arrhythmia-focused QC stress testing. HRV Studio showed near-identical agreement for the widely used time-domain indices RMSSD and SDNN under matched conditions. In the primary five-minute NeuroKit2 comparison, frequency-domain median relative errors were 1.35% for LF, 0.18% for HF, and 1.41% for LF/HF, while VLF remained more convention-sensitive (37.79%). Nonlinear Poincaré indices also demonstrated high consistency. Sequence-harmonized Kubios benchmarking confirmed near-identical agreement for time-domain and nonlinear indices and strong agreement for most frequency-domain measures. Extended ten-minute analyses reproduced the same overall pattern with lower disagreement for some convention-sensitive spectral outputs. Synthetic and arrhythmia stress tests maintained 100% numerical stability while consistently triggering QC warnings. Overall, HRV Studio provides a transparent and reproducible platform for HRV research, with strong cross-platform consistency when NN sequences, preprocessing, and analytical conventions are harmonized. Stress-test results indicate computational robustness rather than clinical validation.

## Metadata
- **Published**: 2026-08-25T08:45:05Z
- **Authors**: Cyrus Mexon Evrard Djindot, Faliang Liu, Sylvain Laborde, Yinjia Zhang, Jessie Chen, Ming Li, Congrong Wang, Weixiong Rao, Qinpei Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24241v1)