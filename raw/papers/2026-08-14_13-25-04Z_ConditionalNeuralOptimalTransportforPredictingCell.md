---
title: Conditional Neural Optimal Transport for Predicting Cellular Phenotypes from Molecular Structure
published: 2026-08-14T13:25:04Z
authors: Gauthier Avité, Maxime Sanchez-Renauld, Nicolas Bourriez, Auguste Genovesio
url: http://arxiv.org/abs/2608.14293v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Conditional Neural Optimal Transport for Predicting Cellular Phenotypes from Molecular Structure

## Abstract
High-content microscopy enables systematic profiling of cellular responses to chemical perturbations, but the scale of the chemical space makes exhaustive phenotypic characterization experimentally infeasible. This motivates computational models that can predict image-derived phenotypes without acquiring the corresponding treated cells. We formulate molecule-induced phenotype prediction as an inductive conditional transport problem in image representation space. Given a negative-control phenotype and the structure of a molecule, we aim to predict the phenotype induced by the corresponding molecule. We first evaluate classical optimal transport baselines and show that static couplings do not yield useful predictions on large-scale phenotypic image datasets. We then introduce a molecule-conditioned Neural Optimal Transport (NOT) model with a Monge-Gap regularization training objective that learns to transport negative-control unperturbed phenotypes toward perturbed phenotypes using molecular structure as conditioning information. NOT recovers molecule-specific phenotypic effects while reducing microscopy-associated technical variation, thereby facilitating comparisons across experimental batches. On unseen active molecules, the model outperforms baseline approaches, demonstrating that chemically conditioned transport can generalize beyond the molecules observed during training. We identified the molecular encoder as the main limitation to this generalization, while transport in a compressed representation space improves performance and scalability. These results establish NOT as a promising framework for predicting cellular phenotypes from molecular structure and negative-control phenotypes, while highlighting the development of more informative molecular representations as a key direction for improving out-of-distribution performance.

## Metadata
- **Published**: 2026-08-14T13:25:04Z
- **Authors**: Gauthier Avité, Maxime Sanchez-Renauld, Nicolas Bourriez, Auguste Genovesio
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14293v1)