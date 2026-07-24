---
title: Spaghetti Architect: A Contamination-Resistant, By-Construction-Labelled, Multi-Language Code Dataset Generator
url: http://arxiv.org/abs/2607.18642v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_02-23-22Z_SpaghettiArchitect_AContamination_Resistant_By_Con.md
generated_at: 2026-07-23 23:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
Spaghetti Architect generates code datasets with controlled messiness and difficulty labels by mapping clean JSON to redundant flattened programs in five languages. Each program is compiled against a reference oracle, guaranteeing correctness by construction. The approach also demonstrates that refactoring equivalence is preserved across languages.

## Key Takeaways
- Each generated program is correct by construction because it is compiled against a reference oracle.
- Difficulty is dialed via nested anti-pattern profiles labeled on two orthogonal axes: intrinsic problem size and incidental presentation complexity.
- The generator's self‑annotations improve the weakest model more than the strongest, indicating annotation quality matters.

## Context
AI research struggles with uncontrolled code corpora where semantics and difficulty are unmeasured. This work provides a benchmark that aligns generated data with human‑rated metrics, offering a reliable standard for evaluating model performance.

## Implications
Practitioners can rely on reproducible, contamination‑free datasets for training models, reducing overfitting to existing samples and enabling fair model comparison across scales.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18642v1)
