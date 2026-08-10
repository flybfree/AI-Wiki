---
title: Zero Gap Is Not Restoration: Stratified Per-Question Probability Evaluation and Step-wise Mitigation of Benchmark Contamination
url: http://arxiv.org/abs/2608.07341v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_15-37-03Z_ZeroGapIsNotRestoration_StratifiedPer_QuestionProb.md
generated_at: 2026-08-09 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper tackles contamination in benchmark evaluation by proposing SA‑PPG to measure per‑question probability gaps and demonstrating that prior restoration methods overestimate their effectiveness while RailCap achieves the lowest gap. It introduces a stratified aggregation of solve probabilities and a generation‑based mitigation strategy that caps greedy tokens when contamination is detected.

## Key Takeaways  
- Discrete correct/incorrect readouts cannot capture per‑question performance because averaging before differencing masks over‑ and under‑suppression, leading to inaccurate restoration estimates.  
- Uniform weighting encourages strategies to push solve probabilities onto the clean model’s high‑frequency values, which undermines true restoration of genuine capability.  
- RailCap caps greedy tokens when contamination is detected during generation, resulting in a lower SA‑PPG compared with other methods.

## Context  
Benchmark contamination inflates pretraining scores by leaking test data into training corpora, causing models to memorize answers rather than learn them. Traditional mitigation evaluation relies on coarse readouts and uniform weighting, which fails to reflect the nuanced degradation across individual questions.

## Implications  
Practitioners must adopt finer granularity in evaluation to avoid overstating model improvement, as current approaches often inflate performance metrics. The study underscores the need for strategies that operate directly during generation rather than relying solely on post‑hoc probability estimates.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07341v1)
