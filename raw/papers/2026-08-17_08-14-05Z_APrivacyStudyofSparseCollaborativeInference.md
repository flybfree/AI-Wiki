---
title: A Privacy Study of Sparse Collaborative Inference
published: 2026-08-17T08:14:05Z
authors: Maximilian Andreas Hoefler, Karsten Mueller, Wojciech Samek
url: http://arxiv.org/abs/2608.16236v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Privacy Study of Sparse Collaborative Inference

## Abstract
Collaborative inference (CI) splits a model between an edge device and a server, whereby the client computes an intermediate activation, transmits it, and the server completes the computation. This raises two concerns, the communication cost of the transmission and the risk that it reveals private information about the input. Recent work reduces this cost by sparsifying activations and entropy-coding the result. Sparsity has also been argued to improve privacy, on the intuition that transmitting fewer values reveals less about the input. We test this claim by decomposing the sparse activation into the retained values and the set of positions they occupy, and by reconstructing inputs from each component in isolation. We find that sparsification reduces the leakage far less than it reduces the transmission cost, and that the remaining risk shifts to the positions, which prior analyses treat as side information for decoding. Across natural-image and face datasets, the positions alone constitute a serious privacy risk, enabling high-fidelity reconstructions and re-identification of individuals. The leakage from the positions persists even when both the transmission cost and the task utility are low. We conclude that the positions of sparse activations should be treated as sensitive transmitted data and audited carefully in the context of collaborative inference. Code is available at https://github.com/an7123/Privacy-Study-Sparse-CI.

## Metadata
- **Published**: 2026-08-17T08:14:05Z
- **Authors**: Maximilian Andreas Hoefler, Karsten Mueller, Wojciech Samek
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16236v1)