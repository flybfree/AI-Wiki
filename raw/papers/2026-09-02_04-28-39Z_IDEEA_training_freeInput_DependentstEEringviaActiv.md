---
title: IDEEA: training-free Input-Dependent stEEring via Activation cluster matching
published: 2026-09-02T04:28:39Z
authors: Zheng Wang, Muchen Li, Renjie Liao, Yan Leng
url: http://arxiv.org/abs/2609.02089v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# IDEEA: training-free Input-Dependent stEEring via Activation cluster matching

## Abstract
Steering aligns large language models (LLMs) by injecting a bias into selected activations at inference time, offering a far cheaper alternative to weight-update methods such as supervised fine-tuning or reinforcement learning. However, most existing training-free steering methods are input-independent: a single direction is fitted once and shared across all inputs. This is fundamentally limiting as different inputs occupy different regions of the activation space and admit different optimal steering directions toward the same target concept, much as the gradient with respect to a fixed loss varies from input to input. We close this gap with IDEEA (Input-Dependent stEEring via Activation cluster matching), a training-free framework for input-dependent steering. IDEEA clusters the positive and negative activation supports per attention head, and solves an optimal-matching problem to construct a set of cluster-conditional directions, all about the target concept. At inference time, it picks from this pool of directions and uses the one that best matches the input's own activation for steering. IDEEA aligns the model toward the target concept while preserving the input's original representation, evidence that activations encoding a concept occupy several distinct sub-regions of the representation space rather than a single one. IDEEA improves the truth $\times$ info rate in TruthfulQA by an average of 9.9% (up to 23.5%) over the best input-independent baseline.

## Metadata
- **Published**: 2026-09-02T04:28:39Z
- **Authors**: Zheng Wang, Muchen Li, Renjie Liao, Yan Leng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02089v1)