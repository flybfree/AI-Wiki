---
title: Infinite-Parameter LLMs: Generating and Adapting Weights from Live Data
published: 2026-09-16T15:49:34Z
authors: Jinli Hu, Ross M. Clarke, Yichuan Zhang, José Miguel Hernández-Lobato
url: http://arxiv.org/abs/2609.18842v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Infinite-Parameter LLMs: Generating and Adapting Weights from Live Data

## Abstract
The scaling laws hold that a language model grows more capable with more parameters and more training data, and Mixture-of-Experts (MoE) architectures have ridden these laws to remarkable results, activating only a fraction of an enormous stored parameter bank for each token. That success is built on static pretraining data. A deployed model faces a different world, where much of the data that would make it more useful is not in its training set but in the live interaction it is currently handling, such as the facts a user supplies or the corrections they give. A conventional model cannot learn from this data, because its weights are frozen after training. Instead, the knowledge and behaviour supplied at run time are placed in the prompt, by retrieval or instruction, and re-read on every request only to be discarded once the request ends. We ask how an architecture could learn from live interaction by writing it into its weights. Taking inspiration from MoE, we propose the \textbf{Infinite-Parameter LLM}. A compact hypernetwork turns the data given at run time into a low-rank modulation of a shared base network, so the feed-forward weights are generated from live data rather than stored in a fixed bank. Where prior weight generators read the context once and freeze, we carry a Bayesian belief over the generator's latent code and update it online, so the effective weight is re-derived from that evolving belief as the session proceeds rather than fixed after one read. The stored footprint stays fixed, yet the weights the model can compile are effectively infinite. For the knowledge and behaviour supplied at run time, carrying them in the weights rather than the prompt is amortized in compute, frees the context window, persists across turns, and can generalise better than in-context use. We specify an evaluation protocol that tests exactly this against in-context learning and retrieval.

## Metadata
- **Published**: 2026-09-16T15:49:34Z
- **Authors**: Jinli Hu, Ross M. Clarke, Yichuan Zhang, José Miguel Hernández-Lobato
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.18842v1)