---
title: Breaking the Compression Barrier: Cross-Architecture Compression Boundary Learning via Reverse Regrowth
published: 2026-08-17T01:59:23Z
authors: Zhaocen Liu, Satvik Praveen, Yi Sheng
url: http://arxiv.org/abs/2608.16010v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Breaking the Compression Barrier: Cross-Architecture Compression Boundary Learning via Reverse Regrowth

## Abstract
Model compression is critical for deploying networks on resource-constrained edge devices. While pruning-based methods can significantly reduce model size, they often suffer from abrupt performance collapse beyond a sparsity thresh-old, making it difficult to identify the feasible compression limit of the model. To address this challenge, we propose a boundary-Learning reverse regrowth framework, BRIDGE, that reformulates compression as a constructive boundary-search problem. Unlike forward pruning, our method first drives the model to an extremely sparse state to expose the collapse region, and then selectively regenerates the critical structure to restore performance. The proposed framework employs a hierarchical regeneration strategy, including coarse-grained layer selection and fine-grained regeneration parameter selection, to accurately identify which parameters require recovery. Experiments show that our method can recover models from the brink of collapse on both CNNs and Transformer architectures, demonstrating its architecture in-dependence. BRIDGE achieves a performance improvement of up to 1.49% in unstructured pruning and up to 4.77% in structured pruning. These results demonstrate that reverse regeneration can effectively extend the compression limit while maintaining stable performance. The source code is available at https://github.com/EnumaCaliber/BRIDGE.

## Metadata
- **Published**: 2026-08-17T01:59:23Z
- **Authors**: Zhaocen Liu, Satvik Praveen, Yi Sheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16010v1)