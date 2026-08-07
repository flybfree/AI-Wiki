---
title: Engram-E2VID: Reference-Based Event-to-Video Reconstruction via Generative Activation of Appearance Engrams
url: http://arxiv.org/abs/2608.05728v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_08-11-11Z_Engram_E2VID_Reference_BasedEvent_to_VideoReconstr.md
generated_at: 2026-08-06 20:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Engram-E2VID, a framework that reconstructs target video frames from a reference frame and an event stream by activating appearance engrams in token space. The method links motion‑structured tokens to relevant appearance information without pixel‑wise matching, using a diffusion backbone for progressive generation. Experiments show PSNR gains of up to 3.29 dB and LPIPS reductions of up to 0.08 over strong baselines.

## Key Takeaways
- The framework encodes the reference frame into token‑space appearance engrams that serve as visual references for reconstruction.  
- Event streams are transformed into a target‑time motion scaffold that defines structural tokens guiding activation across diffusion layers.  
- One‑step diffusion enables progressive interaction between structural and appearance tokens, improving robustness to long intervals.

## Context
Reference‑based event‑to‑video synthesis remains limited by the sparse nature of event data and the difficulty of aligning temporal cues with visual content. This work addresses that gap by leveraging generative activation in a token‑space representation, offering a more flexible alternative to pixel‑wise correspondence methods.

## Implications
The approach can be applied to real‑time video editing where precise motion events must drive frame generation without heavy ground truth. Practitioners may benefit from reduced computational cost and better handling of complex motions across longer reconstruction windows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05728v1)
