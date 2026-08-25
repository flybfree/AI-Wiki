---
title: Exploring Dowker Homology for Sentence Similarity
published: 2026-08-24T07:41:32Z
authors: Marius Huber, Juri Opitz
url: http://arxiv.org/abs/2608.22909v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Exploring Dowker Homology for Sentence Similarity

## Abstract
Dowker homology is a topological tool that may be used to analyze the relative position of two point clouds living in a common space. We investigate whether Dowker homology captures sentence similarity information by treating the embeddings of the tokens that constitute a sentence pair as a pair of point clouds in the latent space of a transformer model, using both models that have and have not been fine-tuned for sentence similarity. We find that Dowker homology captures sentence similarity information, as measured by regressing Dowker homology features onto ground-truth similarity scores, and that it can be used for visual inspection of similarity data and models. In an attempt to make Dowker homology readily applicable, we derive from it single-number summaries that we expect to capture sentence similarity directly. These turn out to work reasonably well, but without outperforming standard sentence similarity measures based on established pooling methods.

## Metadata
- **Published**: 2026-08-24T07:41:32Z
- **Authors**: Marius Huber, Juri Opitz
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22909v1)