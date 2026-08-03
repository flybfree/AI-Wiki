---
title: ViSAGE: Constructing Self-Correcting Memories for Long-Form Video Understanding
published: 2026-07-29T10:25:23Z
authors: Xinkui Zhao, Enbo Chen, Yifan Zhang, Chang Liu, Guanjie Cheng, Naibo Wang, Yueshen Xu
url: http://arxiv.org/abs/2607.28678v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ViSAGE: Constructing Self-Correcting Memories for Long-Form Video Understanding

## Abstract
Multimodal agents operating in long-horizon environments must build and continually update multimedia memories to support entity-consistent, temporally grounded reasoning. However, existing agentic memory approaches often discard fine-grained dentity cues under aggressive compression and segment-wise processing. They also rely heavily on vector similarity retrieval, which can surface semantically related yet identity-mismatched evidence, leading to entity confusion, error propagation, and hallucinated answers.   We propose ViSAGE, a multimodal agentic memory framework that constructs self-correcting, entity-centric memories. Specifically, ViSAGE anchors entity identity via cross-modal binding over long temporal ranges. It then applies bidirectional memory refinement to propagate delayed identity evidence, retroactively unifying historical records and improving future reasoning. We also introduce multi-agent cross-verification to assess retrieved evidence under an identity-evidence alignment onstraint, enabling abstention instead of unsupported answers when evidence is missing. Extensive results demonstrate that ViSAGE consistently outperforms the strongest baseline, achieving 5.9% higher accuracy.

## Metadata
- **Published**: 2026-07-29T10:25:23Z
- **Authors**: Xinkui Zhao, Enbo Chen, Yifan Zhang, Chang Liu, Guanjie Cheng, Naibo Wang, Yueshen Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28678v1)