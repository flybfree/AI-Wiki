---
title: Agreement rather than normalisation keeps depth reusable in looped language models
published: 2026-10-22T21:42:16Z
authors: Ivan Viakhirev, Kirill Borodin, Maxim Abramov, Grach Mkrtchian
url: http://arxiv.org/abs/2610.31943v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agreement rather than normalisation keeps depth reusable in looped language models

## Abstract
Looped language models apply one block of layers repeatedly, and the design pays off only if depth is reusable: loop steps beyond the trained budget must remain usable at inference. We ask whether that rests on normalising the state between loop steps, as the released Ouro models do, or on agreement between the loop a model is trained with and the loop it is run with. On released weights this loop-boundary normalisation can be removed without adding parameters and with the readout path bit-identical, and the operation is an identity at one loop step, which serves as an implementation check. Removing it takes Ouro-1.4B and Ouro-2.6B to zero accuracy by the trained budget on a balanced binary task (chance 0.500). State-norm growth, the failure that prior accounts predict, is not the cause: the norm stays within a factor of 2.021 while the head commits to a single wrong token. Yet in 19M-parameter models trained from scratch on two synthetic tasks, 16 seeds per configuration, training without the normalisation is never worse than training with it and extrapolates better: the two are closest at the trained depth and separate on both sides of it (Cliff's delta up to 0.867 beyond the budget). Both results follow if agreement, and not the normalisation itself, is what keeps depth reusable. The damage sits in the readout together with the last layer of the block: in the models trained from scratch, refitting the head over the frozen modified loop recovers a third of the lost accuracy and plateaus, while refitting the last block layer with it recovers all of it. Finally, comparing looped with stacked depth at an equal inference loop count is confounded by unequal overshoot of the trained budget; at matched overshoot the advantage of looping vanishes on one task and shrinks on the other.

## Metadata
- **Published**: 2026-10-22T21:42:16Z
- **Authors**: Ivan Viakhirev, Kirill Borodin, Maxim Abramov, Grach Mkrtchian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.31943v1)