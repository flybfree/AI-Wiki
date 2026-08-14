---
title: TRAPSBench: Vision-Language Models Encode but Fail to Express Epistemic Restraint
url: http://arxiv.org/abs/2608.13167v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_12-32-13Z_TRAPSBench_Vision_LanguageModelsEncodebutFailtoExp.md
generated_at: 2026-08-13 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces TRAPSBench, a benchmark of video pairs where visual evidence makes an outcome undeterminable due to a single targeted change. It also proposes the Penalized Epistemic Calibration Score (PECS) to measure whether models correctly abstain when needed. Across 16 vision‑language models, spontaneous restraint is poor, with the best PECS reaching only 0.292.

## Key Takeaways
- Models can internally detect when an answer should be withheld but do not output that restraint, indicating a gap between perception and expression.  
- Linear probes show high AUROC (up to 0.91) decoding answerability from hidden states, proving the issue lies in representation rather than detection.  
- The failure is more severe for visual uncertainty than textual impossibility, with models detecting missing visual evidence four times less readily.

## Context
Vision‑language models are expected to understand when information is insufficient and respond appropriately. This study reveals that current systems lack a reliable mechanism to communicate epistemic restraint, highlighting a limitation in their reasoning pipeline.

## Implications
For developers, closing the representation–output gap may require interventions at the output stage rather than solely improving perception. Practitioners should consider designing evaluation metrics like PECS and building models that can explicitly signal uncertainty to align with user expectations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13167v1)
