---
title: On the Resilience of Text-to-Video Diffusion Models to Hardware Faults
published: 2026-08-30T06:41:51Z
authors: Zachary Coalson, A M Aahad, Stella Doehring, Zane Ma, Sanghyun Hong
url: http://arxiv.org/abs/2608.29598v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# On the Resilience of Text-to-Video Diffusion Models to Hardware Faults

## Abstract
We present the first systematic study of the resilience of text-to-video (T2V) diffusion models under random hardware-level faults. While T2V models are widely used for automated video generation due to their ability to produce high-quality, temporally coherent, and realistic videos, their iterative denoising process and spatiotemporal dependencies introduce unique failure modes. We perform an extensive fault-injection study covering both computational and memory faults across three T2V models and a representative benchmark. Our results show that (1) a single fault can degrade overall performance by up to 3.7\%, with semantic correctness more affected than perceptual quality; (2) memory faults are more damaging than computational faults, high-order exponent bits are particularly vulnerable, and the widely-used bfloat16 is more susceptible than alternative formats; and (3) 7-28\% of faults cause visible artifacts, including semantic changes such as added objects, suggesting that single faults are sufficient to alter output semantics. Our findings reveal reliability risks in deployed T2V systems and motivate further research on improving fault resilience. Code: \href{https://github.com/ztcoalson/T2V-Resilience}{https://github.com/ztcoalson/T2V-Resilience}.

## Metadata
- **Published**: 2026-08-30T06:41:51Z
- **Authors**: Zachary Coalson, A M Aahad, Stella Doehring, Zane Ma, Sanghyun Hong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29598v1)