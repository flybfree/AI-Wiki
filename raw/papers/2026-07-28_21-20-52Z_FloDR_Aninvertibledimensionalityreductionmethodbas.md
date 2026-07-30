---
title: FloDR: An invertible dimensionality reduction method based on a normalising flow
published: 2026-07-28T21:20:52Z
authors: Abdallah Baraka, Daniel Probst
url: http://arxiv.org/abs/2607.26278v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FloDR: An invertible dimensionality reduction method based on a normalising flow

## Abstract
It is common for two-dimensional embeddings of high-dimensional data to be read far beyond what they can support. Distances in and between clusters, the meaning behind empty spaces, and the amount of structure hidden at each point are generally invisible in the output of methods such as t-SNE and UMAP. This is because the information that could support the meaning of these properties is discarded during the optimisation process. Here, we present FloDR, a dimensionality reduction method that embeds data through an invertible normalising flow. While FloDR only uses the first two output coordinates to create a two-dimensional embedding, it retains the remaining coordinates rather than discarding them. In addition to the embedding, an exact inverse and an exact density are properties of a trained mapping, which enable diagnostic visualisations that are computed from the exact inverse of the model that drew the layout rather than from an approximate one. Specifically, we draw two fields, the conditional spread, which measures how much of the original data remains undetermined at each embedding position in input units, and the hidden contrast, which measures how much information about a labelled contrast the two plotted coordinates discard. Both fields are rendered with a prespecified test against a held out portion of the input data and a bootstrap confidence. A field that fails the test is reported as refused.

## Metadata
- **Published**: 2026-07-28T21:20:52Z
- **Authors**: Abdallah Baraka, Daniel Probst
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26278v1)