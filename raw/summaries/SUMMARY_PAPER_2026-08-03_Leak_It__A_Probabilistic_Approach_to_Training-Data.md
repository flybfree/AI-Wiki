---
title: Leak It: A Probabilistic Approach to Training-Data Extraction from Black-Box Language Models
url: http://arxiv.org/abs/2608.00144v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-07-31_15-44-43Z_LeakIt_AProbabilisticApproachtoTraining_DataExtrac.md
generated_at: 2026-08-03 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces “LeakIt”, a probabilistic framework to detect training‑data leakage in black‑box language models by treating sampled outputs as estimates of the underlying distribution and measuring leakage as functionals thereof. Experiments on WikiMIA, MIMIR, and Pythia‑6.9B show that aggregate ROC‑AUC hides per‑document disclosures, with identifier leaks rising from 5.6 % to 16.6 % as model capacity grows.

## Key Takeaways
- Blind bag‑of‑words classifiers achieve near‑perfect separation on WikiMIA (AUC 0.97) and add no information when sampling is used, indicating that leakage signals are not captured by aggregate metrics.  
- Per‑document extraction reveals that 83 of 500 Pile documents contain exact identifiers reproduced verbatim under mismatched‑prefix controls, proving that each leak originates from a single document rather than common strings.  
- The risk is uneven: identifier leakage in code (16.6 %) far exceeds prose (4.0 %), while arbitrary continuation recovery only occurs for code (+0.44 member gap).

## Context
Current privacy audits rely on aggregate ROC‑AUC scores that mask the true extent of data leakage, allowing models to inadvertently expose sensitive information without detection.

## Implications
For practitioners and researchers, reporting per‑document extraction decomposed by domain is essential; a single AUC can mislead about risk. The paper urges a shift toward granular privacy audits to protect both users and organizations from model‑driven data exposure.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00144v1)
