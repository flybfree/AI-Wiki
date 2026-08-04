---
title: CADIR: A Cross-Backend Editable Intermediate Representation for Agentic CAD Generation
published: 2026-08-01T23:07:08Z
authors: Yu Liu, Jingzhe Ni, Yiming Chen, Junqi Huang, Ruofeng Tong, Min Tang, Peng Du
url: http://arxiv.org/abs/2608.00891v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CADIR: A Cross-Backend Editable Intermediate Representation for Agentic CAD Generation

## Abstract
Large language models have made it possible to generate executable computer-aided design (CAD) programs from natural-language descriptions or images. However, existing methods represent modeling processes as backend-specific sequential scripts with implicit dependencies or as static geometry, making it difficult to simultaneously preserve construction history, stable topological references, and feature-level editability across different CAD systems. We present CADIR, an agent-friendly executable intermediate representation for CAD generation and cross-backend editing. Built on the OCCT geometry kernel via OCP, CADIR provides explicit, compositional modeling operations and fine-grained execution diagnostics. During program execution, CADIR records modeling operations, parameter dependencies, constraints, and topology selections in a construction graph. To enable reliable cross-backend reconstruction, we introduce Geometric Signature Matching, which identifies corresponding edges and faces despite parameter changes and backend differences, allowing adapters to reconstruct native editable feature histories in FreeCAD, SolidWorks, and Fusion 360. Building on this representation, we further propose a construction-graph retrieval method for text and image queries that supports both full-graph and subgraph retrieval, enabling agents to leverage complete models and modeling substructures. Extensive experiments demonstrate that CADIR achieves higher geometric fidelity and execution reliability than existing CAD representations, that construction-graph retrieval further improves model generation quality, and that cross-backend editing enables reliable model reconstruction and post-reconstruction editing across multiple CAD environments.

## Metadata
- **Published**: 2026-08-01T23:07:08Z
- **Authors**: Yu Liu, Jingzhe Ni, Yiming Chen, Junqi Huang, Ruofeng Tong, Min Tang, Peng Du
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00891v1)