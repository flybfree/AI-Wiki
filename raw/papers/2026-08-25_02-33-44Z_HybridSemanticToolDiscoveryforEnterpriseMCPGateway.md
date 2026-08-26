---
title: Hybrid Semantic Tool Discovery for Enterprise MCP Gateway: Architecture and Implementation
published: 2026-08-25T02:33:44Z
authors: Olympia Saha, Amy Wang, Srinivasan Manoharan
url: http://arxiv.org/abs/2608.23992v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hybrid Semantic Tool Discovery for Enterprise MCP Gateway: Architecture and Implementation

## Abstract
Large language model (LLM) agents invoke external tools to retrieve and reason over information beyond pretrained knowledge. The Model Context Protocol (MCP) standardizes how such tools are surfaced, and a proxy MCP server aggregates many backend servers behind a single endpoint providing a secure, governable chokepoint for authentication, policy enforcement, and observability. This architecture creates two compounding challenges: a context-engineering bottleneck where full tool schemas saturate the model context window before any user query, and a tool discoverability barrier where users and agents cannot identify the best tool among 2,000+ indexed tools across 200+ MCP servers. Prompt caching reduces reprocessing cost but neither frees context capacity nor improves accuracy. We present SCOUT (Selective Context Optimization for Universal Tooling), which reframes tool exposure as a context-selection problem, injecting only tools relevant to the current step. SCOUT surfaces two MCP meta-tools -- tool_search and execute_tool -- where tool_search performs hybrid retrieval, fusing BM25 sparse matching with dense vector search via Reciprocal Rank Fusion to return the top-k relevant tools. Backed by zero-downtime catalog update pipelines, SCOUT resolves both context saturation and tool discovery challenges. In production at PayPal, SCOUT reduces MCP tool-token consumption from 140.2k tokens (70.1% of context) to 1.3k tokens (0.8%), a 99% reduction, cutting per-query inference cost at enterprise scale. Because SCOUT is surfaced as standard MCP tools, it is model-agnostic and requires no client-side modifications.

## Metadata
- **Published**: 2026-08-25T02:33:44Z
- **Authors**: Olympia Saha, Amy Wang, Srinivasan Manoharan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23992v1)