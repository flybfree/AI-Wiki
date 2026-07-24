---
title: Retrieval is Enough: Training-Free Interpretability with a Tool-Using Agent
published: 2026-07-17T18:47:31Z
authors: Sriram Balasubramanian, Soheil Feizi
url: http://arxiv.org/abs/2607.16448v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Retrieval is Enough: Training-Free Interpretability with a Tool-Using Agent

## Abstract
Interpretability methods for neural network activations span a wide cost spectrum, from cheap, training-free techniques (such as linear probes, PCA, SVD) to more expensive training-based ones (such as SAEs and activation oracles). Training-based methods are typically more powerful, in part because they leverage large activation datasets during training. This raises a natural question - do they actually surface insights that go beyond what is recoverable from the training dataset itself? To address this, we equip an LLM agent with a vector database of activations paired with their textual contexts, along with tools for manipulating activations - projecting out directions in latent space, computing activation differences and averages. The agent iteratively queries the database, forms hypotheses from the retrieved samples, and validates them by constructing linear probes. We call this method HARP, for Hypothesis-driven Agentic Retrieval and Probing. Despite not involving any training, HARP outperforms both activation oracles and SAE-based agents on concept discovery, concept detection, model steering, and secret elicitation. The training-free design also makes HARP substantially cheaper and more flexible: new datasets can be indexed on demand whenever existing ones prove insufficient. More broadly, our results suggest that current training-based methods do not yet extract insights beyond their training data, and motivate benchmarks that explicitly require interpretability methods to demonstrate such insights. We release our code at https://github.com/SriramB-98/HARP

## Metadata
- **Published**: 2026-07-17T18:47:31Z
- **Authors**: Sriram Balasubramanian, Soheil Feizi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.16448v1)