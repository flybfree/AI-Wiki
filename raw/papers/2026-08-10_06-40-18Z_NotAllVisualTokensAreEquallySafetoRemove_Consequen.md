---
title: Not All Visual Tokens Are Equally Safe to Remove:Consequence-Sensitive Visual Token Compression
published: 2026-08-10T06:40:18Z
authors: Jingbo Wen, Liang He, Mingyu Cao, Haoyu Wang, Minxuan Hu, Kangning Cui, Xilu Wang
url: http://arxiv.org/abs/2608.09176v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Not All Visual Tokens Are Equally Safe to Remove:Consequence-Sensitive Visual Token Compression

## Abstract
Visual token compression for vision--language models (VLMs) has largely relied on criteria such as attention, redundancy, and uncertainty to maximize average accuracy under a fixed compute budget, implicitly assuming that all errors carry equal cost. However, the consequence of an incorrect prediction on downstream tasks is rarely symmetric: misreading an invoice amount can be far more costly than misclassifying a background color. Motivated by this, we introduce consequence-sensitive visual token compression, which allocates visual computation across requests according to their potential error costs. Our method follows a calibrate-then-allocate procedure, estimating consequence-specific error-budget curves offline and applying the calibrated token budgets online using consequence signals available from question or task information. On a controlled within-task benchmark, high- and low-consequence questions are drawn from the same document images, so content alone cannot reveal which questions are costly to get wrong. In this setting, our method reduces high-stakes errors from 0.300 to 0.133 under the same total token budget, whereas a content-driven allocator performs no better than uniform allocation. Measuring how error rates change with token budget across different cost ratios, we derive an allocation frontier: uniform allocation is optimal when errors are equally costly, and token transfer toward high-consequence questions becomes increasingly beneficial as the cost gap grows. This allocation principle generalizes well across three dense vision-language benchmarks, two budget realization mechanisms (token deletion and resolution reallocation), two VLM architectures, and multiple token selection strategies. On a realistic mixed workload, consequence-sensitive allocation reduces cost-weighted error by 38% while achieving approximately 21% lower latency than full-resolution inference.

## Metadata
- **Published**: 2026-08-10T06:40:18Z
- **Authors**: Jingbo Wen, Liang He, Mingyu Cao, Haoyu Wang, Minxuan Hu, Kangning Cui, Xilu Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09176v1)