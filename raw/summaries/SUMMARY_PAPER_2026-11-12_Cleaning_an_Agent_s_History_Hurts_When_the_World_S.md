---
title: Cleaning an Agent's History Hurts When the World Still Holds the Error
url: http://arxiv.org/abs/2611.14654v1
type: paper-summary
date: 2026-11-12
source_paper: 2026-11-10_19-06-36Z_CleaninganAgent_sHistoryHurtsWhentheWorldStillHold.md
generated_at: 2026-11-12 21:31
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether editing a tool-using language-model agent's history to "clean up" its mistakes actually helps or hurts downstream task performance, depending on the state of the external world the agent operates in. The authors freeze agents mid-task, manipulate either the history or the world state independently, and measure whether a receiver model can recover remaining targets. They find that the same correct information can either help or hurt depending on how it is framed in the history and whether the world still reflects the original error, demonstrating that history compaction strategies must be world-aware rather than purely content-based.

## Key Takeaways
- On AgentCE-Bench, after an agent commits a wrong value, adding a truthful note beside the preserved error raises recovery from 51% to 66%, while replacing the error with the agent's own completed action lowers recovery from 50% to 44%. This shows that the mere presence of a correct value does not predict its effect; the framing and the preservation of the error context matter critically.
- On AppWorld, after a database write, a success receipt lowers whole-task success from 45% to 28% when the effect is absent from the world, but raises it from 38% to 49% once the effect is present. The 27-point pooled difference is positive in six of eight receivers at 97.5% confidence and seven at 95%, confirming robustness across models.
- A history edit's effect is fundamentally contingent on the world state it describes. Making a history appear clean while the world still holds the error can leave an agent worse off than performing no edit at all, undermining the common assumption that removing or correcting erroneous steps is always beneficial.

## Context
Modern agentic systems rely on history management strategies such as compaction, summarization, and handoff to keep context windows manageable and to present a coherent narrative to downstream components. Prior work in this area has largely assumed a fixed world state, treating history editing as a purely textual operation where showing a corrected step and declaring it done are equivalent actions. This paper breaks that assumption by decoupling history edits from world state changes, revealing a gap between how agents "talk about" their mistakes and what the environment actually reflects. This is significant because real-world deployments—database operations, API calls, file system modifications—often leave persistent side effects that history edits cannot erase.

## Implications
For practitioners building agentic pipelines, this work warns that naive history cleaning or "repair" strategies can actively degrade performance when the external world still encodes the original error. System designers should consider whether a history edit is consistent with the actual world state before applying it, and should prefer preserving error context with truthful annotations over silently replacing mistakes with completed actions. For the broader field, this finding challenges the design principle that cleaner histories always lead to better agent behavior, suggesting that future agent architectures need world-aware history management modules that verify environmental consistency before rewriting an agent's narrative.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.14654v1)
