---
title: Closing the Loop: Practical Training Recipes for Looped Language Models
published: 2026-09-30T20:09:58Z
authors: Andrei Marchenko, Viacheslav Bezrukov, Oleg Kashurin, Inessa Fedorova, Dmitry Bocharov, Yuliana Shakhvalieva, Maria Tikhonova, Valerii Ternovskii
url: http://arxiv.org/abs/2610.00673v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Closing the Loop: Practical Training Recipes for Looped Language Models

## Abstract
Looped language models increase effective depth by repeatedly applying a shared block of layers, but existing large-scale recipes require multi-stage training over trillions of tokens, while the benefits of recurrence remain difficult to separate from differences in data and training. In this work, we establish practical training recipes for looped language models, with three main results. (1) We develop a compute-efficient from-scratch pipeline that reduces the training budget from 7.7T tokens in Ouro to 310B tokens while retaining strong reasoning performance. Pretraining followed by high-quality mid-training, together with learning-rate warmup and stronger exit-gate regularization, enables stable recurrent training without prior multi-stage schedules. (2) Under controlled comparisons, our 1.4B LoopLM outperforms a parameter-matched dense model trained on the same data and token budget on all 12 evaluated benchmarks, including +14 points on GSM8K, +10 on MATH, and +22 on DROP. At matched inference compute, it approaches a 3.9B dense model on mathematical reasoning and reading comprehension while using only 36\% as many parameters. (3) We introduce a minimal recipe for converting pretrained dense models into looped ones: a single learned input-mixing scalar and a smoothed exit loss, with no step-specific parameters. Applied to Qwen3-1.7B-Base, Looped Qwen improves over an identically continued dense baseline on every evaluated benchmark across two data regimes, with statistically clear gains on GSM8K, MATH, and MMLU-Pro on the curated mixture. Together, these results make looped language models substantially cheaper to train from scratch and practical to introduce into existing pretrained checkpoints, while isolating the gains due to recurrence itself.

## Metadata
- **Published**: 2026-09-30T20:09:58Z
- **Authors**: Andrei Marchenko, Viacheslav Bezrukov, Oleg Kashurin, Inessa Fedorova, Dmitry Bocharov, Yuliana Shakhvalieva, Maria Tikhonova, Valerii Ternovskii
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.00673v1)