---
title: Where You Measure Decides What You Measure: Position Selection in Ablation-Based SAE Evaluation
published: 2026-08-13T15:06:56Z
authors: Valentin Noël
url: http://arxiv.org/abs/2608.13337v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Where You Measure Decides What You Measure: Position Selection in Ablation-Based SAE Evaluation

## Abstract
Sparse autoencoders are meant to name the things a language model computes, and the usual way to check that a latent matters is to switch it off and see what changes. But a latent fires at many tokens, and the effect has to be measured at one of them. The convention is to measure where the latent fires hardest. That choice is almost never reported, and it is not made by the experimenter: it is made by the dictionary under evaluation. Change the dictionary and the measurement moves to a different token. We show this is not a detail. Take two sparse autoencoders released by Google for the same model and match their latents by decoder similarity: even among the pairs the two dictionaries encode almost identically, they pick different tokens for a large share of them. Two dictionaries compared under the usual protocol are therefore very often compared at different places. To separate the convention from the dictionaries we train six autoencoders from one initialisation, differing only in fitting choices, so that a latent means the same thing in each. Most of the variance such a comparison reads as "these dictionaries disagree about this latent" turns out to be the position instead: it falls from 7.6% and 11.9% of variance to near zero once every dictionary is measured at the same token. More evaluation data does not rescue it. Across a sixteenfold range of corpus sizes the dictionaries agree less about where to measure, not more, so the problem grows with scale. The correction is one line of evaluation code. We give the protocol an ablation-based causal number must report to be comparable across papers, and an audit of five published papers against it. In short: a causal number reported without its position describes the token it was taken at as much as the latent it was taken from.

## Metadata
- **Published**: 2026-08-13T15:06:56Z
- **Authors**: Valentin Noël
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13337v1)