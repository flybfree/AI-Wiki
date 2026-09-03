---
title: PaperCompiler: Faithful Paper-to-Code Generation via Repository-Level Specification Compilation
published: 2026-09-02T08:21:03Z
authors: Yunhao Liu, Hong Phuc Pham, Jaehong Yoon
url: http://arxiv.org/abs/2609.02272v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PaperCompiler: Faithful Paper-to-Code Generation via Repository-Level Specification Compilation

## Abstract
Faithfully translating research papers into repository-level implementations remains challenging because papers often describe methods at a high level, leave implementation assumptions implicit, and require generated repositories to preserve method logic, evaluation protocols, and cross-file consistency. Despite recent advances in paper-to-code agents, their intermediate outputs are often presented as free-form plans or summaries that downstream coding agents may ignore, reinterpret, or compress, leading to algorithmic simplification and inconsistent repository structure. To address these challenges, we introduce PaperCompiler, a paper-to-code generation framework that compiles paper-grounded evidence into explicit repository-level implementation specifications. PaperCompiler grounds implementation-relevant evidence while preserving source provenance and distinguishing paper-supported, inferred, externally delegated, and unresolved information. The resulting specifications encode non-degradation requirements, ownership assignments, cross-file dependencies, and file-level constraints. Repository generation proceeds under these compiled specifications while retaining flexibility over local engineering choices not fixed by the paper. PaperCompiler outperforms strong baselines on Paper2CodeBench, achieving a 13.8% relative improvement in reference-based fidelity (from 3.64 to 4.15) and reducing high-severity evaluator critiques (from 13.2% to 6.1%).

## Metadata
- **Published**: 2026-09-02T08:21:03Z
- **Authors**: Yunhao Liu, Hong Phuc Pham, Jaehong Yoon
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02272v1)