---
title: Compile by Training: Turning Natural-Language Specifications into Local Neural Functions
url: http://arxiv.org/abs/2609.04199v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_17-59-49Z_CompilebyTraining_TurningNatural_LanguageSpecifica.md
generated_at: 2026-09-03 22:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces “compile by training,” a method that converts natural‑language specifications into reusable neural functions without relying on remote models or complex rule engines. By generating task examples at compile time and training small adapters, the system achieves high semantic accuracy while avoiding latency and dependency issues. On FuzzyBench‑Hard it reaches 83.6 % accuracy, a significant improvement over a fast compiler that produced no matches.

## Key Takeaways
- The approach replaces rule‑based implementations with lightweight neural functions trained from teacher‑generated examples, enabling versioned storage and composition like ordinary software.
- Compile time is slower (about a minute) than the fast program‑as‑weights compiler, but this trade‑off yields higher semantic accuracy on challenging benchmarks.
- Deployed functions include interactive website helpers, language‑controlled 3D avatars, and bidirectional English‑Claudish translation services.

## Context
Current AI systems often require constant calls to large external models, creating latency and vendor lock‑in. This paper offers a local alternative that can be pre‑compiled into compact neural modules, aligning with trends toward on‑device inference and modular software engineering.

## Implications
For developers, the method reduces operational costs by eliminating remote API usage while preserving high performance. Enterprises can adopt compiled functions as standard components in AI pipelines, fostering interoperability across platforms and improving system reliability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04199v1)
