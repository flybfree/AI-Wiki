---
title: Superposed Latent Autoencoder
published: 2026-09-01T12:35:08Z
authors: Quanling Zhao, Jiaying Yang, Tianqi Zhang, Ziyang Hao, Fatemeh Asgarinejad, Flavio Ponzina, Tajana Rosing
url: http://arxiv.org/abs/2609.01158v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Superposed Latent Autoencoder

## Abstract
Autoencoders typically meet tight latent-memory budgets by making each latent representation smaller, sacrificing representational capacity. We ask a different question: can multiple wider latents be stored together instead? We introduce the Superposed Latent Autoencoder (SLAE), which preserves high-capacity latent representations while sharing storage through learned superposition. SLAE transforms latents into storage-friendly codes, binds them with randomized keys, superposes multiple codes into a single memory tensor, and learns to recover each latent before decoding. Under the same storage budget, SLAE replaces irreversible dimensional bottlenecks with structured interference that can be suppressed. Across CIFAR-10/100, SVHN, STL-10, Tiny ImageNet, and a wide range of memory budgets, SLAE substantially improves the reconstruction--memory tradeoff, reducing reconstruction error by up to 56% over conventional autoencoders at matched storage. Further analysis shows that SLAE's advantage comes from making wider representations usable under the same storage budget. These gains also extend beyond reconstruction: the information preserved by SLAE improves downstream classification by up to 16.79 percentage points under the same memory budget. Our results suggest a new principle for representation compression: instead of making every latent smaller, keep representations wide and let them share memory.

## Metadata
- **Published**: 2026-09-01T12:35:08Z
- **Authors**: Quanling Zhao, Jiaying Yang, Tianqi Zhang, Ziyang Hao, Fatemeh Asgarinejad, Flavio Ponzina, Tajana Rosing
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01158v1)