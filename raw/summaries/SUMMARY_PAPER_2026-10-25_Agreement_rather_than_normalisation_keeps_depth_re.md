---
title: Agreement rather than normalisation keeps depth reusable in looped language models
url: http://arxiv.org/abs/2610.31943v1
type: paper-summary
date: 2026-10-25
source_paper: 2026-10-22_21-42-16Z_Agreementratherthannormalisationkeepsdepthreusable.md
generated_at: 2026-10-25 21:53
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether the depth reusability of looped language models—models that apply a single block of layers repeatedly—depends on normalizing the hidden state between loop iterations (as the released Ouro models do) or on agreement between the training loop configuration and the inference loop configuration. Through experiments on released Ouro weights and models trained from scratch, the authors demonstrate that removing loop-boundary normalization causes catastrophic failure in pretrained models but is never harmful in models trained without it, and that extrapolation beyond the trained depth is actually better without normalization. The core finding is that agreement between training and inference loop structure, rather than the normalization operation itself, is what preserves depth reusability.

## Key Takeaways
- Removing loop-boundary normalization from released Ouro-1.4B and Ouro-2.6B weights drops accuracy to zero on a balanced binary task by the trained budget, yet the failure mechanism is not state-norm growth as prior accounts predict: the norm remains within a factor of 2.021 while the model head commits to a single wrong token. The damage is localized to the readout path and the last layer of the repeated block, not to a global state explosion.
- In 19M-parameter models trained from scratch across 16 seeds per configuration on two synthetic tasks, training without normalization is never worse than training with it and extrapolates better beyond the trained depth, with Cliff's delta reaching up to 0.867. The two configurations are closest at the trained depth and diverge on both sides, strongly supporting the agreement hypothesis over the normalization hypothesis.
- Refitting experiments reveal the structural locus of damage: refitting only the head over a frozen modified loop recovers roughly one-third of lost accuracy and plateaus, while refitting the last block layer together with the head recovers all of it. Additionally, comparisons between looped and stacked depth at equal inference loop counts are confounded by unequal overshoot of the trained budget; at matched overshoot, the apparent advantage of looping vanishes on one task and shrinks on the other.

## Context
Looped language models represent a parameter-efficient architecture where a single transformer block is applied multiple times, offering a path to scaling effective depth without scaling parameter count. The Ouro models from ELLM are the most prominent released implementation, and their published design includes a normalization step at each loop boundary. This paper directly challenges the architectural rationale behind that design choice, showing that the normalization is not a necessary mechanism for depth reusability and that its removal in pretrained models produces a specific, localized failure rather than the global state-norm explosion that the literature has assumed. This reframes a widely adopted architectural component as a potential confound rather than a requirement.

## Implications
For practitioners building or deploying looped language models, this work suggests that the normalization step at loop boundaries may be an unnecessary and potentially harmful architectural constraint, particularly when models are trained end-to-end without it. Model developers should evaluate looped architectures under matched overshoot conditions to avoid conflating depth-reusability benefits with artifacts of unequal extrapolation budgets. For the broader field, the finding that agreement between training and inference loop configurations is the true mechanism for depth reuse implies that future looped-model research should focus on training-inference consistency rather than on adding normalization layers, potentially simplifying architectures and improving extrapolation performance at inference time.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.31943v1)
