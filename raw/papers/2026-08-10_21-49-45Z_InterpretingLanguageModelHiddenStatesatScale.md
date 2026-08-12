---
title: Interpreting Language Model Hidden States at Scale
published: 2026-08-10T21:49:45Z
authors: Jordan Pettyjohn, Mansi Sakarvadia, Nathaniel Hudson, Daniel McKenzie, Kyle Chard, Ian Foster
url: http://arxiv.org/abs/2608.10260v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Interpreting Language Model Hidden States at Scale

## Abstract
Lens methods interpret large language models (LLMs) by mapping intermediate activations to the output vocabulary, revealing how next-token predictions develop through the network. Trained lenses remain expensive: affine-translator parameters grow quadratically with model width, while exact, full-vocabulary Kullback--Leibler (KL) training dominates memory. Consequently, prior trained lenses have been applied to models of at most 20B parameters and remain tied to particular component types. We present OmniLens, which applies a single lens family to any model-width activation, whether residual stream, attention, or MLP, and combines two independent scaling techniques. First, low-rank translators make per-lens parameter growth linear in model width and reduce trainable parameters by up to 98.4%. Second, Subset-KL materializes only selected vocabulary logits: its Top-k mode cuts peak training memory by up to 70%, while its importance-sampled variant retains unbiased stochastic gradients for the full KL. These savings enable a dense ensemble of 482 lenses for LLaMA-3.3-70B, providing 6x the coverage of a residual-stream design at the same depth. Model-wide coverage then reveals what single-component lenses cannot: the components where a behavior is most visible need not be those where intervention is most effective, and the most effective interventions lie outside the attention heads examined by prior lens studies. Across three case studies (prompt-injection detection, multi-hop memory injection, and toxicity localization), OmniLens reproduces key published results at substantially lower cost.

## Metadata
- **Published**: 2026-08-10T21:49:45Z
- **Authors**: Jordan Pettyjohn, Mansi Sakarvadia, Nathaniel Hudson, Daniel McKenzie, Kyle Chard, Ian Foster
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10260v1)