---
title: Evaluating Dedicated Monolingual and Joint Multilingual Causal Models for Dravidian Languages
published: 2026-08-07T19:33:11Z
authors: Venkata Naga Sai Vishnu Rohit Pulipaka
url: http://arxiv.org/abs/2608.07727v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evaluating Dedicated Monolingual and Joint Multilingual Causal Models for Dravidian Languages

## Abstract
Dravidian languages, mainly Tamil, Telugu, Kannada, and Malayalam make up only a small part of the data used to train multilingual language models, so it's not clear how much per-language ability these models actually keep. I have trained five GPT-2 architecture models from scratch to compare four monolingual models (one each for Tamil, Telugu, Kannada, and Malayalam, each with its own 32K-vocabulary subword tokenizer) against one multilingual model sharing a 64K-vocabulary subword tokenizer across all four languages. All the 5 models are trained on cleaned CC-100, Wikipedia, and Samanantar data. I have tested the models on perplexity, bits-per-byte, tokenizer efficiency, and fine-tuning results which are compared against mGPT. The monolingual models outperform mGPT on sentiment classification and named entity recognition, and their tokenizers proved more efficient than the shared multilingual model across all the languages tested.

## Metadata
- **Published**: 2026-08-07T19:33:11Z
- **Authors**: Venkata Naga Sai Vishnu Rohit Pulipaka
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07727v1)