---
title: KV-Rescue: Recovering Reasoning Language Model KV Eviction Loss via Stepwise Interleaving
published: 2026-08-16T15:23:25Z
authors: Minsoo Cheong, Woosang Lim, Vincent-Daniel Yun, Sungjoo Yoo
url: http://arxiv.org/abs/2608.15797v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# KV-Rescue: Recovering Reasoning Language Model KV Eviction Loss via Stepwise Interleaving

## Abstract
KV-cache eviction caps the memory cost of long reasoning traces but is inherently lossy because the model decodes from a partial view of its history. Under aggressive budgets, this not only lowers accuracy but can also cause runaway degeneration, where the model produces incoherent or repetitive tokens until reaching the length limit. We characterize much of this loss as an information gapf caused by missing context, rather than a capability gap caused by limited model capacity. An evicted 7B model and a full-context 1.5B model make complementary errors, and an oracle choice between their answers recovers 79% of the accuracy gap to the full-KV 7B model. Based on this observation, we propose KV-Rescue, a training-free inference framework that bridges the information gap introduced by KV eviction using a lightweight full-context helper. KV-Rescue interleaves reasoning steps from the two models into a shared trajectory. An online detector uses entropy and compressibility to terminate the generation of incoherent or repetitive base-model candidates early. Across five math benchmarks with Qwen2.5-Math 7B and 72B, KV-Rescue recovers an average of 87% of the accuracy lost to eviction at eviction budget B=64. A decode-cost analysis further shows that preventing runaway degeneration cuts base-model token generation by 43% on average.

## Metadata
- **Published**: 2026-08-16T15:23:25Z
- **Authors**: Minsoo Cheong, Woosang Lim, Vincent-Daniel Yun, Sungjoo Yoo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15797v1)