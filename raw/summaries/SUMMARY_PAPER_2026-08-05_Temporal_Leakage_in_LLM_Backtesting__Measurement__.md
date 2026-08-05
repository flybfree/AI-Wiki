---
title: Temporal Leakage in LLM Backtesting: Measurement, Validation, and Adjusted Scores
url: http://arxiv.org/abs/2608.02985v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_00-45-54Z_TemporalLeakageinLLMBacktesting_Measurement_Valida.md
generated_at: 2026-08-05 01:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper demonstrates that the conventional leakage check — comparing scores before and after a training cutoff — is uninformative because four leading models legitimately know more about questions near their cutoffs, causing recency to masquerade as contamination. It introduces two external references: a known cutoff and a matched clean control, enabling measurement rather than mere detection of leakage. The authors also show that leakage concentrates on outcomes that surprised the crowd yet were well covered in training, rewarding partial memorization disproportionately.

## Key Takeaways
- Standard before‑after comparisons cannot distinguish genuine skill from recency effects; four flagged models actually possess legitimate knowledge near their cutoffs.
- Leakage is most pronounced for surprising questions that were well represented in the training data, leading to over‑rewarding of partial memorization.
- The proposed estimators recover injected leakage doses and return null scores on clean questions; when applied to frontier models they detect a cutoff‑localized signature and clear five models whose advantages were recency alone.

## Context
In AI research, backtesting LLM performance is common practice but often inflates scores due to contamination from future knowledge. This work addresses a methodological flaw that undermines the reliability of such evaluations, highlighting the need for external validation beyond simple temporal splits.

## Implications
For practitioners and researchers, this paper provides a defensible reference point for assessing model competence, encouraging rigorous external checks to ensure backtest results reflect true skill rather than recency or partial memorization.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02985v1)
