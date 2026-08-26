---
title: Does Episodic Memory Help Close the Lexical Frequency Gap in Sensitivity to Syntactic Contrasts? A Test Using Retrieval-Augmented Language Models
published: 2026-08-24T21:45:12Z
authors: Jing Liu, Najoung Kim
url: http://arxiv.org/abs/2608.23851v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Does Episodic Memory Help Close the Lexical Frequency Gap in Sensitivity to Syntactic Contrasts? A Test Using Retrieval-Augmented Language Models

## Abstract
Grammatical knowledge and how it is empirically tested are typically considered robust to the frequency of the lexical items in the expressions. However, neural network-based models of grammaticality exhibit high sensitivity to lexical frequency. We draw upon Complementary Learning Systems theory to test the hypothesis that robustness to lexical frequency can arise via a hippocampal episodic memory mechanism, which enables rapid encoding and retrieval of specific experiences and allows learners to leverage them when processing rare patterns. We use retrieval-augmented language models as an instantiation of such an episodic memory mechanism (specifically, $k$-nearest-neighbor language models that augment parametric models with explicit instance storage), and test whether this augmentation helps close the lexical frequency gap that vanilla language models exhibit in syntactic contrast tests. Using syntactic contrasts with frequency-stratified test items, we find that retrieval augmentation narrows the performance gap between high- and low-frequency items, consistent with episodic memory compensating for weak parametric representations. This benefit is consistent across different syntactic phenomena and across models pretrained on child-realistic and large-scale data. Additionally, we show that structural information is critical for effective retrieval, whereas semantic similarity alone provides little benefit. While these are promising proof-of-concept results supporting our hypothesis, the frequency gap is narrowed rather than fully closed. Based on our analyses, we propose preferential reweighting of retrieved instances, better representations and retrieval strategies for structural information, and flexible configurations of storage and retrieval as promising future directions for improving the implementation of episodic memory in language models.

## Metadata
- **Published**: 2026-08-24T21:45:12Z
- **Authors**: Jing Liu, Najoung Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23851v1)