---
title: GPTQ-2D: Cubic-Time Two-Sided Adaptive Rounding
published: 2026-07-29T15:34:00Z
authors: Jiale Chen, Torsten Hoefler, Dan Alistarh
url: http://arxiv.org/abs/2607.27042v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GPTQ-2D: Cubic-Time Two-Sided Adaptive Rounding

## Abstract
Adaptive rounding methods such as GPTQ, or equivalently Babai's nearest plane algorithm, round a real matrix to integers under a quadratic metric. They process the entries in a fixed order, one at a time, propagating each rounding error to the entries not yet processed through a triangular feedback matrix. We study the two-sided version of this task, in which fixed nonsingular basis matrices act on both the left and the right of the residual; the familiar one-sided case is the special case of an identity right basis. Vectorizing the matrix turns the two-sided objective into a quadratic metric whose Gram matrix is a Kronecker product, so the one-dimensional algorithm applies verbatim, but takes quartic time in the matrix dimension. We present GPTQ-2D, which produces the identical rounded matrix in cubic time. It rounds the entries anti-diagonal by anti-diagonal; entries on the same anti-diagonal are independent and are rounded in parallel.

## Metadata
- **Published**: 2026-07-29T15:34:00Z
- **Authors**: Jiale Chen, Torsten Hoefler, Dan Alistarh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27042v1)