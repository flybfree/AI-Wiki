---
title: CMuon: Accelerating and Stabilizing Diffusion Transformer Training via Chunked Momentum Orthogonalization
url: http://arxiv.org/abs/2608.02502v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_17-04-43Z_CMuon_AcceleratingandStabilizingDiffusionTransform.md
generated_at: 2026-08-03 23:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses the computational bottleneck of training diffusion transformers by improving convergence when using the Momentum Orthogonalization (Muon) optimizer. By partitioning fused weight matrices into independent chunks before orthogonalization, Chunked Muon (CMuon) achieves faster and more stable training than vanilla AdamW or standard Muon.

## Key Takeaways
- Standard DiT architectures fuse distinct weight tensors such as those in AdaLN and QKV layers, which leads to implicit subspace coupling when Muon is applied directly.  
- CMuon resolves this issue by splitting these fused matrices into independent sub‑components prior to orthogonalization, thereby preserving update direction integrity.  
- Experiments show a 675M‑parameter DiT reaches FID 1.18 on ImageNet 256 in 200 epochs using CMuon, delivering over two times the training speedup compared with AdamW and eliminating late‑stage convergence plateaus.

## Context
Diffusion transformers have set new state‑of‑the‑art benchmarks for visual generative modeling, yet their large‑scale training remains limited by inefficient optimizers. Recent momentum‑based methods like Muon promise efficiency gains but suffer from architectural incompatibilities that hinder performance.

## Implications
CMuon offers a practical upgrade to existing diffusion models, enabling researchers and industry practitioners to train massive models faster without sacrificing quality. This approach can lower computational costs and accelerate product development cycles in AI‑driven image generation services.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02502v1)
