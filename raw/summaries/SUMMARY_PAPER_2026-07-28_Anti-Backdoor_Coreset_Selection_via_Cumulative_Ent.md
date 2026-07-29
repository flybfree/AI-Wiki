---
title: Anti-Backdoor Coreset Selection via Cumulative Entropy
url: http://arxiv.org/abs/2607.25502v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_09-37-11Z_Anti_BackdoorCoresetSelectionviaCumulativeEntropy.md
generated_at: 2026-07-28 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes Anti‑Backdoor Coreset Selection using cumulative entropy to build a training‑time defense that isolates benign samples and removes poisonous ones. By measuring the learning dynamics of samples, it selects high‑informativeness benign data while discarding low‑uncertainty backdoor examples. The resulting coreset trains a model with minimal impact on natural accuracy.

## Key Takeaways
- Poisonous samples exhibit lower prediction uncertainty and are less frequent than benign ones, so cumulative entropy naturally biases selection toward benign data.
- The metric tracks learning dynamics to identify high‑informativeness benign samples for inclusion in the coreset.
- Unlearning of selected samples each epoch maintains separability between benign and poisonous examples.

## Context
Training‑time defenses aim to prevent adversarial poisoning by focusing on clean data. Coresets are used to reduce dataset size while preserving representativeness, but prior methods often degrade natural performance or fail against targeted attacks. This work introduces a principled entropy metric to improve selection accuracy.

## Implications
For practitioners, the method offers a lightweight way to detect and neutralize backdoors without retraining large models. It supports robust model deployment where clean training data is scarce, encouraging adoption of defense‑aware pipelines in AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25502v1)
