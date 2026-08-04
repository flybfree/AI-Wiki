---
title: Interpretable MEG Decoding of Perceived Speech: Cortical Sources and the Stimulus Features That Drive Retrieval
url: http://arxiv.org/abs/2608.01481v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_20-28-14Z_InterpretableMEGDecodingofPerceivedSpeech_Cortical.md
generated_at: 2026-08-03 23:34
model: nvidia/nemotron-3-nano-4b
---

## Summary  
This paper introduces a new MEG decoding architecture that learns to retrieve short speech segments from magnetoencephalographic data using a CLIP‑style objective against wav2vec 2.0 embeddings. The model maps network weights onto cortical sources, revealing which auditory features drive retrieval and showing higher accuracy with far fewer parameters than prior approaches.

## Key Takeaways  
- The spherical harmonic spatial attention replaces the flattened sensor layout, yielding a representation that aligns with three‑dimensional source space and reduces subject‑specific branches from 270 to 25.  
- Paired MEG occlusion experiments identify fifteen of nineteen stimulus features as significant, with silence, intensity, vowels, and acoustic onsets having the largest impact on retrieval accuracy.  
- The wav2vec target can be compressed to twelve learned dimensions without loss, whereas excessive temporal compression degrades performance.

## Context  
The work bridges deep language models and non‑invasive neuroimaging by demonstrating that auditory perception can be decoded from MEG signals with clinical relevance. It also highlights the importance of preserving temporal dynamics in feature extraction for reliable retrieval tasks.

## Implications  
For researchers, this approach offers a lightweight, source‑aware decoding framework that could improve real‑time speech monitoring and assistive technologies. In industry, it enables scalable deployment of EEG/MEG‑based speech recognition without sacrificing accuracy or requiring extensive training data.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01481v1)
