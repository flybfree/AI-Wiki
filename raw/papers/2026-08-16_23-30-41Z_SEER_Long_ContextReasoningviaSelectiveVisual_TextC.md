---
title: SEER: Long-Context Reasoning via Selective Visual-Text Compression
published: 2026-08-16T23:30:41Z
authors: Jiawei Xu, Zhilin Zhai, Jinrui Fang, Ruohan Xu, Mingfei Lu, Yi Zhang, Guanchu Wang, Tianlong Chen, Ying Ding
url: http://arxiv.org/abs/2608.15962v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SEER: Long-Context Reasoning via Selective Visual-Text Compression

## Abstract
Long-context reasoning remains computationally expensive for large language models due to the quadratic complexity of attention over text tokens. Visual-text compression offers a promising alternative by rendering text into images and processing them with vision-language models, often reducing token usage. However, existing approaches apply uniform compression regardless of query relevance, potentially sacrificing precision where detailed extraction is required. We present SEER, a framework that learns to select query-relevant images through visual scanning and retrieve textual content only where needed, combining the efficiency of visual compression with the precision of text-based reasoning. Through supervised fine-tuning on tool-interaction trajectories, SEER learns adaptive tool invocation for selection and retrieval. Experiments on long-context benchmarks show that SEER improves extraction precision through selective text retrieval while retaining average prompt-token savings relative to full-text baselines. On LongBench, SEER achieves 51.11% average accuracy, outperforming the visual-text baseline Glyph-9B by 2.33 points and Qwen3-8B by 3.49 points. Code can be accessed at https://github.com/jiaweixu98/SEER

## Metadata
- **Published**: 2026-08-16T23:30:41Z
- **Authors**: Jiawei Xu, Zhilin Zhai, Jinrui Fang, Ruohan Xu, Mingfei Lu, Yi Zhang, Guanchu Wang, Tianlong Chen, Ying Ding
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15962v1)