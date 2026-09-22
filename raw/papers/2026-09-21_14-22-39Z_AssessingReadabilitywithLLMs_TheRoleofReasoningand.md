---
title: Assessing Readability with LLMs: The Role of Reasoning and Few-Shot Prompting
published: 2026-09-21T14:22:39Z
authors: Raphaël Thieffry, Matej Martinc
url: http://arxiv.org/abs/2609.24650v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Assessing Readability with LLMs: The Role of Reasoning and Few-Shot Prompting

## Abstract
Readability assessment is essential for tailoring texts to intended audiences across educational, healthcare, and information retrieval domains. However, traditional readability formulas struggle to generalize across genres and languages, while supervised machine learning models rely on scarce, domain-specific annotated corpora, limiting their applicability--particularly for less-resourced languages. Large Language Models (LLMs) offer a highly scalable, multilingual alternative that requires no task-specific training, yet the impact of advanced prompting strategies on their performance remains underexplored. In this paper, we conduct a systematic benchmark of diverse open-source LLMs for multilingual readability assessment, focusing on the prediction of discrete readability levels required by educational frameworks. In addition to English, we evaluate our approach on a less-resourced language, Slovenian, to establish whether LLMs remain effective in low-resource settings. Specifically, we investigate the influence of explicit reasoning, demonstrating that Chain-of-Thought (CoT) prompting and reasoning-oriented models yield significant improvements over direct answering. Furthermore, our exploration of few-shot in-context learning reveals that providing just one labelled example per category (1-shot) substantially enhances prediction quality compared to zero-shot settings, with additional examples offering diminishing returns. By comprehensively comparing these approaches against traditional unsupervised metrics and state-of-the-art supervised baselines, we establish the viability of out-of-the-box LLMs as robust, cross-lingual readability assessors.

## Metadata
- **Published**: 2026-09-21T14:22:39Z
- **Authors**: Raphaël Thieffry, Matej Martinc
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.24650v1)