---
title: CADENCE: A Cardiac Atom Dictionary for Interpretable Neural Concept Extraction from ECG Foundation Models
published: 2026-07-28T03:38:03Z
authors: Yixuan Duan, Arjun Naik, Sadeer Al-Kindi, Wei Qiu
url: http://arxiv.org/abs/2607.25244v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CADENCE: A Cardiac Atom Dictionary for Interpretable Neural Concept Extraction from ECG Foundation Models

## Abstract
Foundation models for 12-lead electrocardiograms (ECGs) transfer well across clinical tasks, but the physiological knowledge encoded in their representations remains opaque. We present CADENCE, a framework that decomposes an ECG foundation model into a human-interpretable, queryable dictionary of physiological concepts. Using a BatchTopK sparse autoencoder, CADENCE factorizes Layer-6 embeddings from more than nine million ECG tokens into 8,192 sparse cardiac atoms. These atoms align better than individual dense embedding dimensions with clinical phenotypes and waveform morphology, recovering arrhythmias, conduction abnormalities, infarction and repolarization patterns, chamber and axis findings, and lead- and beat-phase-specific waveform primitives. At Layer 6, the best atoms achieve mean AUROCs of 0.88 for clinical phenotypes and 0.90 for morphology, versus 0.78 and 0.83 for the best dense dimensions. Sparse atom probes match or outperform dense probes for phenotype, morphology, and age prediction while attributing each prediction to a small set of interpretable atoms; phenotype AUROC improves from 0.93 to 0.95. Atom-space geometry recovers physiologically coherent relationships, and targeted atom ablation selectively changes frozen downstream outputs. An automated LLM pipeline generates and quantitatively validates atom descriptions by predicting held-out activations. On independent external ECG datasets, CADENCE recovers overlapping concepts and maintains consistent phenotype-prediction performance. CADENCE provides a scalable framework for discovering and auditing the physiological knowledge encoded by ECG foundation models.

## Metadata
- **Published**: 2026-07-28T03:38:03Z
- **Authors**: Yixuan Duan, Arjun Naik, Sadeer Al-Kindi, Wei Qiu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25244v1)