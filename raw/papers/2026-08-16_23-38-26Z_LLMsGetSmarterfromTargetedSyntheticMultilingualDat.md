---
title: LLMs Get Smarter from Targeted Synthetic Multilingual Data
published: 2026-08-16T23:38:26Z
authors: Ishika Agarwal, Arkajyoti Charaborty, Tanner Sorensen, Neha Gupta, Andreas Stolcke
url: http://arxiv.org/abs/2608.15964v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LLMs Get Smarter from Targeted Synthetic Multilingual Data

## Abstract
Language-specific competency (LSC) is the phenomenon of a language model performing better or worse depending on the language of the prompt. In other words, a language model outputs different (and potentially incorrect) responses to the same semantic query when prompted in different languages. Prior work attributes this to an internal misalignment of semantic representation across languages. Currently, there are two main approaches to address LSC in the literature: (1) routing all queries through English, improving performance, but limiting language expressivity to English; or (2) training on language-balanced data, equalizing model performance across languages, but reducing overall performance. In this work, we take a data centric perspective and introduce HOTFIXR: Hardness Optimized Training data For Improving X-Lingual Reasoning. It is a data generation framework that uses models to probe and learn a student model's multilingual weaknesses, and generates data to mitigate them. HOTFIXR can generate multilingual synthetic training data that can improve multilingual performance. We evaluate on three in-distribution tasks, three out-of-distribution tasks, and four out-of-distribution languages. On average, HOTFIXR (1) improves in-distribution performance by 6.2%, (2) reduces catastrophic forgetting (induced by fine-tuning) on OOD tasks by 3.7%, and (3) on OOD languages by 7.1%. Overall, as many real-world applications requires multilingual LLMs, our work contributes to the efforts of making LLMs multilingually proficient. We will release code upon acceptance.

## Metadata
- **Published**: 2026-08-16T23:38:26Z
- **Authors**: Ishika Agarwal, Arkajyoti Charaborty, Tanner Sorensen, Neha Gupta, Andreas Stolcke
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15964v1)