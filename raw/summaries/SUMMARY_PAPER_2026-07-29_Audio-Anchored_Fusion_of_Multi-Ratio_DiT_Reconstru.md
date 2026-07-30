---
title: Audio-Anchored Fusion of Multi-Ratio DiT Reconstruction Residuals for Cross-Domain Audio Deepfake Detection
url: http://arxiv.org/abs/2607.26472v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-29_04-55-14Z_Audio_AnchoredFusionofMulti_RatioDiTReconstruction.md
generated_at: 2026-07-29 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces an audio‑anchored fusion method that combines multi‑ratio DiT reconstruction residuals with a frozen WavLM representation to improve cross‑domain audio deepfake detection. The fused model leverages explicit residual maps from masking ratios 0.5, 0.75, and 0.9 without using gate‑based attenuation, resulting in low EER scores on ASVspoof 5 and ITW Full evaluations.

## Key Takeaways
- The multi‑ratio DiT reconstruction yields scalar‑gated additive corrections that complement the frozen WavLM embedding, lowering EER to 6.5442% on ASVspoof 5 and 13.8372% on ITW Full.  
- Three‑seed averaging produces slightly higher scores: 6.8885% (ASVspoof 5) and 15.3328% (ITW Full), still below a separately optimized WavLM‑ResNet18 baseline under both supervision settings.  
- Adding auxiliary supervision improves the fusion performance from 18.4007% to 25.2968% mean ITW EER, indicating that extra guidance can boost detection quality.

## Context
Audio deepfake detection is challenged by variations in generators, training corpora, and recording conditions, which degrade traditional models. This work addresses the need for robust, transferable detectors across domains using reconstruction‑based residuals as supplementary evidence.

## Implications
The approach provides a non‑competitive auditory path that can be applied from ASVspoof 5 to ITW Full without retraining full networks, offering practitioners a practical tool for domain transfer. It also highlights the value of residual information in deepfake detection, encouraging further research into reconstruction‑driven auxiliary supervision.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26472v1)
