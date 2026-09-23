---
title: Hill Sampling for Test-Time Scaling: A Simple and Better Alternative to Repeated Sampling, Evolution, and Training
published: 2026-09-22T00:08:12Z
authors: Jacob Beck, Philip V. Ogren, Ari Kobren
url: http://arxiv.org/abs/2609.25510v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hill Sampling for Test-Time Scaling: A Simple and Better Alternative to Repeated Sampling, Evolution, and Training

## Abstract
Large language models (LLMs) can improve solutions to verifiable scientific and algorithmic problems by spending additional computation at test time. Recent systems achieve strong results with increasingly elaborate evolutionary search harnesses or by updating model parameters during test-time training. We ask how much of this machinery is necessary. We introduce Hill Sampling, a simple procedure that repeatedly samples candidate program edits from a frozen LLM, retains the best program found so far, and conditions all subsequent samples on that program. We evaluate the method on circle packing, sums/differences of sets, and Erdos' minimum-overlap problem using three open-weight models. Hill Sampling sets a new state of the art on circle packing among published methods, improves over the AlphaEvolve reference on Erdos' minimum-overlap problem, and achieves strong results on sums and differences of finite sets. The circle-packing and Erdos results require only hours of wall-clock time on eight NVIDIA H100 GPUs. To our knowledge, we also conduct, the largest study, by parameter count, of evolution strategies (ES) applied directly to LLM weights at test time. Surprisingly, learning the weights is worse than setting the ES learning rate to zero: at zero learning rate, the method is still searching in weight space through fixed random perturbations. Those perturbations can help exploration, but randomness from token sampling is stronger still, and repeated sampling remains substantially weaker than Hill Sampling. These results suggest a simple test-time compute allocation strategy: repeatedly sample edits to the best verified solution found so far, before introducing additional complexity such as adding archives, diversity mechanisms, evolutionary scaffolds, or test-time parameter learning.

## Metadata
- **Published**: 2026-09-22T00:08:12Z
- **Authors**: Jacob Beck, Philip V. Ogren, Ari Kobren
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.25510v1)