---
title: A Calibrated Test of Internal Action Maps: State Signals Without Global Affine Closure
url: http://arxiv.org/abs/2608.13626v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-13_05-41-24Z_ACalibratedTestofInternalActionMaps_StateSignalsWi.md
generated_at: 2026-08-16 22:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether action maps derived from hidden state signals can be calibrated without requiring global affine closure. It tests this hypothesis on a known affine S5 carrier and finds that most strong cells do not flip the closure gate, indicating bounded rather than universal calibration. The results show that frozen final-token h28 maps have higher error than within-test-domain cross-fit.

## Key Takeaways
- The evidence lattice shows held-source folds pass one-step gates but composition fails, revealing a geometric branch of action map fitting.
- Strongest cells flip closure gates only 23 out of 30, bounding calibration rather than universalizing it.
- Post-trained Qwen models show mean held-entity error .519 for h28 affine maps versus .398 within-test-domain cross-fit.

## Context
This work extends the study of internal action maps in large language models beyond typical global closure assumptions. It highlights that state signals can be usable locally without supporting reusable action maps, a nuance relevant to model interpretability and debugging.

## Implications
For practitioners, these findings suggest focusing on local geometry and held-entity calibration rather than assuming universal action map reuse. The separation of state availability, causal use, and algebraic closure informs future research into modular model design and fine-tuning strategies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13626v1)
