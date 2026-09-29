---
title: RepoMAS: Solving Progressively Specified Tasks with Issue-Driven Multi-Agent Systems
published: 2026-09-26T11:33:53Z
authors: Yuchen Song, Andong Chen, Wenxin Zhu, Muyun Yang, Tiejun Zhao
url: http://arxiv.org/abs/2609.32490v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RepoMAS: Solving Progressively Specified Tasks with Issue-Driven Multi-Agent Systems

## Abstract
LLM-based multi-agent systems (MASs) have shown strong potential for solving complex tasks, but most assume that task requirements are sufficiently specified before execution. In practice, user requests are often incomplete, and additional requirements may only become clear during reasoning, tool use, or execution. We refer to such problems as progressively specified tasks.   To systematically study this setting, we introduce ProgSpec, a benchmark that evaluates final outputs against requirements explicitly stated in the initial request and additional requirements supported by the available task evidence. We further propose RepoMAS, an issue-driven multi-agent framework inspired by open-source project management. RepoMAS records newly discovered requirements, conflicts, and failures as structured Issues and uses them to revise the task specification and execution structure during problem solving.   Across ProgSpec and five existing benchmarks, RepoMAS achieves the best performance. Further analyses show that its issue-driven revision and repository maintenance mechanisms consistently contribute to performance. These results highlight the importance of allowing MASs to revise not only how a task is solved, but also revise their explicit representation of task requirements during execution.

## Metadata
- **Published**: 2026-09-26T11:33:53Z
- **Authors**: Yuchen Song, Andong Chen, Wenxin Zhu, Muyun Yang, Tiejun Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32490v1)