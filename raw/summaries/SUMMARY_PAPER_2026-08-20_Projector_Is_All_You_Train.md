---
title: Projector Is All You Train
url: http://arxiv.org/abs/2608.19726v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-20_07-23-35Z_ProjectorIsAllYouTrain.md
generated_at: 2026-08-20 21:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether fine‑tuning the language model backbone is required when adapting a multimodal large language model to a new 3D modality. Experiments show that training only the projector suffices for strong performance, avoids degradation of existing capabilities, and doubles sample throughput compared with joint training.

## Key Takeaways
- Training solely the projector yields multimodal performance comparable to jointly trained models while preserving the original language model’s abilities.
- Joint training introduces drift in pre‑existing language tasks, which is avoided by definition when only the projector is updated.
- Projector‑only training provides roughly twice the effective training sample rate, improving efficiency.

## Context
The study addresses a key challenge in multimodal AI: balancing adaptation to new data with maintaining performance on existing modalities. As models grow larger, efficient fine‑tuning strategies are crucial for scalable deployment and continual learning.

## Implications
For practitioners, this finding suggests that lightweight projector updates can replace costly full‑model retraining, reducing computational cost and enabling rapid integration of new sensors or modalities. It also highlights the importance of preserving prior knowledge during model adaptation in large multimodal systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.19726v1)
