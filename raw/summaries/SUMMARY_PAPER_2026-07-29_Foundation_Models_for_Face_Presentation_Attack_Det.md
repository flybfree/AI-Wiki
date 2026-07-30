---
title: Foundation Models for Face Presentation Attack Detection: A Unified Linear-Probing Benchmark
url: http://arxiv.org/abs/2607.26993v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-29_14-52-25Z_FoundationModelsforFacePresentationAttackDetection.md
generated_at: 2026-07-29 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes a unified linear‑probing benchmark to evaluate how frozen foundation models encode face presentation attack detection information across multiple datasets. The study finds that while pretrained representations support strong intra‑dataset performance with minimal training, cross‑dataset transfer is limited and varies by model scale and architecture.

## Key Takeaways
- Frozen vision transformers such as InternViT‑6B achieve the lowest mean intra‑dataset error, indicating they capture PAD cues effectively within a single domain.  
- Cross‑dataset performance suffers from significant drops, showing that representation alone is insufficient to handle domain shift between MSU‑MFSD, CASIA‑FASD, Replay‑Attack and OULU‑NPU.  
- The trade‑off between accuracy and compute favors models like CLIP ViT‑B/32 for cross‑dataset evaluation, suggesting that model size is beneficial but not uniformly advantageous.

## Context
Foundation models have become the backbone of many vision tasks, yet their utility in security applications often depends on how well they generalize across datasets. This work highlights a gap: although large pre‑trained encoders can be adapted quickly with linear probes, their cross‑dataset robustness remains fragile, prompting ongoing research into domain‑aware adaptation strategies.

## Implications
For practitioners, the results underscore that simply freezing a foundation model is not enough; targeted fine‑tuning or additional data are needed to mitigate dataset drift. Industry adoption of PAD systems must therefore balance model efficiency with adaptability, potentially integrating lightweight adapters rather than relying solely on raw embeddings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26993v1)
