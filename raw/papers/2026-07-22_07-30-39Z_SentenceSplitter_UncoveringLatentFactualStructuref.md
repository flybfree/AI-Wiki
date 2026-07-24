---
title: Sentence Splitter: Uncovering Latent Factual Structure for Self-Supervised Learning
published: 2026-07-22T07:30:39Z
authors: Ahmad Pouramini, Mahsa Afsharizadeh
url: http://arxiv.org/abs/2607.19845v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Sentence Splitter: Uncovering Latent Factual Structure for Self-Supervised Learning

## Abstract
This paper introduces Sentence Splitter, a self-supervised framework built upon a T5-based encoder--decoder architecture for uncovering the latent factual structure of natural language sentences. The proposed method identifies the semantic boundary between a descriptive prefix (head) and its factual completion (tail) by formulating sentence splitting as a discrete segmentation problem, where a sentence of length $N$ admits $N$ possible split points but only one recovers the intended head--tail structure. Rather than explicitly searching over all candidate boundaries, the model learns to recover the factual completion through probabilistic sequence generation. To eliminate the need for manual annotation, symbolic head--tail pairs are first verbalized into natural-language templates that provide supervision for training the Sentence Splitter. The trained splitter is then applied to raw text to extract aligned prefix--tail pairs, which are subsequently used to train a generative model that proposes additional plausible completions through a lightweight bootstrapping process. This unified pipeline provides a scalable and structure-aware approach to constructing self-supervised training data while bridging symbolic knowledge and natural language. Experiments on both structured and naturally occurring text demonstrate that the proposed splitter generalizes beyond synthetic templates and that the resulting structure-aware supervision consistently improves downstream performance on knowledge graph completion and commonsense question answering, highlighting the effectiveness of recovering latent factual structure for knowledge-centric NLP.

## Metadata
- **Published**: 2026-07-22T07:30:39Z
- **Authors**: Ahmad Pouramini, Mahsa Afsharizadeh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19845v1)