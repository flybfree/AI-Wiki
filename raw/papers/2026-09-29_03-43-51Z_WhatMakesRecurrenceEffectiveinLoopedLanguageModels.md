---
title: What Makes Recurrence Effective in Looped Language Models?
published: 2026-09-29T03:43:51Z
authors: Xinlin Zhuang, Siyuan Wang, Imran Razzak, Weiyang Liu
url: http://arxiv.org/abs/2609.36636v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# What Makes Recurrence Effective in Looped Language Models?

## Abstract
Looped language models (LoopLMs) increase computational depth through parameter sharing, offering a path to scale inference computation without adding parameters. However, it remains unclear when additional recurrence is beneficial and how architectural choices affect its effectiveness. Through controlled experiments, we systematically examine (1) when recurrence helps, (2) where it should be applied, and (3) how its conditioning affects performance. Our evaluation covers inference budgets below, within, and beyond the training horizon under knowledge and reasoning tasks. (1) We find that recurrence can improve reasoning beyond the training horizon while degrading knowledge performance, but harder reasoning instances do not consistently benefit more. (2) Performance also depends on how distinct layers and recurrent iterations are allocated, showing that effective depth alone is insufficient to predict behavior. Non-recurrent output layers improve robustness to under-unrolling, while the preferred placement of input and output layers varies with inference budget. (3) Finally, we find that conventional initial-state injection offers limited robustness to varying recurrence depth. We therefore propose history-state injection as an alternative, and show that channel-wise history-state injection combined with timestep conditioning offers a low-cost and more effective design, better preserving knowledge under extended unrolling while improving robustness across inference budgets. Overall, our results clarify when recurrent computation helps, where it fails, and offer practical guidelines for designing LoopLMs across variable inference budgets.

## Metadata
- **Published**: 2026-09-29T03:43:51Z
- **Authors**: Xinlin Zhuang, Siyuan Wang, Imran Razzak, Weiyang Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.36636v1)