---
title: "Summary: Language-Critique Imitation Learning from Suboptimal Demonstrations"
url: http://arxiv.org/abs/2607.01225v1
type: paper-summary
date: 2026-07-01
source_paper: 2026-07-01_17-57-22Z_Language_CritiqueImitationLearningfromSuboptimalDe.md
generated_at: 2026-07-01 23:00
model: nvidia/nemotron-3-nano-4b
---
# Summary: 2026-07-01 Language-Critique Imitation Learning From Suboptim

## Summary
The paper introduces a language-critique framework that uses natural language labels from suboptimal demonstrations to train imitation learning policies without collapsing feedback into scalar scores. It proposes loss functions LC-BC for behavior cloning and LC-DP for diffusion policies, showing they upper-bound the expert performance gap. Experiments on navigation, manipulation, and gameplay tasks demonstrate consistent superiority over baselines.

## Key Takeaways
- The method replaces compressed supervision signals with structured natural language labels that capture progress, errors, and corrective guidance.
- The language-critique loss directly optimizes policies using these textual cues instead of reducing them to scalars like confidence or importance weights.
- Theoretical analysis proves the objective bounds the expert performance gap under standard assumptions.

## Context
Imitation learning from suboptimal demonstrations remains challenging because traditional scalar supervision lacks expressive power. This work addresses the limitation by leveraging language as a richer, structured signal that can encode intermediate reasoning and corrective actions.

## Implications
For practitioners, this approach enables more reliable policy generation from imperfect data without additional calibration. It opens avenues for integrating human-like feedback into automated learning pipelines, potentially improving robustness in safety-critical applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.01225v1)
