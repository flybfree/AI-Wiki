---
title: Augmenting Molecular Language Models with Local $n$-gram Memory
published: 2026-06-10T14:07:18Z
authors: Xinni Zhang, Zijing Liu, He Cao, Yu Li, Irwin King
url: http://arxiv.org/abs/2606.12113v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Augmenting Molecular Language Models with Local $n$-gram Memory

## Abstract
Transformer-based language models for SMILES strings suffer from a locality gap: standard character-level tokenization fragments chemically meaningful motifs, forcing models to repeatedly learn local syntax at the expense of long-range dependencies. To address this without disrupting standard tokenizers, we propose MolGram, which integrates a conditional $n$-gram memory module into molecular language models. MolGram maps local string patterns to learned embeddings via scalable hash lookups and dynamically injects this regional context into hidden states. Evaluations across three tasks, including unconditional molecule generation, forward reaction prediction, and single-step retrosynthesis, show that MolGram consistently improves performance. Crucially, our analyses demonstrate that MolGram outperforms baselines with 3$\times$ more parameters, establishing explicit local pattern memory as a highly efficient inductive bias.

## Metadata
- **Published**: 2026-06-10T14:07:18Z
- **Authors**: Xinni Zhang, Zijing Liu, He Cao, Yu Li, Irwin King
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.12113v1)