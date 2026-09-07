---
title: Self-Supervised Lexical Representation Learning for Fast, Large-Scale Phylogenetic Inference
published: 2026-09-04T15:23:12Z
authors: Tim Wientzek
url: http://arxiv.org/abs/2609.05262v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Self-Supervised Lexical Representation Learning for Fast, Large-Scale Phylogenetic Inference

## Abstract
Computational phylogenetics has become an essential tool in historical linguistics, yet its application at a global scale remains constrained by two factors: the labor-intensive manual annotation of cognacy judgments required for character-based methods and the substantial computational cost of inference on large datasets. This paper introduces a fully self-supervised contrastive learning framework that learns lexical representations directly from raw IPA-transcribed wordlists, without requiring cognacy annotations, alignments, or additional expert input. The model employs a dual contrastive objective: a word-level loss that organizes phonetically similar forms into a coherent space, and an auxiliary language-level loss that encourages the lexical space to reflect broader phonological properties of languages. From the resulting word representations, pairwise language distances are derived and used to infer a global phylogenetic tree of 3,399 language varieties. The inferred tree achieves a generalized quartet distance (GQD) to the Glottolog reference tree competitive with multiple baselines, while requiring only minutes of computation on a standard notebook GPU. Furthermore, the same representations capture diachronic concept stability: variance in pairwise distances across languages yields stability rankings that correlate significantly with established rankings. Ablation studies confirm that both the language-level objective and the use of phonetic feature vectors improved the inferred trees topology with regards to GQD. The framework thus provides a computationally efficient and fully automatic alternative for large-scale phylogenetic inference and offers a unified representation supporting downstream analyses at both the language and concept level.

## Metadata
- **Published**: 2026-09-04T15:23:12Z
- **Authors**: Tim Wientzek
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05262v1)