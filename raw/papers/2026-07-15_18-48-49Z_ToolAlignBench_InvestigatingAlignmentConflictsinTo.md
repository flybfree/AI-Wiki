---
title: ToolAlignBench: Investigating Alignment Conflicts in Tool-Calling Enabled LLMs
published: 2026-07-15T18:48:49Z
authors: Aryan Keluskar, Amrita Bhattacharjee, Huan Liu
url: http://arxiv.org/abs/2607.14285v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ToolAlignBench: Investigating Alignment Conflicts in Tool-Calling Enabled LLMs

## Abstract
Safety alignment in LLMs aims to align models with human values, but which values take precedence when they conflict? We investigate this question in the context of tool-calling LLM agents deployed in regulated industries, where agents processing confidential documents may encounter content that triggers safety-trained values (e.g., public welfare) that conflict with deployment-context instructions (e.g., internal logging). To empirically verify this phenomenon, we build a benchmark of 128 scenarios across 16 domains. We find that safety-aligned open-source models override their deployment instructions up to 43.4% of the time, engaging in whistleblowing, data exfiltration, and evidence tampering when processing documents that suggest organizational wrongdoing. We also find that abliteration reduces rates of external whistleblowing. These results reveal a fundamental tension in pluralistic alignment, where the same safety training that protects users can cause agents to act against deployment instructions in ways that create unpredictable liability risks. We release our benchmark as a framework to support evaluation of agent behavior under competing legitimate interests.

## Metadata
- **Published**: 2026-07-15T18:48:49Z
- **Authors**: Aryan Keluskar, Amrita Bhattacharjee, Huan Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.14285v1)