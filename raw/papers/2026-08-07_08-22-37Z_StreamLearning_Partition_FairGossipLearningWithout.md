---
title: Stream Learning: Partition-Fair Gossip Learning Without Tokens
published: 2026-08-07T08:22:37Z
authors: Fabien Mathieu, Alexandre Pham, Maria Gradinariu Potop-Butucaru, S{é}bastien Tixeuil
url: http://arxiv.org/abs/2608.06946v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Stream Learning: Partition-Fair Gossip Learning Without Tokens

## Abstract
In gossip learning, a network of nodes trains a shared model collaboratively, without a central coordinator, by repeatedly exchanging parts of their local models. The state-of-the-art protocol, Partitioned Token Gossip Learning (PTGL) of Heged{ü}s et al., splits the weight matrix into S fixed partitions and disseminates them using a token-based fairness mechanism coupled with per-neighbor metadata exchange. We revisit partition scheduling by analogy with peer-to-peer live streaming, where model partitions act as video chunks and partition age acts as chunk scarcity. The analogy yields a design space of two-stage selection strategies (partition first, or neighbor first), from which we instantiate ten concrete protocols collectively called Stream Learning. Our main finding is that the simplest of these protocols, which transmits the locally least-trained partition to a uniformly random neighbor (Ri), matches PTGL on fault-free workloads while requiring neither token counters nor metadata exchange. Under an adversarial 30% permanent crash of the best-performing nodes, Ri matches or outperforms PTGL across all complete-graph configurations tested, with the gap reaching 5.53% on HAR and 5.41% on MNIST in the most heterogeneous regime (Dirichlet $β$ = 0.1). In our experiments, partition fairness, captured by a single local rule on partition age, accounts for the gap; token-based rate control and utility maximization do not improve over this rule and, under heterogeneity, sit below it.

## Metadata
- **Published**: 2026-08-07T08:22:37Z
- **Authors**: Fabien Mathieu, Alexandre Pham, Maria Gradinariu Potop-Butucaru, S{é}bastien Tixeuil
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06946v1)