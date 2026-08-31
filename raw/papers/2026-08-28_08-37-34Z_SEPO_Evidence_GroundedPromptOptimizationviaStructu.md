---
title: SEPO: Evidence-Grounded Prompt Optimization via Structural Editing
published: 2026-08-28T08:37:34Z
authors: Xiaoyu Ma, Haoyue Liu, Yiwen Li, Jionghao Zhu, Zhichao Wang, Ye Chen, Xiaoying Tang
url: http://arxiv.org/abs/2608.28067v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SEPO: Evidence-Grounded Prompt Optimization via Structural Editing

## Abstract
Existing API-only prompt optimisers are often described as interpretable, but in practice, this usually means only post-hoc inspectability: each iteration still rewrites the prompt as one opaque string, leaving a trace of full-prompt diffs rather than localisable, machine-readable edits. This paper introduces SEPO (Structural, Evidence-grounded Prompt Optimization), a multi-trajectory prompt optimiser centred on edit-effect lineage feedback. Rather than treating each iteration as an isolated whole-prompt rewrite, SEPO locally edits stable, typed units in a two-layer prompt schema, links the target and realised structural operations of each edit to the examples it newly fixes or breaks, and carries this edit-effect record forward to guide later architect calls on the same search branch. This makes prompt optimisation addressable, attributable, and actionable. Across a 14-task held-out suite, SEPO improves over the strongest baseline, GEPA, by 3.1 pp on Llama-3.1-8B-Instruct and 2.2 pp on Qwen3-8B, reaching 61.9% and 73.3% macro accuracy. SEPO also lies on both the optimisation-time and test-time Pareto frontiers, spending 2.9M optimisation tokens versus 4.1M for GEPA and producing prompts over 5x shorter.

## Metadata
- **Published**: 2026-08-28T08:37:34Z
- **Authors**: Xiaoyu Ma, Haoyue Liu, Yiwen Li, Jionghao Zhu, Zhichao Wang, Ye Chen, Xiaoying Tang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28067v1)