---
title: Does Forgetting Transfer Across Modalities? A Real-World Benchmark for Cross-Modal Knowledge Unlearning Evaluation
url: http://arxiv.org/abs/2608.03791v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_15-07-07Z_DoesForgettingTransferAcrossModalities_AReal_World.md
generated_at: 2026-08-05 01:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces UNLINK-VL, a benchmark for cross-modal knowledge unlearning in vision-language models, testing how forgetting of real-world entities propagates across modalities. Experiments show that multimodal unlearning retains effectiveness in textual evaluation but fails to transfer well to visual and cross‑modal tasks, revealing an asymmetry not captured by intra‑modal assessments.

## Key Takeaways
- The benchmark demonstrates a pronounced asymmetry where text‑only evaluations overestimate the success of knowledge unlearning compared with visual or cross‑modal tests.  
- Multimodal unlearning remains effective when evaluated only on textual queries but does not generalize to visual representations, indicating limited cross‑modal transfer.  
- General capabilities are largely preserved despite targeted forgetting, suggesting that unlearning can be selective without harming overall performance.

## Context
Vision-language models increasingly rely on large pretraining corpora that may embed sensitive or copyrighted information, making knowledge unlearning a critical research area for trustworthy AI. Existing benchmarks and studies have focused on intra‑modal forgetting, leaving the transfer of unlearned knowledge across modalities largely unexplored.

## Implications
Practitioners must adopt cross‑modal evaluation to avoid overstating unlearning effectiveness in text‑only settings. The findings highlight a need for unified metrics that assess knowledge removal across visual and textual representations to ensure reliable deployment of trustworthy AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03791v1)
