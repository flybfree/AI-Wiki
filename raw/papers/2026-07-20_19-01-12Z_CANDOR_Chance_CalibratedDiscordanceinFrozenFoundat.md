---
title: CANDOR: Chance-Calibrated Discordance in Frozen Foundation Encoders
published: 2026-07-20T19:01:12Z
authors: Soroosh Tayebi Arasteh, Sven Nebelung, Daniel Truhn
url: http://arxiv.org/abs/2607.18451v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CANDOR: Chance-Calibrated Discordance in Frozen Foundation Encoders

## Abstract
Frozen encoders are chosen by how well a lightweight head reads a finding from their features, not whether the geometry separates it. Nearest-neighbor discordance does, but with unequal banks the opposite-label neighbor wins on density, not geometry, so prevalence alone makes an uninformed encoder look blind. We introduce CANDOR, a discordance measure whose equal-size banks are symmetric under a label swap, fixing its chance level at exactly one half. Across 22 encoders, 20 datasets from 7 domains, and 605,443 images, this correction reverses the conclusion. Collapse falls below chance almost everywhere, so no encoder is blind, yet all are weak: the best chest model reads pneumothorax at 84.5 AUROC and still places 18.4% of those positives nearer an opposite-label film than its own kind in the same hospital. The same encoder that resolves bird species at 4.5 leaves chest findings at 42.8 and glaucoma at 49.8, at chance and worse than random weights. Such a case caps the normalized margin of any Lipschitz head, yet some head among eleven is correct on all but 2.8% of cases where one head misses 35.9%: the deficit is selection, not information. Erasure retention is associated with collapse; we detect no association with the objective, scale, recency, or size of the finding. Because the chance level is fixed, CANDOR can be read before any head is trained, flagging which findings a frozen encoder supports poorly.

## Metadata
- **Published**: 2026-07-20T19:01:12Z
- **Authors**: Soroosh Tayebi Arasteh, Sven Nebelung, Daniel Truhn
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18451v1)