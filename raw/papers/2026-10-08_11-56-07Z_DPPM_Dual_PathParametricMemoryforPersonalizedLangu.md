---
title: DPPM: Dual-Path Parametric Memory for Personalized Language Models
published: 2026-10-08T11:56:07Z
authors: Yuhao Chen, Shuochen Liu, Jiayao Shi, Jian Hong, Chen Cheng, Xinyun Ding, Tao Wang, Ya Li, Quan Liu, Tong Xu
url: http://arxiv.org/abs/2610.11776v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DPPM: Dual-Path Parametric Memory for Personalized Language Models

## Abstract
Long-term personalization requires language models to use interaction history to track users' preferences across sessions. Parametric memory encodes this interaction history into model parameters or adapters, reducing the need to include it in the inference context. However, independent context compilation leaves cross-session integration unspecified, while recurrent updates can attenuate earlier evidence. To address these challenges, we propose Dual-Path Parametric Memory (DPPM). Its Evidence path directly pools representations of the interaction history to preserve earlier evidence, while its Delta path sequentially updates an associative state to capture changes. Fusing both outputs produces history-conditioned LoRA adapters that combine evidence accumulation with ordered revision. Across multiple backbones, DPPM outperforms the evaluated baselines, achieving 54.22% on PersonaMem-v2 and 86.79% on PrefEval. These results suggest that DPPM provides a simple and effective design choice for cross-session personalized parametric memory.

## Metadata
- **Published**: 2026-10-08T11:56:07Z
- **Authors**: Yuhao Chen, Shuochen Liu, Jiayao Shi, Jian Hong, Chen Cheng, Xinyun Ding, Tao Wang, Ya Li, Quan Liu, Tong Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.11776v1)