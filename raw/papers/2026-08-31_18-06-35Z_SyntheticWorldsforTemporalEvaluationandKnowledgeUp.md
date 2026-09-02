---
title: Synthetic Worlds for Temporal Evaluation and Knowledge Updating in LLMs
published: 2026-08-31T18:06:35Z
authors: Jonathan Zheng, Zirui Shao, Alan Ritter, Wei Xu
url: http://arxiv.org/abs/2609.00184v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Synthetic Worlds for Temporal Evaluation and Knowledge Updating in LLMs

## Abstract
Large language models (LLMs) rely on static pretraining corpora, causing their knowledge to become outdated over time. Existing approaches for evaluating knowledge edits either suffer from rapid contamination or rely on counterfactual edits that conflict with rigid existing knowledge. In this work, we propose a synthetic, simulation-driven framework for studying knowledge insertion in LLMs. We introduce {\sc ParallelEvents}, a benchmark of fictional yet realistic future worlds that generates coherent event trajectories for controlled evaluation, avoiding contamination while preserving consistency. Building on this dataset, we develop {\sc Synapse}, a training framework that uses model-generated data to update model parameters via mid-training and instruction tuning. This synthetic pipeline enables scalable knowledge integration without costly human-curated data. Empirically, {\sc Synapse} outperforms existing methods by 14.23\%, demonstrating that simulation-based synthetic training leads to robust and coherent knowledge insertions.

## Metadata
- **Published**: 2026-08-31T18:06:35Z
- **Authors**: Jonathan Zheng, Zirui Shao, Alan Ritter, Wei Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00184v1)