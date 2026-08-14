---
title: MARCH: Scaling Recurrent Memory with Content-Routed State Anchors
url: http://arxiv.org/abs/2608.12435v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-12_13-45-01Z_MARCH_ScalingRecurrentMemorywithContent_RoutedStat.md
generated_at: 2026-08-13 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MARCH, a recurrent memory architecture that scales long‑context models by periodically storing state checkpoints as content‑routed anchors. By caching cumulative states and using compact keys, MARCH maintains a growing memory bank while keeping computation linear in sequence length. Experiments show MARCH outperforms linear attention variants on commonsense reasoning, LongBench, and retrieval tasks.

## Key Takeaways
- MARCH caches recurrent state checkpoints as content‑routed anchors to enable a memory bank that grows with context length.
- The architecture uses an anchor query at each token to attend all causally available state anchors, aggregating outputs via attention style.
- This approach reduces quadratic cost while preserving long‑range recall compared to fixed‑size recurrent states.

## Context
Recurrent models struggle to retain early information because only the latest state is kept. Linear attention methods also face quadratic costs for long sequences. MARCH addresses both limits by decoupling memory growth from computational complexity, offering a scalable alternative in the era of very long prompts.

## Implications
For practitioners, MARCH enables efficient training and inference on datasets with thousands of tokens without sacrificing performance. The method could be integrated into large language models to support complex reasoning tasks where historical context matters, such as code generation or multi‑step instruction following.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12435v1)
