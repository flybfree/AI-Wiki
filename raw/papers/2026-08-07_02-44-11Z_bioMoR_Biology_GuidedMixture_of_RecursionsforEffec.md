---
title: bioMoR: Biology-Guided Mixture-of-Recursions for Effective Genomic Learning
published: 2026-08-07T02:44:11Z
authors: Koushik Howlader, Tirtho Roy, Md Tauhidul Islam, Wei Le
url: http://arxiv.org/abs/2608.06727v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# bioMoR: Biology-Guided Mixture-of-Recursions for Effective Genomic Learning

## Abstract
Transformer models for high-dimensional omics analysis process thousands of genes or pathways, although only a subset requires deep computation. Mixture-of-Recursions (MoR) improves efficiency through adaptive token-choice or expert-choice routing. We propose bioMoR, which, to the best of our knowledge, is the first framework to apply MoR to gene-level and pathway-level learning. Our contributions include identifying three locations for integrating structured biological knowledge within an MoR backbone: graph-based information sharing refines token embeddings, a structural bias guides self-attention toward biologically related tokens, and a graph-aware router uses neighborhood information to determine each token's recursion depth. These techniques are centered on our insight that additional knowledge of token interaction can effectively help models construct embeddings and select which tokens should be learned more deeply. Across eight benchmarks spanning diverse omics data types and evaluated under a unified five-fold cross-validation protocol, bioMoR improves average macro-F1 by 8.2 percentage points and balanced accuracy by 7.1 percentage points over the strongest biology-agnostic MoR baseline while using 75 percent fewer parameters and up to 58 percent fewer FLOPs than a non-recursive Transformer. The selected marker genes or pathways provide biological interpretability, while their token-specific recursion depths reveal how computation is allocated.

## Metadata
- **Published**: 2026-08-07T02:44:11Z
- **Authors**: Koushik Howlader, Tirtho Roy, Md Tauhidul Islam, Wei Le
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06727v1)