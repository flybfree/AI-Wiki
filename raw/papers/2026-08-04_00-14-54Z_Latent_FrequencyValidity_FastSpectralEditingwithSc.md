---
title: Latent-Frequency Validity: Fast Spectral Editing with Screened Video-VAE Transfer Operators
published: 2026-08-04T00:14:54Z
authors: Bowen Xue, Jiafeng Xiong, Xin Quan
url: http://arxiv.org/abs/2608.07569v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Latent-Frequency Validity: Fast Spectral Editing with Screened Video-VAE Transfer Operators

## Abstract
Direct spectral editing in video-VAE latents can control noise, flicker, smoothness, and frequency content without a decode--filter--reencode pass. However, video VAEs may redistribute pixel-space frequency bands across latent channels, and latent edits can disrupt VAE round-trip dynamics. We introduce \emph{latent-frequency validity} (LFV), which learns a compact VAE-specific spectral response and deploys it only when it improves decoded-target fidelity without worsening round-trip drift. LFV follows a validation-selected path from a diagonal per-frequency calibrator (C1) to full channel mixing (CM), making cross-channel capacity a controllable per-edit resource. Across 544 VAE--edit cells spanning six spectral families, LFV emits 423 cheap operators: 277 are handled by C1, while 146 (34.5\% of emitted operators) require channel mixing. On the primary 120-cell radial sweep, 99/100 emitted operators pass source-video-grouped held-out evaluation. Across five additional filter families, all 323 emitted operators pass held-out evaluation. Fully frozen OpenVid-fitted operators, including the validation-selected path coefficient, pass all 20 tested CogVideoX and HunyuanVideo generated-domain cells without adaptation. The selected response matches direct latent-filter latency and is about $3\times$ faster than pixel filter--reencode. The resulting maps reveal distinct VAE regimes, including strongly channel-coupled CogVideoX responses and a sharp Open-Sora high-band stability frontier.

## Metadata
- **Published**: 2026-08-04T00:14:54Z
- **Authors**: Bowen Xue, Jiafeng Xiong, Xin Quan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07569v1)