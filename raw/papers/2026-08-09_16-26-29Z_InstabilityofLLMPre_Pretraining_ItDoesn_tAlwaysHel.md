---
title: Instability of LLM Pre-Pretraining: It Doesn't Always Help. An Investigation on Multiple Languages
published: 2026-08-09T16:26:29Z
authors: Sofiia Riazhskykh, Nam Luu, Ondřej Bojar
url: http://arxiv.org/abs/2608.08800v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Instability of LLM Pre-Pretraining: It Doesn't Always Help. An Investigation on Multiple Languages

## Abstract
Pretraining LLMs on artificial languages ("pre-pretraining") is a technique that could reportedly increase token efficiency by 33%, i.e., save up to 33% of training tokens needed to reach a certain performance. We validate this prior result for English on a larger set of natural languages across four language families, using two different tokenizers and varying model sizes. We also relate the observed gains (or losses) in token efficiency to quantified linguistic properties of the languages, such as sentence length, morphological richness, and features of dependency syntactic trees (tree depth, number of children, number of crossing dependencies). Our empirical results indicate that the reported gains depend heavily on the experiment setup and the choice of random seed, although we can confirm the trend of stable gains with 128-Dyck pretraining of small models with the Llama tokenizer for most of the examined languages. On a general note, we argue that multiple training runs should be carried out at least for a subset of experiments to avoid the community adopting unstable approaches.

## Metadata
- **Published**: 2026-08-09T16:26:29Z
- **Authors**: Sofiia Riazhskykh, Nam Luu, Ondřej Bojar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08800v1)