---
title: ReplayLens: Auditing Agents' Use of Outcomes
published: 2026-09-28T02:56:32Z
authors: Dong Xu, Zhangfan Yang, Jiantao Wu, Shipeng Zhang, Zexuan Zhu, Jiangqiang Li, Jun Zhang, Junkai Ji
url: http://arxiv.org/abs/2609.34177v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ReplayLens: Auditing Agents' Use of Outcomes

## Abstract
When an agent reuses logged experience, a changed decision may reflect the recorded score, the action's name, or the record's position in storage. Standard memory evaluations do not reveal which relationship drives that change. We introduce ReplayLens, a black-box audit that changes one relationship in the stored history at a time, holds the remaining interface fixed, and measures the resulting decision. Four interventions target four relationships. Outcome reassignment swaps which scores belong to which actions. Pair transport moves intact action-score pairs to new record slots. Consistent renaming relabels actions in both history and menu. Key-slot reassignment changes both score attachment and position. A constructive separation shows why the audit is needed: two memory writers with identical endpoint accuracy respond differently to the same replay, so conventional evaluation cannot resolve the underlying dependence. On black-box LLM interfaces, swapping scores changes decisions while moving intact pairs does not, separating score attachment from record order. A bounded-memory study exposes ingestion-order sensitivity that endpoint comparison misses. In sequential experiment planning, altered historical scores redirect exploration and reduce final utility despite fresh measurements. A code-debugging agent with sealed hidden tests shows the same pattern outside model selection. ReplayLens provides a relationship-level audit for deciding whether logged experience can be merged, reordered, or reindexed safely.

## Metadata
- **Published**: 2026-09-28T02:56:32Z
- **Authors**: Dong Xu, Zhangfan Yang, Jiantao Wu, Shipeng Zhang, Zexuan Zhu, Jiangqiang Li, Jun Zhang, Junkai Ji
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34177v1)