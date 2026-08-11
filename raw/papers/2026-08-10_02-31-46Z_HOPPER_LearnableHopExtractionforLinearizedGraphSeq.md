---
title: HOPPER: Learnable Hop Extraction for Linearized Graph Sequence Models
published: 2026-08-10T02:31:46Z
authors: Isuru Herath, Arin Gopakumar, Sharan Sahu
url: http://arxiv.org/abs/2608.09031v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HOPPER: Learnable Hop Extraction for Linearized Graph Sequence Models

## Abstract
Graph neural networks typically propagate information through repeated message-passing layers, coupling the distance over which information travels with the number of nonlinear transformations applied. This coupling can make deep architectures difficult to optimize and can lead to over-smoothing, over-squashing, and the loss of long-range information. Linearized Graph Sequence Models (LGSMs) address this issue by separating information depth from processing depth and treating the successive propagation states of each node as a sequence. However, existing LGSMs construct these sequences using fixed graph operators, limiting their ability to adapt propagation to the input graph, node features, and downstream task. We introduce HOPPER, an end-to-end learnable extension of LGSM that learns how hop sequences should be extracted before they are processed by a modern state-space model. Our framework supports feature-conditioned, structure-aware, graph- and hop-adaptive propagation mechanisms while preserving permutation equivariance. Standard adjacency-based and non-backtracking LGSM sequences arise as special cases of our proposed extractor family. We show that HOPPER is state-of-the-art or competitive across the ECHO-Synth benchmark, and that varying the maximum neighborhood size of message backtracking cancellation (i.e. structural memory window) can optimize accuracy on the LRIM physics-based long-range dependency benchmark. These results demonstrate that learnable sequence extraction provides a flexible and effective approach to long-range graph representation learning.

## Metadata
- **Published**: 2026-08-10T02:31:46Z
- **Authors**: Isuru Herath, Arin Gopakumar, Sharan Sahu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09031v1)