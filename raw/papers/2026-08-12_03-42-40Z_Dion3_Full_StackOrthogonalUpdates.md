---
title: Dion3: Full-Stack Orthogonal Updates
published: 2026-08-12T03:42:40Z
authors: Noah Amsel, Jack Zhang, Kwangjun Ahn, Ali Naeimi, Austin Feng, Berlin Chen, Tri Dao, John Langford
url: http://arxiv.org/abs/2608.11612v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dion3: Full-Stack Orthogonal Updates

## Abstract
The Muon optimizer incurs a significant overhead cost due to its cubic-time Newton-Schulz orthogonalization step. When weights are sharded, communication overhead compounds this computational cost, eroding the benefits of Muon in many settings. We present Dion3, a revision of Muon that targets this overhead at every level of the stack. Our Gram Newton-Schulz algorithm reduces the FLOP cost of orthogonalization, our CuteDSL kernels accelerate it by exploiting symmetry, and our megabatching strategy reduces communication overhead. Moreover, we propose a simple change to the update rule that cuts costs even further: selecting only a fraction of the momentum matrix's rows to orthogonalize at each step. This update rule improves on Dion (another "compressed" version of Muon), in both speed and performance. Overall, Dion3 matches or improves on the loss achieved by Muon but reduces optimizer step time by up to 6x. Dion3 is available via the dion package (https://github.com/microsoft/dion) as a drop-in replacement for Muon.

## Metadata
- **Published**: 2026-08-12T03:42:40Z
- **Authors**: Noah Amsel, Jack Zhang, Kwangjun Ahn, Ali Naeimi, Austin Feng, Berlin Chen, Tri Dao, John Langford
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11612v1)