---
title: Quantizing Diffusion LLMs under Parallel Decoding: Commitment Risk and the Parallelism Tax
published: 2026-11-23T12:27:42Z
authors: Huan Xu, Maosen Zhao, Pengtao Chen, Tao Chen
url: http://arxiv.org/abs/2611.30587v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Quantizing Diffusion LLMs under Parallel Decoding: Commitment Risk and the Parallelism Tax

## Abstract
Diffusion large language models (dLLMs) are served with accelerated decoders that cache context and commit, in one step, every masked position whose confidence clears a threshold. Yet post-training quantization of dLLMs has so far been calibrated and evaluated under fixed-step samplers without caching. We study W4A4 quantization under the deployed decoder and find that the decoder determines both where quantization harms accuracy and what it costs. Irreversible errors enter chiefly through forced commitments, made when no position clears the threshold: they are a minority of commitments but carry most quantization-induced flips. Quantization also levies a parallelism tax, extra forward passes per response: by compressing top logit gaps, it pushes positions below the threshold while leaving predictions largely intact. We propose DECAL, which reweights layer-wise calibration by a commitment-risk prior measured on the deployed decoder, and an argmax-preserving commit temperature that recovers the tax. On LLaDA and Dream, DECAL attains the best average accuracy among W4A4 methods, with lower run-to-run variance than the closest existing calibration method.

## Metadata
- **Published**: 2026-11-23T12:27:42Z
- **Authors**: Huan Xu, Maosen Zhao, Pengtao Chen, Tao Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.30587v1)