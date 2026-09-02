---
title: SinkPruner: Sink-Free Visual Token Pruning for Multimodal Large Language Models
url: http://arxiv.org/abs/2609.01004v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_09-52-10Z_SinkPruner_Sink_FreeVisualTokenPruningforMultimoda.md
generated_at: 2026-09-01 22:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
SinkPruner is a training‑free visual token pruning framework designed to reduce the computational load of multimodal large language models (MLLMs) without sacrificing performance. By removing high‑norm outlier tokens that are often mistakenly kept, SinkPruner achieves an 89 % reduction in visual tokens while preserving roughly 96.5 % of LLaVA‑1.5’s original quality.

## Key Takeaways
- High‑norm outlier tokens are highly redundant in both feature and spatial dimensions yet existing pruning methods frequently retain them as informative cues, leading to suboptimal decisions.  
- SinkPruner employs a coarse‑to‑fine design: a visual sanitizer filters these high‑norm redundancies to alleviate attention sink and dispersion, and a text‑guided pruner further retains tokens semantically aligned with the query.  
- Experiments on twelve image‑language and four video‑language benchmarks show that SinkPruner maintains 96.5 % (91.8 %) of LLaVA‑1.5’s performance under an 89 % token reduction.

## Context
Multimodal large language models excel at understanding visual information but become computationally expensive as they process long visual token sequences. Recent pruning approaches focus on vision‑centric or text‑guided strategies, yet many overlook high‑norm outlier tokens that are actually redundant, resulting in inefficient inference pipelines.

## Implications
This work demonstrates that efficient MLLM deployment is possible without sacrificing quality, offering a scalable solution for real‑world applications where bandwidth and latency are critical. Practitioners can adopt SinkPruner to lower inference costs across diverse multimodal benchmarks while preserving strong performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01004v1)
