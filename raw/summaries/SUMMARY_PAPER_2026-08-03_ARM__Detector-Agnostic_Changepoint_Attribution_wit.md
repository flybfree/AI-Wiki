---
title: ARM: Detector-Agnostic Changepoint Attribution with Finite-Sample Error Control
url: http://arxiv.org/abs/2608.01691v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_04-42-28Z_ARM_Detector_AgnosticChangepointAttributionwithFin.md
generated_at: 2026-08-03 23:32
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ARM, a detector‑agnostic changepoint attribution method that certifies which variables changed after a changepoint is detected by any arbitrary detector. It provides finite‑sample error guarantees across coordinates and demonstrates performance on financial data.

## Key Takeaways
- ARM scores each coordinate using a max‑over‑splits rank statistic, guaranteeing per‑coordinate validity regardless of the chosen detector.
- The method controls exact family‑wise error via a Westfall–Young joint permutation that respects cross‑coordinate dependence and offers a distribution‑free Holm fallback.
- It also achieves false discovery rate control under arbitrary coordinate dependence in high dimensions using Benjamini–Yekutieli and e‑BH.

## Context
Detecting changepoints is essential for monitoring multivariate time series, yet current approaches either ignore which variables changed or lack rigorous error bounds. This work bridges that gap by offering a principled statistical framework applicable to any detector.

## Implications
Researchers can trust attribution results in high‑dimensional settings without sacrificing power. Practitioners benefit from reliable change detection in finance and other domains where false alarms are costly.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01691v1)
