---
title: Inter-Residue Geometry Attention for Antibody-Specific Epitope Prediction
published: 2026-08-02T08:48:07Z
authors: Chuanliu Fan, Nan Yu, Junjie Wu, Guohong Fu
url: http://arxiv.org/abs/2608.01092v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Inter-Residue Geometry Attention for Antibody-Specific Epitope Prediction

## Abstract
Antibody-specific epitope prediction aims to identify which antigen residues are recognized by a given antibody, a task that depends on the three-dimensional complementarity between antibody CDRs and the antigen surface. Existing methods usually leverage PLM embeddings and inject structure through additional graph, surface, or point-cloud encoders, where the positional mechanism inside attention remains largely tied to one-dimensional sequence order. For proteins, the analogue of a token offset is not only sequence separation, but also the three-dimensional displacement between residues after folding. This raises a question, can folded residue geometry serve as the positional mechanism of attention itself? We propose Local-Frame 3D Rotary Position Encoding (LF3DRoPE), which expresses inter-residue displacements in backbone-defined local frames and injects them directly into rotary attention. This design preserves continuous directional geometry while ensuring invariance to global $\mathrm{SE}(3)$ transformations. On the AsEP benchmark, LF3DRoPE achieves state-of-the-art $\mathrm{MCC}$ on both ratio and epitope-group splits. Ablations and rigid transformation tests show that local three-dimensional geometry provides information beyond sequence-order attention while preserving invariance to arbitrary global coordinate systems. Mutation ranking results further indicate that LF3DRoPE captures antigen-specific structural compatibility.

## Metadata
- **Published**: 2026-08-02T08:48:07Z
- **Authors**: Chuanliu Fan, Nan Yu, Junjie Wu, Guohong Fu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01092v1)