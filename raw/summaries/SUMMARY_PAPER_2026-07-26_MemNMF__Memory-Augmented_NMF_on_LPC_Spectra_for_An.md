---
title: MemNMF: Memory-Augmented NMF on LPC Spectra for Anomalous Sound Detection
url: http://arxiv.org/abs/2607.22086v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-24_08-34-12Z_MemNMF_Memory_AugmentedNMFonLPCSpectraforAnomalous.md
generated_at: 2026-07-26 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MemNMF, a memory‑augmented NMF method that processes Linear Predictive Coding spectra to detect anomalous sounds in machine condition monitoring. Experiments on MIMII and DCASE 2020 Task 2 show that the approach improves over standard autoencoders and provides stronger robustness under noisy, non‑stationary conditions.

## Key Takeaways
- MemNMF leverages an NMF dictionary learned from normal LPC spectra to initialize a memory module that stores prototypical spectral patterns.  
- The reconstruction of each input is performed as an attention‑weighted blend of these stored patterns, which reduces sensitivity to noise and transients compared with spectrogram autoencoders.  
- Experiments demonstrate that the method yields further gains over baseline autoencoders, especially when operating under noisy or non‑stationary machine conditions.

## Context
Autoencoder‑based anomaly detection is widely used for condition monitoring because it requires only normal data and produces interpretable reconstruction errors. However, most implementations rely on spectrogram representations which struggle with transient noise, limiting separation between normal and anomalous signals.

## Implications
This work provides a more robust framework that can be integrated into existing machine health‑monitoring pipelines without retraining large models. Practitioners can achieve higher detection accuracy in real‑world noisy environments, leading to earlier fault identification and reduced downtime.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22086v1)
