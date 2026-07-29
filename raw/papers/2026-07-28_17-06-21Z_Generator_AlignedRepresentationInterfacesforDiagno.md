---
title: Generator-Aligned Representation Interfaces for Diagnostic Soft Equivariance
published: 2026-07-28T17:06:21Z
authors: Weitao Li, Gong Cheng
url: http://arxiv.org/abs/2607.25988v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Generator-Aligned Representation Interfaces for Diagnostic Soft Equivariance

## Abstract
Exact-equivariant architectures typically encode prescribed group actions in specialized operators, which can complicate their reuse with generic backbones and across data modalities. We introduce the Generator-Aligned Representation Interface (GARI), a representation-level design principle that exposes selected transformation generators to a generic sequence backbone through aligned canonical and generator-induced views. We formalize the resulting behavior using a probe-specific soft-equivariance residual defined over declared data and transformation distributions. This framework distinguishes representation consistency from task robustness and exact equivariance, and localizes residual mismatch to interface construction, shared stream processing, and terminal fusion. We instantiate the interface as GARI-Net, which constructs generator-indexed streams, converts them into a common interaction frame, processes them with shared parameters, repairs ordering-induced context mismatch, enables cross-stream information exchange, and aggregates them using inter-stream discrepancy. Direct Equivariance Error (DEE) provides a frozen-checkpoint diagnostic of the prescribed representation relation under known token or voxel actions. Experiments on genomic sequences, images, and three-dimensional point clouds examine sequence reversal, planar rotations and reflections, and controlled axial transfer. Across these settings, the same interface principle supports task-relevant transformation consistency and generalization to declared held-out probes without requiring group-specific redesign of the sequence backbone. GARI therefore provides a portable diagnostic complement to hard-equivariant architectures: it makes generator structure accessible, learnable, and measurable, while finite-probe evidence remains distinct from certification of exact equivariance over a continuous group.

## Metadata
- **Published**: 2026-07-28T17:06:21Z
- **Authors**: Weitao Li, Gong Cheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25988v1)