---
title: SAEVerbalizer: Generating Explanations for Sparse Autoencoder Features via Representation Verbalization
published: 2026-08-13T17:54:11Z
authors: Weihan Meng, Hongzhu Guo, Yi Jing, Dewen Liu, Zijun Yao, Xiaozhi Wang, Lei Hou, Juanzi Li
url: http://arxiv.org/abs/2608.13538v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SAEVerbalizer: Generating Explanations for Sparse Autoencoder Features via Representation Verbalization

## Abstract
Sparse autoencoders (SAEs) are proposed to extract numerous features from large language model (LLM) representations, yet explaining these features still relies primarily on external observation. This reliance leads to superficial explanations inferred from observed model behavior and computational inefficiency from collecting such behavioral evidence at scale. We introduce SAEVerbalizer, a framework that injects SAE decoder directions into an LLM's representations and fine-tunes the LLM's downstream layers to generate natural-language explanations of the injected features. Once trained, the resulting verbalizer explains SAE features directly from decoder directions, addressing both limitations. Our experiments show that the learned verbalization capability generalizes to unseen features, transfers across separately trained SAE dictionaries, and, with a lightweight adapter, extends to SAE features from different LLMs. Intervention experiments show that injecting multiple directions yields an explanation combining their meanings, while reversing individual directions produces corresponding meaning shifts.

## Metadata
- **Published**: 2026-08-13T17:54:11Z
- **Authors**: Weihan Meng, Hongzhu Guo, Yi Jing, Dewen Liu, Zijun Yao, Xiaozhi Wang, Lei Hou, Juanzi Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13538v1)