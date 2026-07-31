---
title: It's All Just Vectorization: einx, a Universal Notation for Tensor Operations
published: 2026-07-30T10:33:04Z
authors: Florian Fervers, Sebastian Bullinger, Christoph Bodensteiner, Michael Arens
url: http://arxiv.org/abs/2607.27987v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# It's All Just Vectorization: einx, a Universal Notation for Tensor Operations

## Abstract
Tensor operations represent a cornerstone of modern scientific computing. However, the Numpy-like notation adopted by predominant tensor frameworks is often difficult to read and write and prone to so-called shape errors, i.a., due to following inconsistent rules across a large, complex collection of operations. Alternatives like einsum and einops have gained popularity, but are inherently restricted to few operations and lack the generality required for a universal model of tensor programming.   To derive a better paradigm, we revisit vectorization as a function for transforming tensor operations, and use it to both lift lower-order operations to higher-order operations, and conceptually decompose higher-order operations to lower-order operations and their vectorization.   Building on the universal nature of vectorization, we introduce einx, a universal notation for tensor operations. It uses declarative, pointful expressions that are defined by analogy with loop notation and represent the vectorization of tensor operations. The notation reduces the large APIs of existing frameworks to a small set of elementary operations, applies consistent rules across all operations, and enables a clean, readable and writable representation in code. We provide an implementation of einx that is embedded in Python and integrates seamlessly with existing tensor frameworks: https://github.com/fferflo/einx

## Metadata
- **Published**: 2026-07-30T10:33:04Z
- **Authors**: Florian Fervers, Sebastian Bullinger, Christoph Bodensteiner, Michael Arens
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27987v1)