---
title: The Sleeping Agent: What Gist-Based Context Compression Loses and Why
url: http://arxiv.org/abs/2608.11775v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_08-19-15Z_TheSleepingAgent_WhatGist_BasedContextCompressionL.md
generated_at: 2026-08-12 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how gist-based context compression affects long-horizon language model agents by using a biologically inspired framework called Salience‑Weighted Consolidation. It finds that compression improves multi‑hop reasoning and factual questions but harms temporal questions, which score far below full‑context baselines.

## Key Takeaways
- Gist compression outperforms simple truncation on multi‑hop reasoning and single‑hop factual tasks, showing a clear task‑type interaction. - Temporal questions remain substantially harder under compression because the abstraction discards dates and times while preserving relational structure. - A one‑sentence prompt change increases temporal expression preservation from 3.05% to 62.39%, improving judge accuracy by +0.314.

## Context
Long‑horizon agents must balance memory efficiency with information fidelity, yet existing compression methods lack systematic diagnostic tools. This work introduces a structured probe that aligns compression behavior with cognitive processes such as sleep‑based consolidation, offering insight into the trade‑offs of gist abstraction in dialogue systems.

## Implications
For developers building conversational AI, the findings suggest that preserving temporal cues is crucial for tasks requiring precise timing information. The precision nature of the fix indicates that targeted prompt engineering can mitigate degradation without sacrificing overall compression benefits.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11775v1)
