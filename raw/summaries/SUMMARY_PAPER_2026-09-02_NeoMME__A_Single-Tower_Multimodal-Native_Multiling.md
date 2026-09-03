---
title: NeoMME: A Single-Tower Multimodal-Native Multilingual Foundation Encoder for Efficient Fine-Tuning and Inference
url: http://arxiv.org/abs/2609.01657v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-08-31_13-08-15Z_NeoMME_ASingle_TowerMultimodal_NativeMultilingualF.md
generated_at: 2026-09-02 20:53
model: nvidia/nemotron-3-nano-4b
---

## Summary
NeoMME is a family of multimodal multilingual bidirectional encoders that fuse text and raw image patches into a single Transformer encoder trained from scratch with a masked discrete‑diffusion objective. The model supports up to 16,384 tokens and can encode two standard 4K UHD images per input. Downstream retrieval on ViDoRe v3 shows NeoMME outperforms all smaller models while achieving higher nDCG@10 scores.

## Key Takeaways
- The encoder processes both multilingual text and image patches in one bidirectional Transformer, eliminating the need for separate vision‑language pipelines.
- Pre‑training from scratch with a masked diffusion objective yields strong representation alignment between modalities without relying on existing VLM checkpoints.
- Efficient compression techniques reduce late‑interaction embeddings by 255× while preserving over 95% of baseline nDCG@10, enabling high throughput on NVIDIA L40S hardware.

## Context
Current multimodal retrieval systems often rely on heavyweight vision encoders that are not optimized for multilingual text or fine‑tuning efficiency. NeoMME addresses this gap by offering a compact, single‑encoder solution that can be trained and deployed across languages with minimal overhead.

## Implications
For industry practitioners, NeoMME provides a ready‑to‑use backbone that balances performance and resource usage, lowering costs for large‑scale document retrieval services. Its open release under Apache 2.0 encourages community adoption and further research into efficient multimodal foundation models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01657v1)
