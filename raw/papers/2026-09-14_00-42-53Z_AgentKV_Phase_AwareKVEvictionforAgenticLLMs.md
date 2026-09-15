---
title: AgentKV: Phase-Aware KV Eviction for Agentic LLMs
published: 2026-09-14T00:42:53Z
authors: Taowen Tony Liu, Jeffrey T. H. Wong, Can Xiao, Bowen Yang, Hao Mark Chen, Yiren Zhao
url: http://arxiv.org/abs/2609.14872v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AgentKV: Phase-Aware KV Eviction for Agentic LLMs

## Abstract
Agentic serving can consume orders of magnitude more tokens than chatbot workloads, stressing both KV-cache capacity and decode-time bandwidth. Most KV-eviction methods score cached keys against representative queries drawn from the most recent tokens, assuming future attention resembles recent attention. We show that agentic generation violates this assumption: future queries form a mixture over think, act, tool, and others phases, and principal-angle analysis shows these components occupy measurably different query subspaces, so recency representatives systematically undervalue keys that upcoming phases will need. We propose AGENTKV, which maintains a small query buffer per phase and scores cached keys against their union. We further implement AGENTKV in a persistent multi-turn serving path that carries compressed KV state across turns and compacts retained KV pages online. Across two models, six task domains, and three KV budgets each, AGENTKV improves task score by 5.5 points on average over R-KV and 5.3 over Tri-attention. Relative to upstream full-KV SGLang, AGENTKV improves output-token throughput by up to 1.80x. Code: https://github.com/LiuTaowen-Tony/agentkv.

## Metadata
- **Published**: 2026-09-14T00:42:53Z
- **Authors**: Taowen Tony Liu, Jeffrey T. H. Wong, Can Xiao, Bowen Yang, Hao Mark Chen, Yiren Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.14872v1)