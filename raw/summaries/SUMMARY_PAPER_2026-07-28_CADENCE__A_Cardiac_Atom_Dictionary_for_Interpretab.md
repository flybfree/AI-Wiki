---
title: CADENCE: A Cardiac Atom Dictionary for Interpretable Neural Concept Extraction from ECG Foundation Models
url: http://arxiv.org/abs/2607.25244v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_03-38-03Z_CADENCE_ACardiacAtomDictionaryforInterpretableNeur.md
generated_at: 2026-07-28 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CADENCE, a method that extracts interpretable physiological concepts from the hidden representations of ECG foundation models by decomposing Layer‑6 embeddings into sparse “cardiac atoms.” The framework demonstrates that these atomic probes outperform dense embedding dimensions in predicting clinical phenotypes and waveform morphology, achieving higher AUROCs. An automated LLM pipeline validates atom descriptions against held‑out activations, confirming their interpretability.

## Key Takeaways
- CADENCE factorizes nine million ECG tokens into 8,192 sparse cardiac atoms that align better with clinical phenotypes than individual dense dimensions.
- The best atoms reach AUROCs of 0.88 for phenotype and 0.90 for morphology, surpassing the 0.78 and 0.83 of dense probes.
- Phenotype prediction AUROC improves from 0.93 to 0.95 after using sparse atom probes.

## Context
Current ECG foundation models excel at transferring knowledge across tasks but their internal representations are opaque, limiting clinical trust and interpretability. Sparse decompositions that map embeddings to human‑readable concepts could bridge this gap by providing transparent biomarkers for model behavior.

## Implications
For clinicians, CADENCE offers a way to audit what physiological information the model relies on, enabling targeted interventions when atom ablation changes predictions. For developers, the framework provides a scalable tool to improve model transparency and regulatory compliance in AI‑driven cardiac diagnostics.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25244v1)
