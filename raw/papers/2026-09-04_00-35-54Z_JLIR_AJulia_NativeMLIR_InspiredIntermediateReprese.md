---
title: JLIR: A Julia-Native MLIR-Inspired Intermediate Representation with Automatic JACC Kernel Extraction
published: 2026-09-04T00:35:54Z
authors: Narasinga Rao Miniskar, Seyong Lee, Keita Teranishi, Jeffrey S Vetter
url: http://arxiv.org/abs/2609.04585v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# JLIR: A Julia-Native MLIR-Inspired Intermediate Representation with Automatic JACC Kernel Extraction

## Abstract
The Multi-Level Intermediate Representation (MLIR) has made reusable compiler infrastructure practical for domain-specific computation. However, MLIR's strong compile-time type requirements and low-level (C++) extension model can be a poor match for high-level, dynamically specialized languages such as Julia. MLIR has several drawbacks for dynamic programming languages in terms of the type system and level of abstraction. It is thus extremely challenging for non-compiler or scientific computing users to introduce new programming abstractions and express algorithm implementations in a form that remains both natural and optimizable. As a result, library interfaces for linear algebra, mesh processing, partial differential equations, and related domains often sit outside the compiler optimization path. We present JLIR (Julia-native Level Intermediate Representation), a Julia-native intermediate representation framework that brings the main benefits of MLIR-style multi-level, dialect-oriented compilation into the Julia ecosystem while remaining usable as ordinary Julia code. JLIR represents Julia programs before low-level lowering, supports extensible operations and transformation passes through Julia's language mechanisms, and allows partially typed programs to remain transformable until concrete types are known. The framework includes built-in dialects for arithmetic, control flow, functions, structured loops, and memory operations, and it also includes a lightweight mechanism for adding new domain operations without modifying the core system. To demonstrate JLIR's capabilities, we applied it to automatic Julia for Accelerators (JACC) kernel generation.

## Metadata
- **Published**: 2026-09-04T00:35:54Z
- **Authors**: Narasinga Rao Miniskar, Seyong Lee, Keita Teranishi, Jeffrey S Vetter
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04585v1)