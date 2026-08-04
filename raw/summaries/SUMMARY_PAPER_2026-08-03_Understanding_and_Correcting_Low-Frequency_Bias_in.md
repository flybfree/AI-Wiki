---
title: Understanding and Correcting Low-Frequency Bias in EEG Foundation Model
url: http://arxiv.org/abs/2608.01898v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_08-36-10Z_UnderstandingandCorrectingLow_FrequencyBiasinEEGFo.md
generated_at: 2026-08-03 23:30
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates a persistent low‑frequency bias that appears in EEG foundation models despite variations in data volume, model size, or training objectives. The authors show that the $1/f^α$ spectral shape of EEG and neural networks’ preference for low‑frequency components create an imbalance, especially when masked autoencoders use $\ell_2$ reconstruction loss. Their solution is FAME, a frequency‑balanced masked autoencoding method that treats each EEG band as an independent target with equal weighting. Evaluated across 41 tasks in OmniEEG‑Bench, FAME yields more spectrally balanced representations and state‑of‑the‑art results on 24 tasks.

## Key Takeaways
- The $1/f^α$ nature of EEG and neural networks’ bias toward low frequencies cause a persistent underrepresentation of high‑frequency content.  
- In masked autoencoders, $\ell_2$ reconstruction amplifies this imbalance because high‑power low‑frequency components dominate the loss even when relative errors are similar.  
- FAME resolves the issue by standardizing band‑specific targets and assigning equal loss weight across EEG frequency bands.

## Context
EEG foundation models aim to learn universal representations for diverse downstream tasks, yet their performance plateaus due to inherent data biases. This work highlights how spectral characteristics can undermine pretraining objectives, a problem that has not been fully addressed in prior literature on neural network bias correction.

## Implications
Balanced spectral supervision is crucial for reliable transfer learning across EEG applications such as brain‑computer interfaces and neurodiagnostics. Practitioners can adopt FAME to improve model robustness and avoid overfitting to low‑frequency noise, leading to more generalizable and accurate systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01898v1)
