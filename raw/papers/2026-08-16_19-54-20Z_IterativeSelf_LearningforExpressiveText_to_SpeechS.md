---
title: Iterative Self-Learning for Expressive Text-to-Speech Synthesis
published: 2026-08-16T19:54:20Z
authors: Nicholas Sanders, Gustav Eje Henter, Simon King, Korin Richmond
url: http://arxiv.org/abs/2608.15910v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Iterative Self-Learning for Expressive Text-to-Speech Synthesis

## Abstract
Expressive text-to-speech (TTS) systems that use explicit conditioning labels provide direct and interpretable control over expressive attributes, in contrast to reference-based or prompting-based approaches, but require labeled data. Obtaining these labels at scale is costly and time-consuming, yet no prior semi-supervised framework addresses this specific bottleneck. Existing semi-supervised TTS methods instead target scarcity of paired speech-text data or transcriptions. To address the scarcity of expressive labels, we propose an Iterative Self-Learning (ISL) framework for expressive TTS, built on Invert-Classify, a classifier-free method that recovers discrete expressive labels by inverting a frozen generative model. The framework iteratively pseudo-labels unlabeled speech using the current model, retrains on the combined labeled and pseudo-labeled data, and repeats, progressively refining label quality and synthesis. We validate on two expressive tasks, word-level prominence and utterance-level emotion, across multiple low-resource data splits. We find that iterative refinement can improve pseudo-label accuracy over single-pass baselines. Furthermore, we observe that these improvements in pseudo-labeling of expressivity translate to gains in expressive label adherence and synthesis quality, confirmed by objective metrics and human listening tests. In the most data-scarce conditions, ISL-trained models outperform single-pass pseudo-labeling and further approach fully supervised performance, demonstrating that gradient-based ISL is an effective solution to expressive label scarcity in low-resource TTS.

## Metadata
- **Published**: 2026-08-16T19:54:20Z
- **Authors**: Nicholas Sanders, Gustav Eje Henter, Simon King, Korin Richmond
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15910v1)