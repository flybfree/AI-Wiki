---
title: How code helps different tasks? A decompositional lens on LLM post-training
url: http://arxiv.org/abs/2609.33845v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-27_18-57-54Z_Howcodehelpsdifferenttasks_AdecompositionallensonL.md
generated_at: 2026-09-28 22:01
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces a decompositional lens to analyze how code data influences LLM post-training by breaking down execution-verified corpora into interpretable categories based on computational patterns. Through controlled experiments across question answering, mathematics, and code generation tasks, the authors demonstrate that the effectiveness of specific code categories varies significantly depending on the base model and target task, with some categories even causing degradation in certain contexts. Furthermore, the study reveals a "less is more" phenomenon where compact mixtures of beneficial code categories can outperform both individual categories and full-corpus training while utilizing only 10–15% of the data.

## Key Takeaways
- Decomposing code corpora into categories based on computational patterns exposes that data value is highly heterogeneous; a single category may enhance performance for one instruction-tuned model or downstream task while simultaneously degrading results for another, challenging the assumption of uniform benefit from code data and highlighting the need for granular analysis.
- The research identifies a "less is more" efficiency pattern where compact mixtures of carefully selected code categories, which individually improve target tasks, can outperform both their best individual constituent and training on the full corpus using merely 10–15% of the total data volume, proving that strategic composition yields superior results to brute-force inclusion.
- Response maps derived from controlled fine-tuning experiments highlight that optimal data selection is context-dependent, with recurring gains in average question-answering performance but highly variable outcomes for mathematics and code generation tasks that rely heavily on the specific starting model architecture and the desired output domain.

## Context
As large language models increasingly rely on post-training data to enhance capabilities, understanding the granular impact of different data modalities becomes critical for efficient model development. This work addresses a gap in current practices where code is often treated as a monolithic resource, providing a framework to dissect how specific computational structures within code influence learning dynamics across diverse tasks and model

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.33845v1)
