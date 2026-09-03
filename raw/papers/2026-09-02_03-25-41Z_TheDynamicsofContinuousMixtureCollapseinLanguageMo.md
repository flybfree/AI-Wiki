---
title: The Dynamics of Continuous Mixture Collapse in Language Models
published: 2026-09-02T03:25:41Z
authors: Ali Backour
url: http://arxiv.org/abs/2609.02049v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Dynamics of Continuous Mixture Collapse in Language Models

## Abstract
LLMs latent-state reasoning methods replace discrete intermediate tokens with continuous states, such as weighted mixtures of token embeddings, to retain multiple possible reasoning directions rather than committing to one. Yet pretrained language models often fail to preserve these mixtures. We study why through a combination of theoretical analysis and controlled empirical investigations on a variety of models. We identify three independent, distinct sources of failure. First, transformer architectures already distort mixture geometry, and training substantially amplifies this effect. Moreover, the failure can occur even if the model transports mixtures perfectly linearly: the softmax readout and autoregressive feedback form a dynamical system that either amplifies small differences until one component of the mixture dominates or contracts different mixtures until they become indistinguishable. We verify this theoretical prediction empirically: the observed transition between contraction and amplification occurs near the theoretical threshold derived by our analysis, and pretrained-model rollouts lie predominantly on the amplifying side. Finally, we generalize to mixtures of many components and show that exact preservation generally requires context-dependent correction, whose required dimensionality can grow with the number of components.

## Metadata
- **Published**: 2026-09-02T03:25:41Z
- **Authors**: Ali Backour
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02049v1)