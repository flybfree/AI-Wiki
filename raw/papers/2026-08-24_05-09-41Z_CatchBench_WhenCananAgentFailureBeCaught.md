---
title: CatchBench: When Can an Agent Failure Be Caught?
published: 2026-08-24T05:09:41Z
authors: Yue Zhao
url: http://arxiv.org/abs/2608.22808v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CatchBench: When Can an Agent Failure Be Caught?

## Abstract
When can an agent failure be caught? An audit is usually limited by the record rather than by the method. CatchBench therefore puts one auditor's question to three information states: the declared configuration before a run (PRE), a growing prefix of its trace (LIVE), and the finished trace (POST). Prior benchmarks fix one of these states or vary the telemetry; to our knowledge none scores all three under one task-method interface. Each state admits different questions, so seven task contracts carry their own labels and metrics rather than one leaderboard. Four are evidential; three are Gold-derived mechanism diagnostics.   The release scores 72 entrants, from rule scanners and structural models to eleven LLM judges across nine model families (GPT, Claude, Gemini, Gemma, Llama, Qwen, DeepSeek, Mistral, Nova), over 1187 declared configurations and 1162 recorded runs. Most of the arena does not order: 47 of 118 pre-declared contrasts separate, and the rest are published unresolved rather than ranked. The two sharpest results cut against our own data. One rule ignores every name and permission; it flags each capability declared after the first. On one of six configuration sources it reaches a perfect F1, so a score there measures how the corpus was built rather than how well a method reasons. Our admissibility bar then rejected one injected substrate and withheld evidential status from the other. A benchmark number is therefore not interpretable until the process behind its labels is published and tested for the shortcut it may leave. We report both, and regenerate every ordering from released predictions with no model call.

## Metadata
- **Published**: 2026-08-24T05:09:41Z
- **Authors**: Yue Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22808v1)