---
title: Code as Representation: A Compilable Parsing Paradigm for Academic Documents
url: http://arxiv.org/abs/2608.17550v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_09-10-43Z_CodeasRepresentation_ACompilableParsingParadigmfor.md
generated_at: 2026-08-18 21:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Compilable Academic Document Parsing (CADP), a framework that converts an entire academic page into LaTeX plus executable Python code, preserving the structure of tables, formulas, charts, and pseudocode. Experiments on CADP‑Bench show that even state‑of‑the‑art multimodal models produce low‑fidelity reconstructions, indicating significant challenges in faithful representation.

## Key Takeaways
- CADP reconstructs a full page as LaTeX plus Python, enabling structural fidelity and direct verification against the source.
- The benchmark CADP‑Bench contains expert‑verified pages with tightly coupled text and multiple SAE types, evaluated via re‑injection compilation.
- Current MLLMs still struggle to generate high‑fidelity executable reconstructions, highlighting a gap in structure‑aware parsing.

## Context
Academic documents are richly multimodal yet poorly understood by AI systems that rely on simple text conversion. This work addresses the need for a representation that can capture both visual and logical structures of scientific pages, aligning with trends toward code‑generating models and verifiable outputs.

## Implications
For researchers, CADP provides a testbed to evaluate parsing robustness across diverse SAE types. For industry, it could enable automated extraction and validation of data from research papers, improving reproducibility and downstream AI pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17550v1)
