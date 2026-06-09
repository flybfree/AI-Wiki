---
title: When Eyes Betray AI: Social Gaze Consistency as a Semantic Cue for AI-Generated Image Detection
published: 2026-05-26T17:50:17Z
authors: Kim Jihyeon, Sohee Kim, Soosan Lee, Souhwan Jung, James Matthew Rehg, Hyesong Choi
url: http://arxiv.org/abs/2605.27348v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Eyes Betray AI: Social Gaze Consistency as a Semantic Cue for AI-Generated Image Detection

## Abstract
Recent generative models have largely closed the gap on low-level artifacts - pixel fingerprints, frequency anomalies, upsampling traces - particularly in person-centric and partial-edit settings where the manipulated region is small and surrounded by photometrically authentic content. We introduce Social Gaze Consistency, a high-level semantic cue defined as the mutual coherence of gaze direction, head-eye alignment, and pupil placement between interacting individuals, and show that it constitutes a previously underutilized detection axis orthogonal to existing low-level paradigms. We instantiate this insight through three coupled mechanisms: (i) a controlled diagnostic dataset with region-specific perturbations of gaze-consistent imagery, where strict pair-level grouping forecloses generator-fingerprint memorization as an optimization-time shortcut rather than relying on augmentation; (ii) Block-Compositional Caption Supervision, which holds a single 5-block reasoning skeleton invariant across 1,250 macro-combined captions, decoupling reasoning consistency from surface diversity; (iii) Cross-architecture validation showing the same supervision improves a vision-language backbone (FakeVLM) by +3.7 pp on the COCOAI Interaction subset (balanced accuracy 67.8 -> 71.5) and +1.3 pp on the COCOAI Person subset (83.0 -> 84.3), with consistent gains on a vision-only backbone (Effort), evidencing a backbone-agnostic cue. Real- and fake-class recalls rise simultaneously, ruling out a "predict-all-fake" artifact. A four-step mechanistic account - paired-edit shortcut blocking, hard-to-easy difficulty transfer, CLIP prior preservation, and diffusion-family shared spectral weakness in periocular structure - explains why training on a single inpainter (FLUX.1-Fill) transfers to multi-generator suites. We will release the code upon acceptance to facilitate reproducibility.

## Metadata
- **Published**: 2026-05-26T17:50:17Z
- **Authors**: Kim Jihyeon, Sohee Kim, Soosan Lee, Souhwan Jung, James Matthew Rehg, Hyesong Choi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.27348v1)