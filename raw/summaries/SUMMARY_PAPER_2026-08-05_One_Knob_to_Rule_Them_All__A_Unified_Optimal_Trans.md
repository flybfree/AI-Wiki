---
title: One Knob to Rule Them All: A Unified Optimal Transport View of Cold-Start Active Learning
url: http://arxiv.org/abs/2608.03249v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_07-21-39Z_OneKnobtoRuleThemAll_AUnifiedOptimalTransportViewo.md
generated_at: 2026-08-05 01:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a unified optimal transport framework for Cold-Start Active Learning, showing that existing selection heuristics share a common allocation structure and can be subsumed under this view. It introduces a task‑agnostic minimax bound controlled by entropic regularization and derives an adaptive rule that selects the regularization strength from unlabeled data. The resulting ε‑Adaptive Selection algorithm outperforms prior methods on ImageNet‑1k, boosting accuracy by 1.29% while cutting selection time by 56.2%.

## Key Takeaways
- The generalized transport selection framework reveals a shared allocation structure across existing CSAL methods and subsumes their specific formulations.
- Entropic regularization introduces a trade‑off that can be tuned adaptively to the unlabeled pool, yielding a task‑agnostic minimax bound for cold‑start selection.
- The ε‑Adaptive Selection algorithm uses Sinkhorn optimization to implement this adaptive rule, achieving state‑of‑the‑art performance on multiple datasets and annotation budgets.

## Context
Cold‑Start Active Learning struggles with the lack of labeled data or human guidance, limiting its applicability in real‑world scenarios where labeling is costly. This work addresses that gap by providing a principled, data‑driven approach that does not rely on arbitrary heuristics, aligning with broader efforts to make active learning more flexible and efficient.

## Implications
For practitioners, the ε‑Adaptive Selection algorithm offers a practical tool that reduces annotation effort while improving model performance, making large‑scale AI systems more scalable. The theoretical insights also guide future research toward adaptive regularization in unsupervised settings, potentially benefiting other domains such as few‑shot learning and continual adaptation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03249v1)
