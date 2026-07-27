---
title: Interpretable EEG biomarkers with bag-of-waves: Spatial and temporal waveform dictionaries for low-data regimes
url: http://arxiv.org/abs/2607.22508v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-24_17-27-43Z_InterpretableEEGbiomarkerswithbag_of_waves_Spatial.md
generated_at: 2026-07-26 21:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces bag-of-waves, an interpretable EEG analysis method that learns a small dictionary of recurring waveform templates called atoms without using labels. It converts continuous EEG into token sequences and uses simple classifiers or clustering to predict outcomes. Experiments on low-data mouse genotype clustering, spatial dementia classification, and the TUEV benchmark show performance competitive with deep models while requiring far fewer parameters.

## Key Takeaways
- bag-of-waves learns a small dictionary of atom tokens from shift-invariant k-means, enabling downstream tasks without labeled data.
- it adds n-grams to capture temporal structure and supports regional cross-channel atoms for multichannel EEG.
- the method matches deep model performance but operates with far fewer parameters and provides interpretable waveform recovery.

## Context
Current EEG analysis often relies on predefined spectral features or large neural networks that are opaque and need massive data. This work offers a lightweight alternative that balances accuracy with interpretability, addressing the data scarcity problem in neuroimaging research.

## Implications
Clinicians can directly inspect atom waveforms to validate known clinical patterns, improving trust in automated diagnosis tools. The approach makes advanced EEG analysis feasible on limited datasets, encouraging broader adoption of interpretable machine learning in medical imaging.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22508v1)
