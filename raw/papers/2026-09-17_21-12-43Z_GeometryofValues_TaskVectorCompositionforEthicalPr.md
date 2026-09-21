---
title: Geometry of Values: Task Vector Composition for Ethical Preference Alignment in Language Models
published: 2026-09-17T21:12:43Z
authors: Utkarsh Agarwal, Monojit Choudhury
url: http://arxiv.org/abs/2609.21094v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Geometry of Values: Task Vector Composition for Ethical Preference Alignment in Language Models

## Abstract
Large Language Models (LLMs) are increasingly deployed in applications that must weigh clashing moral values, yet even strong models exhibit hidden biases and brittle instruction-following across languages. We introduce a 12,000-instance dataset of two-option dilemmas covering pairwise three value conflicts: Honesty vs. Justice, Justice vs. Autonomy, and Autonomy vs. Honesty, along with their translations into Hindi, Arabic, Spanish, and Chinese, to probe cross-lingual behavior. Benchmarking on GPT-5-mini reveals that it consistently favors Honesty over Autonomy across all five languages when no policy is given. The Llama-3.2-1/3B models exhibit strong first-option bias; however, both plain fine-tuning and Direct Preference Optimization fine-tuning effectively remove this bias, increasing accuracy to greater than 98%. In order to decouple the effect of learning correlations in the dataset from abstract values, we propose a task vector transfer based experiment where after computing the task vectors for a direction of value preference we orthogonalize it with respect to the general instruction following vector. Our experiment shows that this method is effective in isolating the direction of the specific value preference that can successfully be used to conduct task arithmetic to obtain a model with the opposite stance.

## Metadata
- **Published**: 2026-09-17T21:12:43Z
- **Authors**: Utkarsh Agarwal, Monojit Choudhury
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.21094v1)