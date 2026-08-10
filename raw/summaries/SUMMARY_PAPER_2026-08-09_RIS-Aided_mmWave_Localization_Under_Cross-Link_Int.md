---
title: RIS-Aided mmWave Localization Under Cross-Link Interference via Beam-Domain ML Fingerprinting
url: http://arxiv.org/abs/2608.07444v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_17-28-33Z_RIS_AidedmmWaveLocalizationUnderCross_LinkInterfer.md
generated_at: 2026-08-09 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a beam-domain fingerprint framework that maps received signal‑to‑noise ratio (SNR) across predefined RIS reflection states to UE azimuth and range without CSI. It extends the approach to interference from cross‑link interferers, producing an SINR fingerprint while keeping the interference level interpretable via INR constraints. Machine‑learning regressors are evaluated under both clean and interference conditions.

## Key Takeaways
- KNN achieves the lowest angle MAE of 0.37° and range MAE of 4 cm in a clean 28 GHz simulation with a 20×20 RIS, but degrades to 1.4° and 7.6 cm when cross‑link interference is present.  
- The angle estimation suffers more than range estimation under interference because location information is encoded asymmetrically in the beam‑domain fingerprint.  
- An INR‑constrained calibration strategy maintains physical interpretability of the interference level, preventing it from overwhelming the SNR fingerprint.

## Context
This work advances AI‑driven localization for 6G networks by leveraging machine learning to decode spatial cues directly from RIS beam patterns. It highlights how signal quality and interference can be transformed into interpretable ML features, aligning with broader trends in edge‑computing and real‑time channel estimation.

## Implications
Practitioners can deploy these fingerprint models on reconfigurable surfaces to improve UE tracking efficiency without costly CSI acquisition. The demonstrated robustness under interference suggests a practical path toward reliable beam management in dense 6G environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07444v1)
