---
title: BaseRSI: Recursive Self-Improvement of a Base Vision-Language Model via Training-Free Harness Internalization
published: 2026-11-18T15:10:11Z
authors: Mingda Zhang, Yuanhao Dong, Qiang Huang, Rui Qian, Yanjin Li, Zhenyu Liu, Xiao Huang, Zihao Yang, Jian Wang, Pinjia He, Xiaoying Tang
url: http://arxiv.org/abs/2611.24578v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BaseRSI: Recursive Self-Improvement of a Base Vision-Language Model via Training-Free Harness Internalization

## Abstract
Recursive self-improvement (RSI) is moving from the harness of prompts and tools around a base model toward the model itself. However, existing RSI still faces key challenges, including harness-bound gains that stay outside the base model, black-box supervision that reads only the model's outputs, and imprecise edits whose site and strength are fixed in advance. To address these challenges, we propose BaseRSI, a new paradigm of Recursive Harness Internalization: the base model improves its harness, then writes what the harness adds into its own weights through training-free edits, round after round on its own responses. To support this paradigm, we introduce ReGap, a mechanism that supervises every transformer block with the high-dimensional activation difference that the harness makes at that block alone, and updates the block's weights along this signal in a low-dimensional subspace. Building on this mechanism, we further propose ReKey, an algorithm that writes this signal by regression into a few key-value neurons of every block, and measures the site and strength of each edit on the model's own responses. Moreover, the base model fills every role of this recursion with forward passes alone, and its edits, written at different sites, compose in one checkpoint without refitting. Experimental results on ten visual reasoning benchmarks show that BaseRSI consistently improves a base vision-language model both in distribution and on held-out benchmarks. Our code is available at https://github.com/beita6969/BaseRSI.

## Metadata
- **Published**: 2026-11-18T15:10:11Z
- **Authors**: Mingda Zhang, Yuanhao Dong, Qiang Huang, Rui Qian, Yanjin Li, Zhenyu Liu, Xiao Huang, Zihao Yang, Jian Wang, Pinjia He, Xiaoying Tang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.24578v1)