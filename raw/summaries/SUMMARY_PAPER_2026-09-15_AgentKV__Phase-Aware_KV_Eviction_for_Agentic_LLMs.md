---
title: AgentKV: Phase-Aware KV Eviction for Agentic LLMs
url: http://arxiv.org/abs/2609.14872v1
type: paper-summary
date: 2026-09-15
source_paper: 2026-09-14_00-42-53Z_AgentKV_Phase_AwareKVEvictionforAgenticLLMs.md
generated_at: 2026-09-15 01:24
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
The paper introduces AgentKV, a phase-aware key-value eviction strategy designed to address the severe memory and bandwidth constraints inherent in agentic large language model workloads. By recognizing that agentic generation alternates between distinct cognitive phases like thinking, acting, and tool usage, the authors demonstrate that traditional recency-based KV caching fails because future queries occupy different attention subspaces than recent ones. AgentKV mitigates this by maintaining phase-specific query buffers to score cached keys against a unified representation, significantly improving both task performance and inference throughput across diverse domains and models.

## Key Takeaways
- Agentic LLM workloads generate highly heterogeneous query patterns spanning think, act, and tool phases, which occupy measurably distinct subspaces that break the recency assumption underlying most existing KV-eviction methods.
- The proposed AgentKV framework maintains a small, dedicated query buffer per phase and evaluates cached keys against their combined representation, effectively preserving context critical for upcoming cognitive stages while drastically reducing memory overhead.
- Implemented within a persistent multi-turn serving architecture that compresses and compacts KV state online, AgentKV achieves an average 5.5-point task score improvement over R-KV and boosts output-token throughput by up to 1.80x compared to full-KV baselines across multiple models and domains.

## Context
As large language models transition from static chatbots to autonomous agents capable of extended reasoning, tool use, and multi-step planning, the computational demands on KV-cache management have grown exponentially. Traditional caching strategies optimized for conversational or short-context tasks struggle with the non-stationary attention patterns characteristic of agentic workflows, creating a bottleneck that limits scalability and real-world deployment. This research addresses a critical gap in efficient LLM serving by aligning cache eviction mechanics with the actual cognitive architecture of agent-based inference.

## Implications
The introduction of phase-aware KV eviction offers practitioners a practical pathway to deploy longer-horizon agentic workflows on resource-constrained hardware without sacrificing performance. By decoupling cache retention from naive recency and instead aligning it with functional reasoning phases, organizations can significantly reduce inference costs while maintaining or improving task accuracy. This approach also informs future system-level optimizations for multi-turn agent serving, encouraging the development of adaptive memory management frameworks that dynamically respond to shifting attention distributions during complex reasoning tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.14872v1)
