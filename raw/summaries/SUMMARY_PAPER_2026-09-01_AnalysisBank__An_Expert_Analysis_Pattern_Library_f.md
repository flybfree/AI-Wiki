---
title: AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation
url: http://arxiv.org/abs/2609.00818v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_07-18-06Z_AnalysisBank_AnExpertAnalysisPatternLibraryforFina.md
generated_at: 2026-09-01 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes AnalysisBank, a library that extracts analytical moves from expert financial reports and uses them to generate new reports based on data signals rather than structural templates. Experiments show it boosts novel data‑grounded insights by up to three times compared with baseline LLM methods.

## Key Takeaways
- The library captures 47–52 distinct signal types across 13 analytical moves, showing a heavy‑tailed distribution of expert content.
- On two financial benchmarks and four LLMs, AnalysisBank raises the proportion of novel insights by 1.7–3.7× over structural‑level baselines.
- The approach distills reports into reusable Analyses that pair signals, moves, and source spans for inference.

## Context
This work addresses a limitation in current AI report generation where models rely on fixed templates, limiting creativity and relevance to data. By shifting focus to analytical patterns, the study demonstrates how domain‑specific insights can be encoded as reusable modules.

## Implications
For finance, this could automate more accurate earnings calls and risk assessments. The methodology may extend to scientific writing, offering a scalable way to embed expert reasoning into generative AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00818v1)
