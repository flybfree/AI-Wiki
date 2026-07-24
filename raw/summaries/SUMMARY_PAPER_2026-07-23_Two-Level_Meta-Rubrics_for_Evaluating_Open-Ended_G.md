---
title: Two-Level Meta-Rubrics for Evaluating Open-Ended Generation: GAMUT, a Benchmark for Factual Completeness
url: http://arxiv.org/abs/2607.19322v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_17-42-50Z_Two_LevelMeta_RubricsforEvaluatingOpen_EndedGenera.md
generated_at: 2026-07-23 23:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a two‑level meta‑rubric framework called Gamut to evaluate factual completeness in long‑form generation, addressing the “missing half” of factuality that precision metrics ignore. The benchmark demonstrates that even frontier models achieve only about 58.7% correct coverage, highlighting the difficulty of fully capturing required information.

## Key Takeaways
- The dominant precision‑focused evaluation misses the missing half of factuality, i.e., whether a response contains all the information it should.
- A two‑level meta‑rubric captures the organization and importance of required content, then mechanically compiles it into a flat checklist that LLM judges can score reliably.
- Gamut’s benchmark with 1,813 questions across ten domains yields challenging results, with the best model scoring 58.7% from Gemini 3.1 Pro.

## Context
Long‑form generation evaluation has traditionally centered on precision, which measures whether claims are correct but not whether they are complete. This work expands the field by tackling factual completeness, a problem that involves open‑ended sets of facts and relationships rather than simple boolean checks.

## Implications
Accurate completeness metrics are essential for reliable long‑form outputs in domains such as medical reports, legal briefs, and educational content. The Gamut benchmark provides a standardized tool that can guide model development and help practitioners move beyond superficial precision to holistic factual coverage.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19322v1)
