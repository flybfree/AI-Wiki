---
title: Don't Stop Long-Context Continual Pre-Training Too Early: An Empirical Scaling Law
url: http://arxiv.org/abs/2610.29352v1
type: paper-summary
date: 2026-10-21
source_paper: 2026-10-21_07-46-55Z_Don_tStopLong_ContextContinualPre_TrainingTooEarly.md
generated_at: 2026-10-21 21:08
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates how the benefits of long-context continual pre-training (LCCP) scale with the number of training tokens used, establishing an empirical additive power law that relates long-context performance to model size and token budgets for both short-context pre-training and LCCP. Through experiments spanning five model scales and over one hundred budget configurations, the authors demonstrate that LCCP gains remain stably observable, quantitatively predictable, and transferable to downstream tasks, arguing strongly against stopping LCCP training prematurely.

## Key Takeaways
- The authors establish an empirical additive power law connecting long-context performance to model size and the respective token budgets of short-context pre-training and LCCP. Experiments across five model scales and more than one hundred short- and long-context budget configurations confirm that the fitted law reproduces observed trends and extrapolates well to held-out model scales, providing a practical tool for predicting LCCP outcomes before committing compute.
- A novel training and observation protocol called Constant-Last4 is introduced, which averages the four most recent consecutive checkpoints from a constant-learning-rate run to enable stable monitoring along a single extensible training trajectory. Under this protocol, the same scaling-law form fits well and accurately predicts the LCCP performance trajectory of a 1.22B-parameter model trained on approximately 100B LCCP tokens, offering a reproducible methodology for tracking long-context capability gains over time.
- Downstream evaluations along the training trajectory show continued improvements in long-context performance with no clear sign of saturation within the evaluated range. These gains persist after both 128K context extension and supervised fine-tuning, with benefits extending to long-context understanding and agentic tasks, indicating that LCCP improvements are not merely superficial but transfer meaningfully to practical applications.

## Context
Long-context capability has become a critical requirement for modern large language models, as applications in retrieval-augmented generation, code understanding, and agentic reasoning increasingly demand models that can process and reason over very long sequences. While LCCP is widely adopted as a technique to extend context windows, the field has lacked rigorous quantitative understanding of how performance scales with training token budgets, leading practitioners to make ad-hoc decisions about when to stop training. This paper fills that gap by providing a validated scaling law and a monitoring protocol that make LCCP outcomes predictable and measurable.

## Implications
For practitioners and organizations investing in long-context model development, this work provides actionable guidance: scaling LCCP token budgets yields stably observable and quantitatively predictable gains that transfer to downstream tasks including agentic workflows, suggesting that early stopping of LCCP may leave significant performance on the table. The Constant-Last4 protocol and the fitted scaling law together offer a practical framework for planning compute budgets and setting training schedules, potentially reducing wasted compute and enabling more confident deployment decisions across model scales.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.29352v1)
