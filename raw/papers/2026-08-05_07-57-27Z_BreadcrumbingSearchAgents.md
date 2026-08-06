---
title: Breadcrumbing Search Agents
published: 2026-08-05T07:57:27Z
authors: Xuebin Li, Hanqing Zhao, Siyuan Liang, Kejiang Chen, Weiming Zhang, Dacheng Tao, Nenghai Yu
url: http://arxiv.org/abs/2608.04565v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Breadcrumbing Search Agents

## Abstract
LLM-based search agents are widely used for information-seeking tasks, but their reliance on external tool returns introduces a critical security risk: web content retrieved during execution is untrusted, exposing agents to prompt injection and goal hijacking. Prior work on search-agent safety primarily focuses on static web-content injection, but modern agents issue follow-up queries and cross-check competing sources, so a single injected page is often diluted or rejected. We show that the channel delivering search and page observations is a fragile security boundary: beyond exposing the agent to a single poisoned page, a mediated search interface can repeatedly steer how the agent gathers evidence and forms its final answer. Under a constrained tool-intermediary threat model, appending only one controlled result per query can substantially increase attack success when the evidence is coordinated across the agent's trajectory. We study this setting with a strategy-driven long-horizon attack system and introduce Authority-Chain Hijack (ACH), an expert-refined strategy that turns isolated search-result and page-content manipulations into a coherent evidence chain across seemingly corroborating sources. ACH achieves the highest Overall ASR among all baselines, reaching 55.9% / 83.3% ASR / MaxN ASR on the full SafeSearch test split. We further introduce Trace-Guided Strategy Evolution (TGSE), which automatically improves attacker strategies from execution traces, replacing manual redesign with trace-driven refinement; its strongest single setting reaches 71.4% / 95.0% in held-out evaluation.

## Metadata
- **Published**: 2026-08-05T07:57:27Z
- **Authors**: Xuebin Li, Hanqing Zhao, Siyuan Liang, Kejiang Chen, Weiming Zhang, Dacheng Tao, Nenghai Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04565v1)