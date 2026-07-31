---
title: Improving the Robustness/Accuracy Tradeoff Against Adversarial Attacks Using Information Bottleneck Distillation Through Dual Teachers
url: http://arxiv.org/abs/2607.27737v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_06-20-37Z_ImprovingtheRobustness_AccuracyTradeoffAgainstAdve.md
generated_at: 2026-07-30 21:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper extends Information Bottleneck Distillation by adding a clean teacher model and using cross‑layer attention to transfer both clean and robust features to the student network. Experiments on CIFAR‑10 and CIFAR‑100 show that this approach improves classification accuracy on clean samples while keeping adversarial robustness comparable to the original IBD method.

## Key Takeaways
- The dual‑teacher framework transfers both clean and robust feature representations via cross‑layer attention, boosting clean classification accuracy without harming adversarial performance.  
- Experiments on CIFAR‑10/CIFAR‑100 demonstrate that the method outperforms the original IBD in clean accuracy while maintaining similar adversarial robustness.  
- The harmonic mean of clean and robust accuracies is competitive with B‑MTARD, indicating strong overall performance.

## Context
Deep neural networks are vulnerable to adversarial attacks, driving research on methods that balance robustness and accuracy. Information Bottleneck Distillation seeks this balance but often sacrifices clean performance. This work tackles the tradeoff by integrating a dedicated clean teacher into the distillation process.

## Implications
The dual‑teacher distillation method provides a practical way for practitioners to enhance model reliability across both clean and adversarial inputs, supporting deployment in safety‑critical applications where both accuracy and robustness matter. It also establishes a benchmark against B‑MTARD, encouraging further research on attention‑based feature transfer techniques.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27737v1)
