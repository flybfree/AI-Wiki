---
title: Evaluating Compressed Memory: Dependence, Utility, and Content Benefit
published: 2026-10-14T01:17:03Z
authors: Minsu Oh, Seunghui Jwa, Chanjun Park, Yeo-Chan Yoon
url: http://arxiv.org/abs/2610.19373v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evaluating Compressed Memory: Dependence, Utility, and Content Benefit

## Abstract
Does a language model answer better because its compressed memory contains useful document information? Replacing memory vectors with zeros can lower a trained model's score without showing that it outperforms a model trained without memory. We combine zeroing with separately trained models that cannot access stored text or receive the same constant input for every document. Across nine systems, some models rely on memory yet perform worse than the trained alternative. For example, in experiments that predict states in generated stories, zeroing memory worsens a model's prediction loss, yet a model trained without memory achieves lower loss than the original model with intact memory. On TriviaQA, giving xRAG memory from another question's passage raises F1, which measures word overlap with accepted answers, from 19.38 without a document to 24.78. Its effect on how often outputs contain an accepted answer is statistically uncertain. The question's retrieved passage scores higher still (29.88 F1). Thus a gain over no document alone does not establish that the gain requires the question's passage. Evaluations must therefore specify the comparison model, absolute performance, and generation and scoring conditions.

## Metadata
- **Published**: 2026-10-14T01:17:03Z
- **Authors**: Minsu Oh, Seunghui Jwa, Chanjun Park, Yeo-Chan Yoon
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.19373v1)