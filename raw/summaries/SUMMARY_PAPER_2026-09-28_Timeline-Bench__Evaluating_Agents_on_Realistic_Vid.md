---
title: Timeline-Bench: Evaluating Agents on Realistic Video-Editing Tasks, from Raw Footage to Final Cut
url: http://arxiv.org/abs/2609.35143v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_13-28-17Z_Timeline_Bench_EvaluatingAgentsonRealisticVideo_Ed.md
generated_at: 2026-09-28 23:10
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces Timeline-Bench, a comprehensive benchmark designed to evaluate AI agents on realistic video-editing workflows that require transforming raw production footage into polished final cuts. The study reveals that even the most advanced frontier models paired with coding harnesses struggle significantly, resolving only about a quarter of tasks while consistently failing quality assessments calibrated by professional editors. Ultimately, the research highlights a critical gap between current agent capabilities and the nuanced craft required for professional creative work.

## Key Takeaways
- Timeline-Bench comprises 56 real-world video-editing challenges that provide source assets, editing briefs, and automated verification tests covering format compliance, content accuracy, explicit requirements, and a quality metric validated through thousands of blind editor judgments.
- When tested across sixteen agent configurations combining frontier models with coding environments like Codex and Claude Code, performance remained low, with the top-performing system resolving just 26.8 percent of tasks and the average success rate sitting at 14.0 percent.
- The majority of failures stem from missing the quality test rather than technical errors, as agents primarily analyze footage through static frames and transcripts to check for defects instead of developing the temporal pacing, narrative flow, and editorial intuition that define professional video craft.

## Context
As AI systems transition from isolated task completion to executing long-horizon creative pipelines, existing evaluation frameworks have proven inadequate for measuring

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.35143v1)
