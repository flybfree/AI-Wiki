---
title: Sliding-window beats linear attention
published: 2026-08-28T15:31:34Z
authors: Alexia Jolicoeur-Martineau, Rhea Sanjay Sukthanker, Pashmina Cameron, Emy Gervais
url: http://arxiv.org/abs/2608.28444v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Sliding-window beats linear attention

## Abstract
Due to the nature of quadratic attention, Large Language Models (LLMs) consume a lot of memory and energy. Every new token costs more than the previous one. For each additional token, the keys and values must be stored in memory indefinitely, which is unsustainable.   Several alternatives have been proposed to fix the quadratic scaling problem, one of which is retrofitting LLMs to use Linear Attention. This idea has attracted a lot of attention, given its promise to solve the quadratic scaling problem with state-of-the-art performance at low cost. However, this line of research has not been properly compared to simpler baselines.   In this work, we show that Sliding Window Attention (SWA) with sinks performs as well or better than post-trained Linear Attention models. We observe this across multiple LLMs on various downstream tasks. For long-context reasoning tasks (Needle-in-a-Haystack and BABILong), SWA achieves massively higher performance (2 to 10 times higher than linear attention). SWA requires no post-training, is extremely fast, and requires low memory; therefore, making it an extremely cheap and reliable solution.   To reduce inference memory cost, we strongly recommend switching to SWA instead of post-training linear models. Linear attention models may have shown some promise, but they likely require to be trained from scratch or extensive post-training in order to even match SWA.

## Metadata
- **Published**: 2026-08-28T15:31:34Z
- **Authors**: Alexia Jolicoeur-Martineau, Rhea Sanjay Sukthanker, Pashmina Cameron, Emy Gervais
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28444v1)