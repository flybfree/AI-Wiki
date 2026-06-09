# Summary: 2026-05-06_16-20-24Z_OrderMatters_ImprovingDomainAdaptationbyReordering.md
Saved: 2026-05-07 22:08
Source: 2026-05-06_16-20-24Z_OrderMatters_ImprovingDomainAdaptationbyReordering.md
Model: None

---

## Summary
ORDERED proposes improving unsupervised domain adaptation by changing the order in which training samples are processed. The paper treats discrepancy estimation as a stochastic variance problem and uses reordering to reduce estimation error for alignment losses.

## Key Takeaways
- Introduces Optimal Reordering of Data for Error-Reduced Estimation of Discrepancy (ORDERED).
- Focuses on correlation alignment and maximum mean discrepancy.
- Uses an unbiased stochastic variance reduction approach.
- Reports reduced variance in simulation and improved target accuracy on image classification benchmarks.

## Context
The method addresses instability in discrepancy estimates that can limit the practical value of UDA. Instead of altering the model architecture, it optimizes the sampling order of training data.

## Implications
This suggests that training dynamics and data ordering can materially affect adaptation quality. The idea may be useful wherever stochastic alignment objectives suffer from high variance.

## Original Reference
- Title: Order Matters: Improving Domain Adaptation by Reordering Data
- Authors: Andrea Napoli, Paul White
- URL: http://arxiv.org/abs/2605.05084v1
- Published: 2026-05-06T16:20:24Z