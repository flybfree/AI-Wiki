---
title: CRAFT: Compression via Recursive Adaptive Fusion of Video Tokens for Vision-Language Models
url: http://arxiv.org/abs/2608.01644v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_03-27-46Z_CRAFT_CompressionviaRecursiveAdaptiveFusionofVideo.md
generated_at: 2026-08-03 23:12
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces CRAFT, a token‑compression technique for vision‑language models that recursively merges video tokens while preserving spatial‑temporal information. Experiments demonstrate an 8× compression ratio with only a ~3% drop in accuracy compared to the original backbone.

## Key Takeaways  
- Global similarity determines which tokens to merge, enabling parameter‑free selection of tokens for fusion.  
- A position‑aware weighting module and a content‑adaptive channel‑wise gate learn how to fuse retained tokens together.  
- The compression pipeline is query‑agnostic; each retained token remains a linear combination of the originals, preserving true coordinates and alignment with the language model’s input distribution.

## Context  
Video understanding in multimodal AI relies on VLMs that ingest large numbers of visual tokens, inflating computational cost. Efficiently compressing these sequences without sacrificing performance is a key challenge for scalable deployment. This work provides a principled method to balance efficiency and adaptivity.

## Implications  
For industry, CRAFT enables smaller models that can run on edge devices while maintaining high accuracy. For researchers, it offers a reusable framework for compressing sequential data in multimodal systems, reducing resource demands without compromising downstream task performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01644v1)
