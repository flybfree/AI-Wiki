---
title: Privileged Likelihood Is Not Automatically Value: Three Checks for Token Credit in On-Policy Self-Distillation
published: 2026-08-10T08:18:48Z
authors: Xuan-Phi Nguyen, Shrey Pandit, Yiran Zhao, Anurag Koul, Zeyu Liu, Shafiq Joty
url: http://arxiv.org/abs/2608.09263v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Privileged Likelihood Is Not Automatically Value: Three Checks for Token Credit in On-Policy Self-Distillation

## Abstract
Outcome verifiers score completed reasoning traces but do not assign credit to intermediate tokens. Privileged self-distillation attempts to fill this gap by rescoring a model's own rollout with training-only information. A token likelihood change, however, is not automatically outcome credit. We separate three questions: whether the score tracks better actions, whether feedback construction changes what is compared, and what behavior the training loss reinforces. We establish these distinctions formally. When a rollout is scored using hindsight feedback written about that same rollout, its content determines both the tokens and the scoring context, creating direct self-dependence. Using feedback from another rollout of the same problem removes this dependence but does not guarantee a useful score. In matched experiments with a 20B model on AIME 2025, the implemented additive score is near chance (AUC=0.505) and slightly favors incorrect traces after length adjustment. In the paired comparison, the outcome-only control records 64.2\%, versus 24.2\%--33.9\% for five token-score variants. The results motivate validating score meaning, feedback construction, and training behavior separately before calling a likelihood signal credit.

## Metadata
- **Published**: 2026-08-10T08:18:48Z
- **Authors**: Xuan-Phi Nguyen, Shrey Pandit, Yiran Zhao, Anurag Koul, Zeyu Liu, Shafiq Joty
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09263v1)