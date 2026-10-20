---
title: Bud ContextCompact 2.0: Context Compaction for Agent Success and Accuracy with Small Language Models and Constrained Context Windows
url: http://arxiv.org/abs/2610.25516v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-18_20-15-30Z_BudContextCompact2_0_ContextCompactionforAgentSucc.md
generated_at: 2026-10-20 00:22
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Bud ContextCompact 2.0, a context compaction mechanism built into the Bud agent runtime that replaces older conversation turns with summaries to allow agents to continue operating within constrained context windows. The authors evaluate the system across two settings—recall accuracy on recorded sessions and end-to-end task resolution on SWE-bench Verified—and demonstrate that compaction significantly improves both accuracy and task completion rates for small and mid-sized language models, though the gains are bounded by time costs and trigger timing.

## Key Takeaways
- Compaction to a 16K token budget raised a 1.2B-parameter model's recall accuracy from 0.247 (truncation) and 0.176 (full 32K history) to 0.335 (p < 0.001), and improved a 9B model from 0.515 to 0.577 (p = 0.04), showing that summarizing older turns is strictly better than either truncating or retaining full history for small models.
- On 100 SWE-bench Verified tasks run by a 27B reasoning model within a 49K-token window across 556 graded sessions, compaction raised the resolve rate on long sessions from 41% to 53% (McNemar p = 0.043) while using 13% fewer tokens per solved task at equal total cost; short sessions saw no change, indicating compaction specifically rescues long-running agent sessions.
- The primary failure mode without compaction was not history overflow but a reasoning turn exhausting the remaining room left by the history, and the benefit vanished under a 45-minute session budget because each summary call took a median of 161 seconds, while an 8B model that submitted after roughly ten turns at 5-8K tokens never triggered compaction at all.

## Context
As agentic systems proliferate in production environments, the tension between multi-turn task completion and finite context windows becomes a critical engineering bottleneck, particularly on small language models and constrained inference hardware such as CPU-only deployments. This paper addresses a practical gap in the literature by providing a concrete, evaluated compaction pipeline rather than theoretical proposals, and it quantifies both the accuracy gains and the latency penalties that practitioners must budget for when deploying agents on resource-limited infrastructure.

## Implications
For practitioners building agent systems on edge devices, on-premise CPU clusters, or any constrained inference environment, this work provides empirical evidence that context compaction is not merely an optimization but a necessity for maintaining task success in long-running sessions, while also warning that the summarization cost must be explicitly budgeted to avoid session timeouts. The finding that accuracy results transfer across hardware for equivalent models and windows suggests that compaction strategies can be standardized across deployment targets, but the time cost scaling with hardware means that system architects must co-design compaction triggers with their inference infrastructure rather than treating them as a software-only concern.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.25516v1)
