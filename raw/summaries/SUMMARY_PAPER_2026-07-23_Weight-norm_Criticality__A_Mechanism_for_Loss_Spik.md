---
title: Weight-norm Criticality: A Mechanism for Loss Spikes Induced by the Normalization and Weight Decay
url: http://arxiv.org/abs/2607.21005v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_07-39-03Z_Weight_normCriticality_AMechanismforLossSpikesIndu.md
generated_at: 2026-07-23 23:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces weight‑norm criticality as a mechanism that explains loss spikes during deep network training. It shows how the interaction between normalization and weight decay drives scale‑invariant weights toward zero, increasing landscape sharpness and causing abrupt loss increases when decay becomes too strong.

## Key Takeaways
- As the weight‑decay coefficient rises, the norms of scale‑invariant parameters shrink, eventually crossing a critical threshold that destabilizes optimization.  
- The resulting increase in loss‑landscape sharpness triggers sudden spikes rather than gradual degradation.  
- This mechanism offers a testable boundary beyond which excessive decay harms training despite its usual benefit for generalization.

## Context
Training instability has long been attributed to learning‑rate criticality, but practical deep models also contain components that are invariant to scaling. The proposed weight‑norm criticality explains why strong regularization can backfire when combined with such invariances, a phenomenon not captured by standard stability analyses.

## Implications
Practitioners should monitor weight‑decay levels relative to the presence of scale‑invariant layers to avoid crossing this critical point. Understanding this boundary could lead to more robust training protocols and better generalization without sacrificing regularization strength.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21005v1)
