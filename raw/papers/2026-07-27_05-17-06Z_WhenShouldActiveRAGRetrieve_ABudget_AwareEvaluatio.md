---
title: When Should Active RAG Retrieve? A Budget-Aware Evaluation of Utility, Calibration, and Cost
published: 2026-07-27T05:17:06Z
authors: Pin Qian, Su Wang, Chong Peng, Junxian You, Lifei Liu, Haoran Yu, Yihang Chen, Xiaochong Jiang
url: http://arxiv.org/abs/2607.24010v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Should Active RAG Retrieve? A Budget-Aware Evaluation of Utility, Calibration, and Cost

## Abstract
Active RAG systems decide when to retrieve external knowledge during generation, making them a budget-sensitive case of agentic RAG and self-adaptive retrieval. Yet evaluations often leave the operating point underspecified: two systems may both claim a 50% evidence-usage budget while realizing different held-out usage rates, so higher accuracy can reflect a looser budget rather than a better retrieval policy. We study budget-aware evaluation for Active RAG by recasting active retrieval as utility estimation, where retrieval is valuable only through its marginal correctness change over a no-retrieval answer. This view separates three questions that single-point evaluations conflate: whether trigger scores rank useful retrieval decisions, whether thresholds calibrated on past data meet future budgets, and how trigger-side computation changes deployment cost. We operationalize these questions with exact top-k utility frontiers, deployable threshold frontiers, conservative budget frontiers, harm audits, and cost decompositions. Across knowledge-intensive multi-hop QA datasets and open instruction models, retrieval harm is non-negligible, router rankings change across datasets and budgets, nominal thresholds can miss target usage, and simple uncertainty or retrieval-score baselines often rival learned utility routers. Budget-aware Active RAG evaluations should therefore report frontiers, realized usage, threshold-transfer error, harm rates, and cost decompositions alongside accuracy.

## Metadata
- **Published**: 2026-07-27T05:17:06Z
- **Authors**: Pin Qian, Su Wang, Chong Peng, Junxian You, Lifei Liu, Haoran Yu, Yihang Chen, Xiaochong Jiang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24010v1)