---
title: AgentKV: Phase-Aware KV Eviction for Agentic LLMs
url: http://arxiv.org/abs/2609.14872v1
type: paper-summary
date: 2026-09-14
source_paper: 2026-09-14_00-42-53Z_AgentKV_Phase_AwareKVEvictionforAgenticLLMs.md
generated_at: 2026-09-14 22:23
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
This paper introduces AgentKV, a novel KV eviction strategy designed to address the severe token consumption and bandwidth constraints inherent in agentic LLM workloads. The authors demonstrate that traditional recency-based eviction methods fail for agents because future queries span distinct semantic phases like thinking, acting, and tool usage, which occupy different query subspaces rather than resembling recent attention patterns. AgentKV overcomes this by maintaining phase-specific query buffers to score cached keys against a unified representation, significantly improving task performance and output throughput compared to existing baselines.

## Key Takeaways
- Agentic generation violates the standard assumption that future attention resembles recent attention; principal-angle analysis reveals that queries form a mixture over think, act, and

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.14872v1)
