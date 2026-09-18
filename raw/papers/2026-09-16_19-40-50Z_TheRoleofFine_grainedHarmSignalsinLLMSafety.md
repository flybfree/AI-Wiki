---
title: The Role of Fine-grained Harm Signals in LLM Safety
published: 2026-09-16T19:40:50Z
authors: Soyeon Park, Seogyeong Jeong, Sunwoo Kim, Alice Oh
url: http://arxiv.org/abs/2609.19366v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Role of Fine-grained Harm Signals in LLM Safety

## Abstract
Prior work has shown that internal harmfulness representations in large language models vary across risk categories, while sharing a common general harm representation component. This raises a question about the role of the category-specific component beyond general harm representation in LLM safety. To answer this question, we isolate the category-specific component by removing shared general harmfulness representation from each categorical harmfulness representation, yielding a category residual that is orthogonal to general harmfulness at every layer. Using activation steering with category residuals across 11 risk categories in 3 instruction-tuned LLMs, we find that whether category residuals encode harmfulness varies across categories, and that this category-wise pattern is similar across models. Whether category residuals induce refusal also varies across categories, but this category-wise pattern is more model-dependent. We also find that category residuals increase LLMs' downstream internal alignment with shared general harmfulness representation. Together, these findings demonstrate that more fine-grained category residuals should also be considered beyond shared general harmfulness representation to fully understand LLM safety. More broadly, our findings show that even a direction orthogonal to a concept at one layer can contribute to the concept's downstream amplification.

## Metadata
- **Published**: 2026-09-16T19:40:50Z
- **Authors**: Soyeon Park, Seogyeong Jeong, Sunwoo Kim, Alice Oh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.19366v1)