---
title: Bud ContextCompact 2.0: Context Compaction for Agent Success and Accuracy with Small Language Models and Constrained Context Windows
published: 2026-10-18T20:15:30Z
authors: Jithin VG, Ditto PS
url: http://arxiv.org/abs/2610.25516v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Bud ContextCompact 2.0: Context Compaction for Agent Success and Accuracy with Small Language Models and Constrained Context Windows

## Abstract
Agents that work for many turns outgrow the context window of the model that serves them, and on small language models (SLMs) and constrained inference systems that window is small. Context compaction replaces older turns with a summary so a session can continue, but it is lossy, costs a model call, and can help or hurt depending on when it runs. We describe Bud ContextCompact 2.0, the compaction built into the Bud agent runtime, and evaluate it in two settings. On recall questions over recorded agent sessions, compaction to a 16K budget raised a 1.2B-parameter model's accuracy to 0.335, from 0.247 with truncation and 0.176 with its full 32K history (p < 0.001), and raised a 9B model from 0.515 (truncation) to 0.577 (p = 0.04). On 100 SWE-bench Verified tasks run end to end by a 27B reasoning model on a 49K-token window (556 graded sessions), compaction raised the resolve rate on long sessions from 41% to 53% (+12.3 points, 95% CI +1.6 to +23.0, McNemar p = 0.043), left short sessions unchanged, and used 13% fewer tokens per solved task at equal total cost. The main failure without compaction was not the history overflowing but a reasoning turn exhausting the room the history left. The gain has limits: it vanished under a 45-minute session budget, because each summary took a median of 161 s, and in a threshold study it appeared only when compaction triggered early enough to leave room. An 8B model submitted after about ten turns at 5-8K tokens and never needed compaction. We argue that the accuracy results transfer across hardware, including CPU inference, for an equivalent model and window, while the time cost scales with the hardware and must be budgeted for.

## Metadata
- **Published**: 2026-10-18T20:15:30Z
- **Authors**: Jithin VG, Ditto PS
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.25516v1)