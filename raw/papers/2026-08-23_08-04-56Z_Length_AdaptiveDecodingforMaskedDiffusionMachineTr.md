---
title: Length-Adaptive Decoding for Masked Diffusion Machine Translation
published: 2026-08-23T08:04:56Z
authors: Yan Zhan, Mengkai Hou, Wanting Zhang, Zhijun Gao
url: http://arxiv.org/abs/2608.22274v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Length-Adaptive Decoding for Masked Diffusion Machine Translation

## Abstract
Machine translation tests masked diffusion language models (dLLMs) because every source token must be rendered faithfully, while fixed canvas decoding must choose target length before denoising. Existing masked diffusion decoding work mainly studies token unmasking order, leaving this length decision under-explored despite its direct effect on coverage and redundancy. We introduce Entropy-Valley (EV), a training-free length selector that scores candidate target canvases by mean predictive entropy from all-mask forward passes and selects the canvas the backbone is most prepared to fill. Relative to a baseline using training corpus length statistics, EV recovers 64.9%, 65.3%, and 33.0% of the COMET-22 gain from reference target lengths on En$\to$Zh, Zh$\to$En, and En$\to$De. Our diagnostics show that denoising-friendly lengths need not match reference lengths. Evaluation by three translation experts supports the En$\leftrightarrow$Zh adequacy gains, with stronger evidence on Zh$\to$En. Compared with a LLaMA-3-8B autoregressive (AR) model trained on the same fine-tuning data, the EV system ties on En$\to$Zh and leads on Zh$\to$En; an oracle-length diagnostic further shows that, in this masked diffusion MT setting, deciding which tokens to reveal first matters less than how the target length is supplied.

## Metadata
- **Published**: 2026-08-23T08:04:56Z
- **Authors**: Yan Zhan, Mengkai Hou, Wanting Zhang, Zhijun Gao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22274v1)