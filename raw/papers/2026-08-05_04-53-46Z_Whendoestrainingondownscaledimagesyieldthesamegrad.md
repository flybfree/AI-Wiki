---
title: When does training on downscaled images yield the same gradients?
published: 2026-08-05T04:53:46Z
authors: Seunghyun Ji
url: http://arxiv.org/abs/2608.04448v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When does training on downscaled images yield the same gradients?

## Abstract
Diffusion transformers deliver strong image generation, but their training cost grows superlinearly with resolution. Recent work justifies training or sampling at reduced resolution on a spectral premise: at high noise, a downscaled latent preserves almost the full surviving signal. Whether a downscaled step also preserves the native training gradient signal, however, has remained unresolved. We reduce how that signal changes under downscaling to two terms: a noise-dependent term governed by the downscale ratio, which decays at high noise as the spectral premise predicts, and a σ-independent floor governed by the target grid's absolute token count, carried by the compute graph itself and removed by no noise level. The measured (route, σ) map corroborates the account and uncovers structure the spectral picture cannot express: on the 1024->768 route, a window (0.65 < σ< 0.95), predicted by no spectral criterion at any tolerance, where the downscaled gradient stays within a small margin of the native one. Training LoRA adapters with downscaled steps restricted to the routes and noise windows the map validates reduces training time by 14.6% at a fixed step budget while remaining near-native in weight space. Code is available at https://github.com/sorryhyun/anima_lora.

## Metadata
- **Published**: 2026-08-05T04:53:46Z
- **Authors**: Seunghyun Ji
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04448v1)