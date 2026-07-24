---
title: Differentiable Clone-Structured Causal Graphs for End-to-End Cognitive Map Learning from Image Sequences
published: 2026-07-14T05:54:39Z
authors: Arash Nikzad, Sasan Sarbishegi, Ali Dasmeh, Muhammad Asif, Parsa Gharavi, Erik Husom, Sagar Sen, Andrew B. Lehr, Olivier Penacchio, Ana Clemente, Tristan M. Stöber
url: http://arxiv.org/abs/2607.12382v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Differentiable Clone-Structured Causal Graphs for End-to-End Cognitive Map Learning from Image Sequences

## Abstract
How can an agent build a structured map of its world from nothing but an ongoing sequence of raw sensory input and its own movements, especially when natural variation means exact sensory patterns rarely repeat? The Clone-Structured Causal Graph algorithm (CSCG), a normative hippocampus model, shows how an interpretable map can be learned from aliased observations. However, CSCG requires a predefined discrete alphabet, and its expectation-maximization formulation is not easily combined with existing neural network modules, preventing the end-to-end processing of raw image sequences. We remove this barrier by reformulating CSCG as a single, fully differentiable module, gradCSCG, and coupling it to a learned vector-quantized variational autoencoder (VQ-VAE) perceptual front-end. A soft emission forward pass allows the map-learning objective to flow back into perception, while a set of loss-balancing mechanisms mitigates module collapse during joint training. We demonstrate, first, that gradient training reproduces CSCG's results on original symbolic grid worlds by recovering room topology from heavily aliased observations. Second, we show that map recovery remains robust on MNIST image sequences, where each visit to a location yields a newly sampled image of its assigned digit. Across four heavily aliased environments, the end-to-end pipeline successfully uncovers the underlying adjacency graph with high edge precision and recall, directly from visual input. This work provides a proof of principle that CSCG can serve as a composable building block in a deep learning architecture.

## Metadata
- **Published**: 2026-07-14T05:54:39Z
- **Authors**: Arash Nikzad, Sasan Sarbishegi, Ali Dasmeh, Muhammad Asif, Parsa Gharavi, Erik Husom, Sagar Sen, Andrew B. Lehr, Olivier Penacchio, Ana Clemente, Tristan M. Stöber
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.12382v1)