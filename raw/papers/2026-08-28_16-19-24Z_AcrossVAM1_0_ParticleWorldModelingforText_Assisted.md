---
title: AcrossVAM1.0: Particle World Modeling for Text-Assisted Robot Video Prediction
published: 2026-08-28T16:19:24Z
authors: Yafei Zhang, Nan Wu
url: http://arxiv.org/abs/2608.28491v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AcrossVAM1.0: Particle World Modeling for Text-Assisted Robot Video Prediction

## Abstract
Predicting robot videos requires both precise motion reasoning and preservation of high-frequency appearance, yet monolithic pixel models entangle these objectives and often conceal their progress behind a strong last-frame baseline. We present AcrossVAM1.0, a lightweight, text-assisted video action model that factorizes future prediction into object-centric motion and dense appearance. A frozen SAM3-DLP codec decomposes four context frames into semantic particles for the robot, arm, and gripper, together with a background latent. A 0.28M-parameter spatio-temporal Transformer aligns particle identities, rolls their states forward, and is modulated by a frozen OpenCLIP instruction embedding through FiLM. A causal dual-stream decoder combines particle-rendered motion with appearance encoded exclusively from the last observed frame; a residual refiner and learned delivery mask produce five future frames without access to future appearance. On our VRS benchmark constructed from diverse real-robot trajectories, particle dynamics reduce trajectory error by 21.0\% over persistence. Across three delivery-mask seeds, AcrossVAM1.0 improves future-frame PSNR/SSIM from 19.97/0.796 to 20.573/0.8004, while raw particle generation improves motion-region PSNR from 11.89 to 13.23. The delivered model does not yet beat persistence in LPIPS, and correct-versus- shuffled language changes trajectory error by only 2.8--3.1%. We report these limitations alongside oracle, negative-control, multi-seed, and per-robot analyses. The results show that explicit particle dynamics are a promising low-dimensional interface for robot video prediction, while robust language grounding and appearance delivery remain the principal open challenges.

## Metadata
- **Published**: 2026-08-28T16:19:24Z
- **Authors**: Yafei Zhang, Nan Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28491v1)