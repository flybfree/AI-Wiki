---
title: Entangled Representations Amplify Collateral Damage in Unlearning
published: 2026-09-02T08:35:14Z
authors: Evžen Wybitul, Tim G. J. Rudner, Christian Schroeder de Witt
url: http://arxiv.org/abs/2609.02285v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Entangled Representations Amplify Collateral Damage in Unlearning

## Abstract
A long-held intuition in interpretability research is that representational entanglement, the sharing of structure between knowledge domains in a neural network, makes unlearning harder. While the intuition is widespread, it has never been directly tested in a controlled experiment. We present a way to do so: by repurposing Selective Gradient Masking (SGTM), we train a suite of six 254M-parameter language models on English Wikipedia with graded levels of disentanglement between biology and non-biology knowledge. Applying three standard unlearning methods to every model in the suite, we find that more disentangled models consistently achieve better retain-forget trade-offs: at a fixed level of forgetting, the most disentangled models incur roughly $4\times$ lower retain cost under two of the three methods, and $1.3\times$ lower under the third. Because our intervention changes only the model, not the data or the unlearning algorithm, this is direct evidence that representational entanglement is one of the causes of collateral damage in unlearning, as interpretability researchers have long suspected. A similar design could be used to test other structural claims from interpretability.

## Metadata
- **Published**: 2026-09-02T08:35:14Z
- **Authors**: Evžen Wybitul, Tim G. J. Rudner, Christian Schroeder de Witt
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02285v1)