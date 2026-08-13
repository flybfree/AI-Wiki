---
title: Diagram-MMU: A Multi-Modal Benchmark for Scientific Diagrams
url: http://arxiv.org/abs/2608.12262v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_17-04-13Z_Diagram_MMU_AMulti_ModalBenchmarkforScientificDiag.md
generated_at: 2026-08-12 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Diagram-MMU, a multi‑modal benchmark that tests large language models’ ability to parse scientific diagrams into LaTeX TikZ code and answer diagram‑based questions. The evaluation of 12 MLLMs shows that tasks involving diagram-to-code generation are harder than question answering, while Claude‑4.6 Opus improves performance across all three tasks.

## Key Takeaways
- Diagram‑to‑code parsing is more challenging than diagram question answering because models can reason about diagrams but often fail to translate them into accurate LaTeX TikZ code.  
- Human validation of 18.3 k questions across six scientific domains ensures the benchmark covers a wide range of visual and textual complexities.  
- In agentic settings, most models see gains in parsing and editing but experience a drop in question‑answering performance.

## Context
The rapid growth of multimodal large language models has made them useful for scientific writing tools such as OpenAI Prism, which converts diagrams into LaTeX TikZ. Assessing these capabilities on a dedicated benchmark is essential to guide model development and tool design.

## Implications
For researchers, the results highlight a need for methods that specifically enhance diagram‑to‑code generation in MLLMs. Practitioners can leverage this benchmark to evaluate and improve scientific collaboration platforms, ensuring reliable integration of visual content into code.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12262v1)
