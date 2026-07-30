---
title: Learning the Word Problem: Geodesic Lengths and Cryptographic Applications
published: 2026-07-28T20:22:47Z
authors: Elisabeth Fink
url: http://arxiv.org/abs/2607.26241v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning the Word Problem: Geodesic Lengths and Cryptographic Applications

## Abstract
The Word Problem has been a subject of intensive mathematical study for over a century, initially driving advances in combinatorial group theory and more recently emerging as a foundational hardness assumption in post-quantum cryptography (PQC). While generally undecidable, several families of infinite non-abelian groups exhibit solvable or algorithmically fast word problems, making them attractive platforms for cryptographic design. This paper introduces WPNet, a novel Graph Neural Network architecture capable of solving the Word Problem heuristically, which is demonstrated on the Baumslag-Solitar group $BS(1,2)$ and on an Artin group. By mapping unreduced words to dynamic graph structures, the model learns to cluster algebraically equivalent elements in a continuous embedding space, effectively identifying the geodesic representative of a word without executing discrete reduction steps. As an application, a model variant is developed that can predict the geodesic length of an unreduced word in both groups. To demonstrate the cryptographic severity of this structural leakage, WPNet is successfully deployed against the Wagner-Magyarik public-key cryptosystem.

## Metadata
- **Published**: 2026-07-28T20:22:47Z
- **Authors**: Elisabeth Fink
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26241v1)