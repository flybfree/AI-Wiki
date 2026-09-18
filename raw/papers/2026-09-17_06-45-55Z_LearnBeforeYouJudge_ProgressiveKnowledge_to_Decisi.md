---
title: Learn Before You Judge: Progressive Knowledge-to-Decision Alignment for Explainable Hateful Meme Detection
published: 2026-09-17T06:45:55Z
authors: Bo Xu, Chenyuan Wang, Xinyu Chen, Quanhao Zhu, Rui Lin, Liang Zhao, Hongfei Lin, Feng Xia
url: http://arxiv.org/abs/2609.19778v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learn Before You Judge: Progressive Knowledge-to-Decision Alignment for Explainable Hateful Meme Detection

## Abstract
Hateful memes spread abusive content through implicit interactions between images and text, posing serious threats to the safety of online communities. In recent years, multimodal large language models have been widely used for hateful meme detection and are increasingly adopted to generate explainable detection results. However, we find that existing explain-then-detect methods often couple explanation generation and label prediction within the same training process. This coupling causes interference between task objectives, leading to limited detection performance and even worse results than simple SFT baselines. To address these challenges, we propose ProKDA, a progressive knowledge-to-decision alignment method for explainable hateful meme detection. Inspired by the human annotation training process, ProKDA first uses an agentic background knowledge construction pipeline to obtain external knowledge related to meme understanding. It then adopts a three-stage training strategy that sequentially performs background knowledge learning, hatefulness detection learning, and hatefulness boundary alignment. Unlike prior explain-then-detect methods that jointly optimize both tasks, ProKDA focuses on a single training objective at each stage. This design reduces interference between the two tasks and progressively transforms background knowledge into robust detection decisions. Experiments on three public hateful meme benchmarks show that ProKDA achieves state-of-the-art detection performance and provides accurate, explainable, and evidence-supported decisions for hateful meme moderation. Project page: https://meizhiyuan88666.github.io/prokda.

## Metadata
- **Published**: 2026-09-17T06:45:55Z
- **Authors**: Bo Xu, Chenyuan Wang, Xinyu Chen, Quanhao Zhu, Rui Lin, Liang Zhao, Hongfei Lin, Feng Xia
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.19778v1)