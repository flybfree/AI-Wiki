---
title: What Does a Harness Repair? A Preregistered Study of Visibility, Baseline Adequacy and Evaluation Defects
published: 2026-10-04T20:56:07Z
authors: Bowen Xu, Boyu Chen
url: http://arxiv.org/abs/2610.05533v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# What Does a Harness Repair? A Preregistered Study of Visibility, Baseline Adequacy and Evaluation Defects

## Abstract
Harness search keeps a change to the prompts, reasoning switches, token budgets or parsers around a frozen model if the change raises a score. Such a gain can come from answers the parser could not read before, a weak comparison, or a defect in the evaluation. We preregistered a study of where these gains come from, with three small models, three benchmarks, replication and test partitions, a GEPA search arm and six evaluation defects injected one at a time, and we report all 47 primary endpoints. Turning thinking off raised accuracy over a capped thinking setting in 5 of 9 model-benchmark cells, and in each the gain came mostly from questions where the capped setting gave no readable answer. The thinking-off setting was not meaningfully worse than a rescue configuration or four GEPA-selected harnesses in 11 of 13 comparisons, and lost to the rescue on GSM8K for two models. GEPA repaired its broken starting points, but none of its selected harnesses was more accurate than the thinking-off setting. A thinking budget in the serving engine, which also allows a longer answer, lowered truncation and raised the parse rate in 6 of 9 cells. In 6 of 15 evaluable defect-model pairs, replication through the same pipeline reproduced the defect's distortion instead of revealing it. On the LongevityBench multiple-choice tasks, only the longevity-tuned model beat the strongest constant-label baseline.

## Metadata
- **Published**: 2026-10-04T20:56:07Z
- **Authors**: Bowen Xu, Boyu Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.05533v1)