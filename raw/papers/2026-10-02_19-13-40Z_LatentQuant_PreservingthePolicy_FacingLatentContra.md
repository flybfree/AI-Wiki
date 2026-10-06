---
title: LatentQuant: Preserving the Policy-Facing Latent Contract under NVFP4 VAE Quantization
published: 2026-10-02T19:13:40Z
authors: Ziye Deng, Lufang Chen, Shuyu Feng, Zhenwei Duan, Zicong Ye, Yu Sun, Xiaofan Li, Ruyi Gan, Hao Wang, Hao Zhang
url: http://arxiv.org/abs/2610.03959v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LatentQuant: Preserving the Policy-Facing Latent Contract under NVFP4 VAE Quantization

## Abstract
Recent world action models (WAMs) reuse pretrained video VAEs whose encoder latents directly condition downstream action policies. Quantization must therefore preserve not only reconstruction fidelity but also the policy-facing latent contract expected by the frozen policy. Direct NVFP4 leaves W4A4 quantization error uncompensated, whereas joint quantization-aware training (QAT) can recover reconstruction by moving this representation. On Wan2.1, joint QAT nearly matches FP32 VBench-7 (0.7403 versus 0.7409), yet LIBERO success collapses from 95.5% to 10.5%. Controlled decoder-only experiments show that activation quantize-dequantize operations alter the reconstruction signal and decoder Jacobian, redirecting the gradient returned to the encoder and inducing persistent latent drift. Based on this mechanism, we introduce LatentQuant, a two-stage NVFP4 QAT framework that first aligns the quantized encoder with its high-precision counterpart, then freezes it while adapting the decoder. Across Wan2.1 and Wan2.2, LatentQuant preserves near-baseline control and high reconstruction quality, achieving 95.75% success on LIBERO and 68.8% on RoboTwin. On NVIDIA B300 GPUs, NVFP4 execution achieves 1.17x-1.26x end-to-end VAE speedups over BF16 cuDNN.

## Metadata
- **Published**: 2026-10-02T19:13:40Z
- **Authors**: Ziye Deng, Lufang Chen, Shuyu Feng, Zhenwei Duan, Zicong Ye, Yu Sun, Xiaofan Li, Ruyi Gan, Hao Wang, Hao Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.03959v1)