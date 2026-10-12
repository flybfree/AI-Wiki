---
title: Quality, Not Just Outcome: A Structural Scoring Framework for Selecting Coding-Agent Trajectories for Supervised Fine-Tuning
url: http://arxiv.org/abs/2610.13152v1
type: paper-summary
date: 2026-10-11
source_paper: 2026-10-09_07-40-42Z_Quality_NotJustOutcome_AStructuralScoringFramework.md
generated_at: 2026-10-11 20:50
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces TQS (Trajectory Quality Score), a structural scoring framework designed to evaluate and filter coding-agent interaction trajectories for supervised fine-tuning based on process quality rather than mere outcome success. The authors demonstrate that filtering training data by structural trajectory quality—using signals like information focus, intent-action alignment, and policy dynamics—consistently produces better-performing coding agents on SWE-Bench-Verified compared to training on random or low-quality subsets, all without requiring an LLM judge.

## Key Takeaways
- Outcome-level filtering (selecting only trajectories whose final patches pass a benchmark test suite) is insufficient for coding-agent training because successful trajectories may still embed inefficient interaction patterns such as repetitive file inspection, unstable tool usage, or delayed modification behavior. These poor process patterns become part of the imitation target during supervised fine-tuning, degrading model quality.
- TQS operates directly on trajectory structure using three organized structural signals: information focus (how efficiently the agent gathers relevant context), intent-action alignment (how well the agent's stated goals match its executed tool calls), and policy dynamics (the coherence and progression of the agent's decision-making over time). The framework runs in linear time and requires no LLM-based judge, making it scalable to large corpora.
- Using 155,144 successful trajectories from a public open-license corpus, the authors rank trajectories by TQS and fine-tune coding agents on filtered subsets. Models trained on top-ranked trajectories consistently outperform those trained on random or bottom-ranked subsets on SWE-Bench-Verified, confirming that process-level quality is a meaningful and exploitable signal for data selection.

## Context
Supervised fine-tuning of coding agents has become a dominant paradigm for improving software engineering capabilities in large language models, with benchmarks like SWE-Bench driving rapid progress. However, the field has largely relied on binary pass/fail filtering of trajectories, treating any trajectory that produces a passing patch as equally valuable training data. This paper addresses a critical gap in data curation methodology by showing that the internal structure of an agent's reasoning and tool-use sequence carries substantial signal about training value, and that this signal can be extracted cheaply through deterministic structural analysis rather than expensive LLM-based judging.

## Implications
For practitioners building coding agents, this work suggests that investing in trajectory-quality filtering pipelines can yield measurable performance gains without additional compute for LLM judges, making high-quality data curation accessible at scale. For the broader AI research community, the finding that process quality matters independently of outcome success challenges prevailing assumptions in RLHF and SFT data selection, pointing toward a future where structural and behavioral metrics become standard components of training-data pipelines for agentic systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.13152v1)
