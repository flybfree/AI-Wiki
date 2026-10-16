---
title: ToolBottleneckBench: Measuring Tool-Agent Performance under Controlled Pressures and Fixed Harness Budgets
published: 2026-10-15T01:59:58Z
authors: Zichuan Xu, Yuyang Dong, Makoto Onizuka, Chuan Xiao
url: http://arxiv.org/abs/2610.21098v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ToolBottleneckBench: Measuring Tool-Agent Performance under Controlled Pressures and Fixed Harness Budgets

## Abstract
The success score of a tool agent reflects both its model and the budgets of the harness that runs it. We present ToolBottleneckBench, a benchmark that measures tool-agent performance under controlled pressures and fixed harness budgets. Synthetic enterprise tasks stay fixed while one pressure varies: the registered tool catalog, the visible tool menu, the certified workflow, or the encoding of returned records. An exact grader records the first unmet obligation of each failed episode and the harness limit, if any, that ended it. Across 21 model and harness configurations, the visible menu is the only one of the three pressures that act on the model with a large penalty, and this penalty tracks truncation at the completion cap. Raising the cap sixteenfold removes most of the penalty in the truncation-heavy configurations. Most failures end at a harness limit, and the failure record identifies the assigned pressure no more reliably than a count of tool calls. The repairs that help change which tools reach the model or who issues the calls, and only two repairs, neither improving model behavior, beat every configuration switch. We recommend reporting pressure effects with the harness budgets under which they were measured. We release the benchmark at https://github.com/zichuanxu/tool-bottleneck-bench.

## Metadata
- **Published**: 2026-10-15T01:59:58Z
- **Authors**: Zichuan Xu, Yuyang Dong, Makoto Onizuka, Chuan Xiao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.21098v1)