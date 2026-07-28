---
title: How Well Can AI Generate Backlogs from App Mockups?
published: 2026-07-24T20:40:22Z
authors: Andrea Lezcano Airaldi, Lourdes Romera, Walid Maalej
url: http://arxiv.org/abs/2607.22902v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# How Well Can AI Generate Backlogs from App Mockups?

## Abstract
Creating sprint backlogs requires considerable effort, as items such as epics, user stories, and tasks can be missed or inconsistently specified. We propose a multimodal approach to support backlog generation from visual app mockups, an artifact available at early project stages. We evaluate three prompting strategies on GPT-4o: a zero-shot baseline, Compositional Chain-of-Thought (CCoT) for vision-language reasoning, and a persona-driven prompt. We study seven app development projects across two countries and interview developers about the results. Overall, we observed that the baseline prompt favours recall over precision, whereas CCoT is more balanced, achieving average F1 scores of 52-66% for epics and user stories. Tasks were more challenging to generate accurately. Precision gains were most consistent when adding architectural context, particularly for backend tasks (precision gains up to 35%). Interviews with developers revealed that up to 26% of false positives were still considered useful, reflecting the creative and open-ended nature of backlog creation. To capture this, we propose a new measure called Revised Recall, which complements ground-truth evaluation with developer assessments. Our findings suggest that hybrid prompting with architectural context can assist backlog generation from early mockups, though results vary by item type and developer oversight remains necessary.

## Metadata
- **Published**: 2026-07-24T20:40:22Z
- **Authors**: Andrea Lezcano Airaldi, Lourdes Romera, Walid Maalej
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22902v1)