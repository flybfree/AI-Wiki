---
title: Semantics Delivery Network: Rethinking Web Retrieval Infrastructure for LLM Agents
published: 2026-09-18T18:49:38Z
authors: Peichun Hua, Yunming Xiao
url: http://arxiv.org/abs/2609.22486v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Semantics Delivery Network: Rethinking Web Retrieval Infrastructure for LLM Agents

## Abstract
Large language models (LLMs) increasingly rely on external sources when answering questions that require proprietary information or up-to-date live web content, through both traditional single-shot retrieval-augmented generation (RAG) and multi-turn agentic RAG. Yet today's web infrastructure is still built for human clients. Given a query, current search services return a list of URLs and snippets ranked for generic relevance; content delivery networks (CDNs) cache URL-addressed objects (texts, images, videos, etc.) without knowing which passage an agent needs. LLMs, in contrast, consume short, semantically coherent passages, hereafter "chunks", selected for downstream task utility rather than similarity alone, and may retrieve statefully across reasoning turns. Uncoordinated agents also repeat search, data acquisition, and semantic processing, duplicating work that could be shared. We argue that semantic chunk retrieval should become a first-class network-delivery abstraction. We propose Semantics Delivery Network (SemDN): an origin-authorized, hierarchical edge substrate that indexes, searches, and smart-caches web content at chunk granularity. SemDN serves agents on behalf of participating websites, amortizes data acquisition and processing across agents, and supports tenant-specific retrieval policies. Because, unlike URL caching, semantic retrieval provides no explicit miss signal, SemDN must estimate when its enrolled corpus may be incomplete or stale and trigger scoped discovery or refresh. It raises open questions about shareable retrieval state, hierarchical caching, coverage risk, and deployment. Our preliminary probes reveal a large gap between page content processed and chunks consumed, substantial task-local reuse, and higher answer quality per context token from chunk delivery.

## Metadata
- **Published**: 2026-09-18T18:49:38Z
- **Authors**: Peichun Hua, Yunming Xiao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.22486v1)