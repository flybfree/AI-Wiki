---
title: On the Recall Scaling Laws in Mamba: A Theoretical and Mechanistic Study via Hashing
published: 2026-09-07T16:05:24Z
authors: Yuval Koren, Assaf Ben-Kish, Raja Giryes, Lior Wolf, Itamar Zimerman
url: http://arxiv.org/abs/2609.07681v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# On the Recall Scaling Laws in Mamba: A Theoretical and Mechanistic Study via Hashing

## Abstract
Associative Recall (AR) is the cognitive ability to learn and retrieve links between items in memory. In NLP, AR is used as a benchmark for evaluating the in-context memory capacity of architectures such as Mamba, and has been found to strongly correlate with language modeling performance. This paper explores AR from the perspective of mechanistic interpretability, aiming to reverse-engineer the exact internal algorithm used by Mamba to perform recall. Our key insight is that Mamba performs recall by implicitly learning linear hash functions, and we identify the low-level circuit that enables this behavior. Building on these findings and inspired by theoretical tools in similarity-preserving hashing, such as the Johnson-Lindenstrauss lemma, we develop a theoretical framework for analyzing AR, which we term Recall Scaling Laws. Given the vocabulary size and the number of facts in context, this framework allows us to (1) predict the embedding and state dimensions required for Mamba to achieve perfect recall, (2) predict recall success probability given the model dimensions, and (3) analyze multi-layer models and multi-head SSM patterns. Empirical results show that our theoretical findings are accurate and predictive, offering insights into how AR capacity scales with vocabulary, state, embedding size, and architecture.

## Metadata
- **Published**: 2026-09-07T16:05:24Z
- **Authors**: Yuval Koren, Assaf Ben-Kish, Raja Giryes, Lior Wolf, Itamar Zimerman
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.07681v1)