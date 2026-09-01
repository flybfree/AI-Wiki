---
title: Reading the News: Adapting Large Language Models to Swedish Journalism Through Continued Pre-Training
published: 2026-08-31T11:20:55Z
authors: Lukas Borggren, Jenny Kunz, Marco Kuhlmann
url: http://arxiv.org/abs/2608.30609v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reading the News: Adapting Large Language Models to Swedish Journalism Through Continued Pre-Training

## Abstract
Large language models are increasingly capable in general, but their utility can remain modest in niche or understudied areas. One approach to address this limitation is to specialise existing models through additional training on target-domain corpora. In this work, we investigate such continued pre-training for adapting large language models to Swedish journalism, using a high-quality dataset that we curate from millions of news articles. To evaluate the adaptation efficacy, we also construct a novel domain-specific benchmark that covers six editorial tasks. Through full and parameter-efficient fine-tuning across two model sizes, we find that continued pre-training yields benefits in the target domain, but only when paired with experience replay to mitigate forgetting. We observe consistent enhancements in the models' generation quality and factual knowledge, but not their proficiency in discriminative tasks. Exploring a training-free method to facilitate instruction following, we see further improvements, but exclusively for models trained with low-rank adaptation. Crucially, we demonstrate the importance of targeted evaluation in the adaptation process, as an existing Swedish benchmark largely fails to capture the models' in-domain performance gains.

## Metadata
- **Published**: 2026-08-31T11:20:55Z
- **Authors**: Lukas Borggren, Jenny Kunz, Marco Kuhlmann
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30609v1)