---
title: Autoregressive EHR Foundation Models with Multimodal Inputs
url: http://arxiv.org/abs/2607.22264v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-24_12-59-20Z_AutoregressiveEHRFoundationModelswithMultimodalInp.md
generated_at: 2026-07-26 21:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes an autoregressive foundation model for electronic health records that can be conditioned on multiple clinical modalities such as ECG waveforms, chest X-ray images and notes. Experiments on MIMIC-IV show that the best latent‑compression configurations outperform uncompressed cross‑attention and mean pooling. Adding auxiliary modalities does not guarantee better ICU mortality prediction without careful design.

## Key Takeaways
- The model uses modality‑specific latent compression to shorten long sequences like ECG time series before they enter gated cross‑attention, reducing compute overhead while potentially improving generalization.
- Pretrained encoder choice matters: stronger encoders consistently give higher performance than weaker ones within each modality.
- Simply adding extra modalities does not automatically improve ICU mortality prediction; the fusion architecture and evaluation must be carefully designed.

## Context
Foundation models that process structured EHR data are advancing toward zero‑shot clinical tasks, but most ignore multimodal inputs. This work addresses a gap by integrating diverse signals in a principled way, highlighting the importance of compression strategies for long sequences.

## Implications
Clinicians and developers must consider both technical choices like encoder strength and sequence compression when building multimodal EHR models. The findings suggest that effective integration requires tailored architecture design rather than blind addition of modalities.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22264v1)
