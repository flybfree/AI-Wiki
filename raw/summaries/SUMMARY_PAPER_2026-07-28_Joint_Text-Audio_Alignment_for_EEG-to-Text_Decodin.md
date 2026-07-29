---
title: Joint Text-Audio Alignment for EEG-to-Text Decoding in Chinese Speech Production and Perception
url: http://arxiv.org/abs/2607.25626v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_12-06-56Z_JointText_AudioAlignmentforEEG_to_TextDecodinginCh.md
generated_at: 2026-07-28 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes EEGAlign, a parameter‑efficient framework that jointly aligns EEG signals with both text and audio features to decode large‑vocabulary Chinese sentences from non‑invasive scalp recordings. On the ChineseEEG‑2 dataset the method achieves 82.37 % Top‑1 accuracy for reading‑aloud production and 41.43 % for passive listening among 101 candidate sentences, outperforming prior single‑axis approaches.

## Key Takeaways
- The framework combines BGE‑M3 text embeddings with wav2vec‑2.0 speech features through contrastive learning to capture both semantic and temporal information.  
- Joint alignment improves sentence classification beyond using either modality alone, as shown by consistent gains in the ablation studies.  
- The method is the first to decode large‑vocabulary Chinese sentences from EEG during overt production while maintaining strong closed‑set performance.

## Context
Current neural decoding of speech relies on invasive electrocorticography or single‑axis supervision, limiting deployment for individuals with severe impairments. This work addresses the gap by enabling non‑invasive decoding that respects the high dimensionality and variability inherent in Chinese language processing.

## Implications
The results suggest a viable path toward scalable, real‑time neural communication interfaces for speech‑impaired users, potentially reducing reliance on assistive devices. Practitioners can leverage this model to design more robust EEG‑based systems tailored to multilingual and high‑vocabulary applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25626v1)
