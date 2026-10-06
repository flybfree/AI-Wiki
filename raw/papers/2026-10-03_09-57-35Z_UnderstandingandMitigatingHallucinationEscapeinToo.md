---
title: Understanding and Mitigating Hallucination Escape in Tool-Using LLM Agents
published: 2026-10-03T09:57:35Z
authors: Peigui Qi, Kunsheng Tang, Yide Song, Weiming Zhang, Nenghai Yu
url: http://arxiv.org/abs/2610.04409v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Understanding and Mitigating Hallucination Escape in Tool-Using LLM Agents

## Abstract
Large language models (LLMs) increasingly serve as autonomous agents that invoke external tools. However, this capability introduces tool hallucination, selecting incorrect tools or generating invalid calls. Existing mitigation methods report substantial improvements, yet we identify a previously overlooked failure mode that we term Hallucination Escape. These methods reduce hallucination on the tool configuration they are tuned on but increase it on other configurations, canceling out the gain. We further investigate this phenomenon and find that hallucination rises sharply when a model's intrinsic tool-use tendencies conflict with the current tool configuration, and that existing methods reinforce rather than suppress these tendencies, which in turn contributes to hallucination escape. Building on these findings, we propose EscapeGuard, a training-free inference-time method that combines conflict-aware gating with configuration-derived attention enhancement to mitigate tool hallucination while preventing hallucination escape. Across six benchmarks on various models, EscapeGuard reduces tool-selection hallucination by 9.0 pp and suppresses hallucination escape, lowering the cross-configuration mean by 23.7 pp and achieving an 89.1% net improvement in paired-query evaluation. We hope this work can encourage evaluation beyond a single tool configuration and pave the way for more reliable tool-using LLM agents.

## Metadata
- **Published**: 2026-10-03T09:57:35Z
- **Authors**: Peigui Qi, Kunsheng Tang, Yide Song, Weiming Zhang, Nenghai Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04409v1)