---
title: Logical Embeddings for Argument Analysis
published: 2026-08-15T17:03:05Z
authors: Leander Heldring, Santiago Torres
url: http://arxiv.org/abs/2608.15325v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Logical Embeddings for Argument Analysis

## Abstract
We propose a new framework for machine-learning-oriented argument analysis tasks. Our proposal involves replacing traditional contextualized word embeddings used in most NLP tasks with logical embeddings, an alternative encoding that directly exploits argumentation structures. In essence, logical embeddings encapsulate the logical semantics of an argument, allowing for a better representation of its meaning. Supporting these embeddings is a mathematical logic-based similarity measure that offers a transparent notion of proximity and is guaranteed to satisfy several desirable theoretical properties that current cosine similarity-based contextualized word embeddings cannot assure. This similarity measure induces a positive semi-definite kernel on the set of arguments, enabling us to uniquely define logical embeddings using the theory of Reproducing Kernel Hilbert Spaces (RKHS). Moreover, we prove that this encoding is optimal, in the sense that no logical information is lost in the process. As with other RKHS applications, logical embeddings can be used in numerous supervised and unsupervised tasks. We provide an implementation of the method and aim to test it against literature benchmarks. Additionally, we demonstrate that logical embeddings outperform most standard embedding methods on a classification task.

## Metadata
- **Published**: 2026-08-15T17:03:05Z
- **Authors**: Leander Heldring, Santiago Torres
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15325v1)