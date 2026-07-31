---
title: OneShot: Index-in-Ranking with Neural Scoring for Large-Scale Retrieval
url: http://arxiv.org/abs/2607.27475v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-29_21-29-00Z_OneShot_Index_in_RankingwithNeuralScoringforLarge_.md
generated_at: 2026-07-30 23:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces OneShot, an end‑to‑end retrieval framework that aligns index learning with ranking objectives in a single model. By replacing the persistent dot‑product bottleneck with neural scoring, OneShot achieves higher recall and faster search at scale. In Instagram’s short‑video recommendation system, it delivers a 20 % recall gain and a tenfold efficiency improvement while maintaining operational performance.

## Key Takeaways
- The framework jointly optimizes index construction and ranking predictions to eliminate the structural misalignment between them.
- Neural scoring replaces dot‑product similarity, allowing richer interaction modeling beyond simple inner products.
- OneShot is deployed at production scale on Instagram, resulting in a 20 % recall increase and tenfold speedup for equivalent recall levels.

## Context
Modern recommendation systems face a trade‑off between high ranking accuracy and the ability to index billions of items quickly. Traditional approaches treat indexing and ranking as separate stages, limiting their scalability. This work demonstrates that integrating these tasks can overcome that limitation in large‑scale settings.

## Implications
The results suggest that holistic retrieval models are viable for real‑world recommendation engines, offering both performance gains and operational efficiency. Practitioners can adopt similar joint learning strategies to improve user engagement without sacrificing search speed.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27475v1)
