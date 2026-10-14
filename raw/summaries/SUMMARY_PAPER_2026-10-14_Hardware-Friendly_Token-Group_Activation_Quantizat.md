---
title: Hardware-Friendly Token-Group Activation Quantization for Low-Bit Mamba Super-Resolution
url: http://arxiv.org/abs/2610.16261v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-12_06-43-58Z_Hardware_FriendlyToken_GroupActivationQuantization.md
generated_at: 2026-10-14 01:01
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper addresses the challenge of low-bit post-training quantization (PTQ) for Mamba-based super-resolution models, where the selective scan operator causes varying activation ranges across spatial tokens, making uniform clipping ineffective. The authors propose Token-Group Quantization, a hardware-friendly framework that uses a lightweight predictor to statically assign tokens to quantization groups based on pre-scan features, combined with a Frequency-Preserving Refinement objective to maintain high-frequency image structures during quantization. The method consistently outperforms existing Mamba and SR quantization baselines across multiple bit-widths, backbones, and tasks while achieving a 2.23x speedup on Jetson Orin Nano hardware.

## Key Takeaways
- Token-Group Quantization statically approximates a hardware-unfriendly post-scan grouping oracle by clustering post-scan activation descriptors during calibration to form pseudo-labels, then training a lightweight predictor that maps pre-scan features to groups at inference time. This eliminates the need for runtime statistics collection, dynamic clipping updates, or post-scan group assignment, making it compatible with static low-bit inference pipelines on edge hardware.
- The Frequency-Preserving Refinement (FPR) objective aligns Fourier amplitude and phase between full-precision teacher outputs and quantized student outputs during clipping-bound calibration. This addresses the specific degradation pattern in low-bit super-resolution where high-frequency structures such as edges and fine textures are lost, going beyond standard MSE-based calibration objectives.
- The method demonstrates broad generalizability: it transfers to Transformer-based super-resolution and Vision Mamba classification tasks, composes with rotation-based quantization techniques, and maintains consistent performance gains across multiple PTQ protocols and bit-widths, while delivering a 2.23x speedup over FP16 inference on Jetson Orin Nano, confirming its practical deployability on resource-constrained edge devices.

## Context
Mamba-based architectures have emerged as efficient alternatives to Transformer-based models for tasks like super-resolution due to their linear-complexity selective scan mechanism. However, the very property that makes Mamba efficient—input-dependent state-space operations that produce token-varying activation distributions—creates a fundamental obstacle for quantization, since traditional layer-wise or channel-wise clipping strategies assume uniform activation behavior. This paper sits at the intersection of efficient model compression and state-space model deployment, addressing a gap that prior quantization literature for Transformers does not directly solve.

## Implications
For practitioners deploying super-resolution on edge devices such as Jetson hardware, this work provides a practical path to running Mamba-based restoration models at low bit-widths without sacrificing perceptual quality, enabling real-time image enhancement on constrained hardware. For the broader quantization research community, the token-group approach and the frequency-preserving calibration objective offer transferable ideas that extend beyond Mamba to any architecture with input-dependent activation distributions, potentially informing future PTQ methods for state-space models, diffusion models, and other non-uniform activation architectures.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.16261v1)
