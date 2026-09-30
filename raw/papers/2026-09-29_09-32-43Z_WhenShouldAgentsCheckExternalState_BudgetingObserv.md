---
title: When Should Agents Check External State? Budgeting Observations for Stored Intentions
published: 2026-09-29T09:32:43Z
authors: Zhengkun Di, Bin Shi, Kai Sun, Yiming Xu, Bo Dong
url: http://arxiv.org/abs/2609.37125v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Should Agents Check External State? Budgeting Observations for Stored Intentions

## Abstract
Prospective memory allows an agent to retain an intention tied to a future condition, but the stored intention does not reveal whether that condition currently holds. Checking it may require web access, multi-step tool use, and paid calls. Existing systems decide when intentions require attention, but do not allocate the resulting observations under a shared budget. We introduce the first resource-allocation formulation for the external observations required by stored intentions under a shared episode budget. BudgetPM offers two policy variants that share a hard-budget executor. BudgetPM-Static uses a lightweight Logistic scorer to learn whether a check improves the current decision. BudgetPM-Sequential distills full-episode hindsight schedules into a lightweight policy that decides when to spend or reserve capacity using only pre-query information at deployment. We evaluate BudgetPM against two public memory-agent systems, five matched controls, and four hand-designed monitoring or budget-adaptation rules. Across two benchmarks and three backbones, BudgetPM-Static outperforms adapted Mem0 and PMA workflows. On PM-Bench, its Logistic scorer reaches competitive quality--cost operating points alongside higher-capacity scorers and retains 99.9--100\% of unconstrained quality with 42--54\% fewer observations. Under severe scarcity and the same hard caps, BudgetPM-Sequential exceeds the strongest tested natural monitoring schedule by 1.92--2.58 Set F1 points. It reaches the same Set F1 and on-time recall with 16--33\% fewer observations. Matched attribution, exact-cost analysis, and a fixed-budget load intervention link this gain to competition between present and future opportunities. These results yield a demand--capacity design rule: local gating works when capacity covers demand, while future-aware supervision adds value when observations compete across time.

## Metadata
- **Published**: 2026-09-29T09:32:43Z
- **Authors**: Zhengkun Di, Bin Shi, Kai Sun, Yiming Xu, Bo Dong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.37125v1)