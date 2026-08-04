---
title: A Fortran General-Purpose Transpiler: Proof of Concept
published: 2026-07-31T13:38:16Z
authors: Shivamshan Sivanesan, Kazem Ardaneh
url: http://arxiv.org/abs/2608.00130v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Fortran General-Purpose Transpiler: Proof of Concept

## Abstract
Fortran has been the cornerstone of high-performance computing for decades and remains unmatched in many domains. Yet the language faces an expertise gap: a new generation of scientists is barely familiar with it, while many experienced Fortran developers are only now transitioning to modern ecosystems such as JAX. This gap often results in "Fython"--Python code written with a Fortran mindset-- that fails to leverage modern frameworks. We present FGPT, a Python-based compiler framework designed to bridge this divide. It provides a systematic pipeline that transpiles Fortran into GPU-adapted Fortran, auto-differentiable Fortran via Tapenade, or NumPy and JAX modules. Its architecture comprises three stages: (i) a frontend that parses Fortran and extracts target procedures along with their cross-module dependencies; (ii) a middle-end that lowers the code into an intermediate representation, then into GPU-adapted or auto-differentiable Fortran, or a NumPy class; and (iii) a backend that rewrites control-flow and expressions to produce JAX modules ready for GPU acceleration and automatic differentiation. While large language models hold promise for small snippets, they fail at the scale of community scientific codes--often spanning hundreds of thousands of lines--where consistent transformations, strict numerical fidelity, and validation against production tests are non-negotiable. FGPT addresses these challenges by preserving program semantics throughout the entire translation. We verified the framework on representative climate modeling kernels and demonstrated that it produces correct, differentiable Python implementations without requiring manual intervention. By combining rigorous compiler techniques with modern accelerator support, FGPT offers a scalable, trustworthy path for modernizing legacy Fortran code.

## Metadata
- **Published**: 2026-07-31T13:38:16Z
- **Authors**: Shivamshan Sivanesan, Kazem Ardaneh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00130v1)