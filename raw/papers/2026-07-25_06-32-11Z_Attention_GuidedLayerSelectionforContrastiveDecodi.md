---
title: Attention-Guided Layer Selection for Contrastive Decoding in Large Language Models
published: 2026-07-25T06:32:11Z
authors: Yusuke Sakai, Natthawut Kertkeidkachorn, Kiyoaki Shirai
url: http://arxiv.org/abs/2607.23067v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Attention-Guided Layer Selection for Contrastive Decoding in Large Language Models

## Abstract
Contrastive decoding methods such as DoLa improve the factuality of Large Language Models (LLMs) by contrasting the output distributions of mature and premature layers. However, DoLa's dynamic layer selection relies solely on divergences in output vocabulary distributions. In this work, we propose three attention-guided strategies: Attention-JSD, Attention-Entropy-Max, and Attention-Entropy-Min, which leverage structural information carried by internal self-attention mechanisms as a signal for layer selection. Experimental results on TruthfulQA demonstrate that our strategies, particularly Attention-JSD and Attention-Entropy-Min, consistently outperform the original DoLa. We observe significant gains on multi-answer metrics (MC2 and MC3), suggesting that attention distributions can provide a more sensitive signal for resolving factual knowledge than output vocabulary distributions.

## Metadata
- **Published**: 2026-07-25T06:32:11Z
- **Authors**: Yusuke Sakai, Natthawut Kertkeidkachorn, Kiyoaki Shirai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23067v1)