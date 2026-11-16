---
title: PaperCritic: Training AI Reviewers to Assess the Soundness of Papers
published: 2026-11-13T07:14:57Z
authors: Hyun Ryu, Ji Yong Cho, Eunho Yang, Moontae Lee, June Yong Yang, Sean Welleck, Carolyn Rose
url: http://arxiv.org/abs/2611.17834v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PaperCritic: Training AI Reviewers to Assess the Soundness of Papers

## Abstract
As AI conference submissions grow rapidly, AI reviewers are being considered as an alternative. However, simply imitating human reviewing is problematic because reviewing serves multiple purposes, including evaluating papers' soundness, interestingness, and clarity, the last two of which are subjective. In this work, we focus solely on evaluating soundness, the most important and objective criterion, and define the learning objective as jointly maximizing (1) precision, based on the soundness and substantiveness of review points, and (2) recall, the coverage of high-quality reference review points. Under this problem formulation, we construct a quality-labeled review point dataset, PaperSound-23K, using 1K ICLR submissions and 23K human-written and LLM-generated review points. Using this dataset, we train an AI reviewer model, PaperCritic, through reinforcement learning with the F1 score of precision and recall as the reward. Our experiments show that PaperCritic outperforms frontier models and models trained with other AI reviewer training methods on an in-domain test set. Surprisingly, learning to review ICLR submissions also transfers to reviewing Nature-family papers and even to out-of-domain reviewing tasks (e.g., code review, legal contract review, and feedback on story writing).

## Metadata
- **Published**: 2026-11-13T07:14:57Z
- **Authors**: Hyun Ryu, Ji Yong Cho, Eunho Yang, Moontae Lee, June Yong Yang, Sean Welleck, Carolyn Rose
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.17834v1)