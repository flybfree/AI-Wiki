---
title: Using LMs to Model the Effects of Context and Coreference during Sentence Comprehension
published: 2026-09-26T00:43:56Z
authors: Kohei Kajikawa, Lin Ai, Tatsuki Kuribayashi, Ethan Gotlieb Wilcox
url: http://arxiv.org/abs/2609.32119v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Using LMs to Model the Effects of Context and Coreference during Sentence Comprehension

## Abstract
Language models (LMs) are often used as a tool to model human language processing. Recent studies suggest that severely restricting LMs' context window improves their fit to human psycholinguistic data by simulating human working memory constraints. However, it is possible that this strict memory-decay approach overlooks humans' reliance on long-range structural representations, such as discourse structre. In this work, we systematically vary the context window size of GPT-2 across four large-scale naturalistic English reading-time datasets and observe a U-shaped relationship: Although restricted contexts (< 20 tokens) successfully capture local memory limitations, expanded contexts (500--1,000 tokens) ultimately yield the highest overall psycholinguistic fit. To investigate the mechanism driving this benefit, we conduct a counterfactual inference-time experiment that disrupts cross-sentential entity chains by pronominalizing repeated discourse entities. Obscuring these structural linkages significantly degrades the predictive power of larger context windows by 20% to 40%. Our experiments demonstrate that tracking long-range coreference relations is one important factor for the alignment between LM surprisal and human reading behavior, and approximate the extent to which human comprehenders use global discourse relations during language processing.

## Metadata
- **Published**: 2026-09-26T00:43:56Z
- **Authors**: Kohei Kajikawa, Lin Ai, Tatsuki Kuribayashi, Ethan Gotlieb Wilcox
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32119v1)