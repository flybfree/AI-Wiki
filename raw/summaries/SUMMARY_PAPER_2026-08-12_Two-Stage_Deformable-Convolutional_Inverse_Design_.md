---
title: Two-Stage Deformable-Convolutional Inverse Design of Nanophotonic Absorbers from Optical Spectra
url: http://arxiv.org/abs/2608.11860v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_09-47-06Z_Two_StageDeformable_ConvolutionalInverseDesignofNa.md
generated_at: 2026-08-12 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a two‑stage deformable‑convolutional inverse design method that reconstructs metal–insulator–metal resonator geometries from an 80‑dimensional absorption spectrum. The framework projects the spectrum into a latent space, decodes it to a 64 × 64 mask, and refines the result with adversarial learning. Experiments show state‑of‑the‑art reconstruction metrics compared with plain convolution.

## Key Takeaways
- The model maps an 80‑dimensional absorption spectrum onto a $150\times4\times4$ latent representation before decoding it into a $64\times64$ resonator mask, enabling precise geometry generation.  
- Training uses supervised reconstruction followed by least‑squares adversarial refinement starting from the best supervised checkpoint, which yields higher PSNR and SSIM than plain convolution alone.  
- Deformable sampling with adaptive offsets at coarse and intermediate decoder stages improves reconstruction quality, as evidenced by Dice score of 0.9623 and IoU of 0.9342.

## Context
Inverse design in nanophotonics traditionally relies on manual optimization or limited data‑driven approaches that struggle with non‑unique mappings from spectra to structures. This work leverages deep learning to automate the mapping, demonstrating how generative models can handle high‑dimensional spectral inputs and produce fine geometric features automatically.

## Implications
The improved reconstruction capabilities reduce development time for custom absorbers, allowing rapid prototyping of photonic devices without extensive trial‑and‑error. Practitioners in photonics research and industry can adopt this framework to generate tailored nanostructures that match specific optical requirements efficiently.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11860v1)
