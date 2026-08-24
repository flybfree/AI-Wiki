---
title: Fine-Grain GPU Parallelization of the Generalized Partition Crossover for Large-Scale Traveling Salesman Problems
published: 2026-08-21T15:42:05Z
authors: Swetha Varadarajan, Darrell Whitley
url: http://arxiv.org/abs/2608.21233v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fine-Grain GPU Parallelization of the Generalized Partition Crossover for Large-Scale Traveling Salesman Problems

## Abstract
The Traveling Salesman Problem (TSP) is one of the most extensively studied NP-hard optimization problems. Genetic Algorithm (GA)-based solvers, such as the Edge Assembly Crossover (EAX), achieve state-of-the-art performance on many benchmark instances. However, the scalability of these approaches in massively parallel architectures remains limited because crossover operations involve irregular memory access patterns, graph traversals, and sequential dependencies. Existing GPU-based TSP solvers primarily exploit population-level parallelism and are limited to relatively small problem sizes. This work presents a fine-grain GPU implementation of the partition phase of the Generalized Partition Crossover (GPX) operator for large-scale TSP instances. The proposed approach reformulates GPX partitioning as a graph-parallel problem using coalesced memory layouts, ghost-node transformations, and connected-component analysis. The im- plementation parallelizes the union of parent tours, the splitting of degree- four vertices, the deletion of common edges, and the identification of recombining components using CUDA. Experimental results on instances ranging from 10,000 to 2 million cities demonstrate substantial acceleration over a naive sequential CPU imple- mentation. The proposed GPU partitioning achieves speedups between 48x and 625x while significantly reducing memory overhead. The re- sults demonstrate that operator-level parallelism can substantially im- prove the scalability of GA-based TSP solvers on modern many-core architectures.

## Metadata
- **Published**: 2026-08-21T15:42:05Z
- **Authors**: Swetha Varadarajan, Darrell Whitley
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21233v1)