---
title: DIVE: Dynamic Iterative Visual Evidence Construction for Efficient Vision-Language Models
published: 2026-08-05T06:32:25Z
authors: Chen Zhong, Xiao An, Zijie Wang, Jiepan Li, Guangyi Yang, Wei He
url: http://arxiv.org/abs/2608.04496v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DIVE: Dynamic Iterative Visual Evidence Construction for Efficient Vision-Language Models

## Abstract
Visual inputs in vision-language models (VLMs) are often encoded into substantially longer token sequences than text, making visual tokens a major bottleneck for efficient inference. Abundant recent methods address this bottleneck by scoring token importance and pruning low-scoring tokens in a single pass. However, one-shot scoring is insufficient because a token's prompt-relevant usefulness depends on the evidence already retained. Motivated by this insight, we introduce DIVE (Dynamic Iterative Visual Evidence Construction), a training-free framework that recasts visual-token pruning as dynamic evidence construction. DIVE repeatedly selects the remaining token with the highest residual-conditioned score, updates the visual and prompt residuals to discount the evidence already explained, and re-evaluates the remaining tokens. This select-update-re-evaluate process builds a retained set of complementary, prompt-relevant evidence. Experiments across eight image-understanding benchmarks show that DIVE consistently preserves performance across token budgets. With an 88.9% reduction in visual tokens, DIVE retains 98.2% of the uncompressed model's average performance. Code is available at https://github.com/Zhong-Chenchen/DIVE.git.

## Metadata
- **Published**: 2026-08-05T06:32:25Z
- **Authors**: Chen Zhong, Xiao An, Zijie Wang, Jiepan Li, Guangyi Yang, Wei He
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04496v1)