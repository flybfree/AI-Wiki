---
title: FORGE: Frame Orthogonality in Relevance Geometry for Long-Form Video Understanding
url: http://arxiv.org/abs/2607.25266v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_04-09-49Z_FORGE_FrameOrthogonalityinRelevanceGeometryforLong.md
generated_at: 2026-07-28 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces FORGE, a model‑agnostic technique that selects video frames by maximizing relevance while preserving diversity in a query‑conditioned embedding space. Experiments on Video-MME and LongVideoBench show the method improves keyframe selection scores by 11–15 points over training‑free baselines and doubles recall at K=64. The gains also translate to question‑answering accuracy across eight MLLMs.

## Key Takeaways
- FORGE aligns embedding space geometry so that frames covering independent query‑relevant directions are far apart, enabling selection of diverse relevant content within a budget.
- The method boosts unified keyframe selection scores by 11.0–15.3 points over the strongest training‑free baseline across two benchmark datasets.
- Recall at K=64 is doubled (0.415 vs 0.204) and question‑answering accuracy improves up to 8.7 points over uniform sampling.

## Context
Long‑form video understanding faces a trade‑off between relevance and diversity when selecting frames, limiting the use of large language models that rely on dense embeddings. This work demonstrates that inference‑time geometry alignment can overcome this bottleneck without retraining.

## Implications
Practitioners can apply FORGE to compress long videos for downstream tasks while preserving essential information, reducing bandwidth and latency. The approach offers a scalable, model‑agnostic strategy that could be integrated into existing MLLM pipelines for efficient video processing.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25266v1)
