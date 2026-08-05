---
title: Designing a Good Virtual Node: Addressable and Cardinality-Preserving Global Memory for Message Passing Architectures
published: 2026-08-03T17:44:10Z
authors: Félix Marcoccia
url: http://arxiv.org/abs/2608.02709v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Designing a Good Virtual Node: Addressable and Cardinality-Preserving Global Memory for Message Passing Architectures

## Abstract
Virtual nodes give message-passing neural networks a simple global communication route, but the standard node--VN--node pipeline compresses the graph into one homogeneous state and broadcasts it identically to every node. Building on the Two-Radius analysis of Mishayev et al., we ask how auxiliary virtual memory can relieve this finite-capacity bottleneck without self-attention. We identify two requirements. First, the global memory should be factorized into independently writable and readable states: this can be achieved using addressable cross-attention slots. Second, addressability alone does not preserve multiplicity, because softmax attention is invariant to uniform replication. Inserting each slot query as a private key/value anchor recovers the discarded normalization mass and yields, on bounded color domains, an injective multiset representation able to implement a 1-WL refinement. Experiments on multiplicity-aware Two-Radius, motif counting, and constrained link-set prediction support this addressable and cardinality-preserving virtual memory at (O(nMd)) arithmetic cost.

## Metadata
- **Published**: 2026-08-03T17:44:10Z
- **Authors**: Félix Marcoccia
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02709v1)