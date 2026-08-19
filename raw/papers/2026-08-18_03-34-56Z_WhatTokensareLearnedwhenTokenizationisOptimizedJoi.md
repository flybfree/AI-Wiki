---
title: What Tokens are Learned when Tokenization is Optimized Jointly with Language Modeling?
published: 2026-08-18T03:34:56Z
authors: Saketh Reddy Vemula, Parameswari Krishnamurthy
url: http://arxiv.org/abs/2608.17325v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# What Tokens are Learned when Tokenization is Optimized Jointly with Language Modeling?

## Abstract
Tokenization is a fundamental component of language modeling pipelines. Despite its importance, it is often fixed, even though it significantly impacts model performance across languages. In this work, we analyze what tokens are learned when tokenization is jointly optimized with language modeling. We compare tokenizer-free approaches such as SSLMs and H-Nets with fixed tokenizers across 18 typologically and script-diverse languages. Our results show that joint optimization fundamentally alters token structure. SSLMs recover morphologically aligned and contextually efficient tokens, whereas H-Nets prioritize byte-level efficiency, producing longer tokens with very low overlap with standard subword vocabularies. We further show that tokenization behavior varies across language typologies. Agglutinative languages exhibit more dynamic segmentation patterns while learning. Through downstream evaluation, with pretrained-then-finetuned BERT models, we find that SSLM-based pretokenization consistently reduces language modeling perplexity and achieves competitive downstream performance despite distinct vocabularies. Overall, tokenizer-free approaches optimize for contextual and computational efficiency rather than strict morphological structure, resulting in fundamentally different yet effective vocabularies for downstream NLP.

## Metadata
- **Published**: 2026-08-18T03:34:56Z
- **Authors**: Saketh Reddy Vemula, Parameswari Krishnamurthy
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17325v1)