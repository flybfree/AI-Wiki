---
title: Tokenizer-Agnostic Engram Module
published: 2026-07-31T06:32:15Z
authors: Jia Peng Lim, Hai Leong Chieu
url: http://arxiv.org/abs/2607.29065v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Tokenizer-Agnostic Engram Module

## Abstract
Deepseek's Engram, a conditional memory module, was introduced to trade-off storage versus reasoning in large language models. However, the module relies on token-level $N$-gram hashing for Engram embedding lookup, introducing a tight coupling to the tokenizer used: a model with a different tokenizer would have to train its own Engram embeddings from scratch. To improve the reusability of Engram embeddings, we propose a change to the hashing routine, enabling compatibility between Engram models using different tokenizers. Instead of modelling disjoint $N$-gram spaces, we treat $N$-gram as a method to sample potentially useful byte sequences, from all possible byte sequences across tokens. We replace the XOR-based hashing with the general polynomial hashing with a joint embedding space across $N$. This work investigates the possible trade-offs and shows that this simple substitution produces comparable performance and achieves tokenizer-agnosticism: hash equivalence for byte-equivalent token sequences.

## Metadata
- **Published**: 2026-07-31T06:32:15Z
- **Authors**: Jia Peng Lim, Hai Leong Chieu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29065v1)