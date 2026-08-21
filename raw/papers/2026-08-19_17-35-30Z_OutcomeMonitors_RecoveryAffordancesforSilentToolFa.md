---
title: Outcome Monitors: Recovery Affordances for Silent Tool Failures
published: 2026-08-19T17:35:30Z
authors: Sugam Panthi, Rabab Abdelfattah
url: http://arxiv.org/abs/2608.19303v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Outcome Monitors: Recovery Affordances for Silent Tool Failures

## Abstract
When a tool call times out, the agent sees the failure and can route around it. A cached error page or negative price can instead arrive in the expected format and be consumed as fact. We introduce Outcome Monitors, which detect violations of outcome contracts mined from task-disjoint traces or derived from public schemas. On a violation, the monitor preserves the result and issues a nonbinding receipt naming the violated property and public recovery tools. In frozen, prespecified evaluations with injected failures, Outcome Monitors raise ToolMaze completion from 10.9% to 28.1% across four models in two provider families and replicate in a third. In tau-bench retail, completion improves by 14.0 and 12.0 points on two tiers. In separate ToolMaze controls, removing the recovery-tool list eliminates the measured gain and restoring it recovers the effect; diagnostic detail and timing produce no detectable differences. Gains concentrate where the fault blocks completion. On a suite transcribed from a published incident taxonomy, detection outside the mined vocabulary falls to 46%, though delivery continues and completion is unchanged. Recovery tools are the active receipt content in these controls; extending detection beyond the contract vocabulary remains open.

## Metadata
- **Published**: 2026-08-19T17:35:30Z
- **Authors**: Sugam Panthi, Rabab Abdelfattah
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.19303v1)