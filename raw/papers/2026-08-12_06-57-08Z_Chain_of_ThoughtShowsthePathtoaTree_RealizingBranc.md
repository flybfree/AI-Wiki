---
title: Chain-of-Thought Shows the Path to a Tree: Realizing Branching Complexity
published: 2026-08-12T06:57:08Z
authors: Debanjan Dutta, Anish Chakrabarty, Swagatam Das
url: http://arxiv.org/abs/2608.11716v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Chain-of-Thought Shows the Path to a Tree: Realizing Branching Complexity

## Abstract
Chain of Thought (CoT) lifts the expressive ceiling of bounded-depth Transformers, with characterizations tying the number of CoT steps to circuit complexity classes. What remains largely missing are concrete instantiations with explicit, depth-bounded constructions, and the traversal procedures such characterizations presuppose. We close this gap for branching complexity. We give CoT realizations of depth-first search (DFS) and of Dijkstra algorithm, the latter subsuming breadth-first search, by unique hard-attention decoders of at most two layers, and use them as a shared computational substrate: reusing the DFS decoder yields the Strahler number of an $n$-vertex tree in $2n-1$ steps with four layers, and reusing the Dijkstra decoder yields its width in $n-1$ steps with three. Since computing the Strahler number of a binary tree given as a term is \textsf{NC\textsuperscript{1}}-complete, and our constructions handle arbitrary $n$-ary trees without layer normalization or positional encodings, this is a non-trivial witness for the linear-step regime of the CoT hierarchy. Exploiting the classical bijection between ordered trees and Dyck paths, itself realized by our DFS construction, which emits the path as it traverses, we give independent constructions for both measures on the path representation.

## Metadata
- **Published**: 2026-08-12T06:57:08Z
- **Authors**: Debanjan Dutta, Anish Chakrabarty, Swagatam Das
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11716v1)