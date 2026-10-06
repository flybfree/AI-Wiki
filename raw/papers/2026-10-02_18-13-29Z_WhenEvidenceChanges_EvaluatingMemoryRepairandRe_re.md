---
title: When Evidence Changes: Evaluating Memory Repair and Re-reading in Language-Model Agents
published: 2026-10-02T18:13:29Z
authors: Wenhui Chu
url: http://arxiv.org/abs/2610.03902v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Evidence Changes: Evaluating Memory Repair and Re-reading in Language-Model Agents

## Abstract
When documents supporting an agent's derived facts are revoked or replaced, should it repair memory or re-read current evidence? We introduce an evidence-revision evaluation on medication- and problem-list tasks from public ICU records. Under revocation, replacement and control events, we compare full and source-filtered re-reading with caching, rebuilding and graph-local repair across two 7B models. Memory is supplied in full without retrieval, and costs include ingest, revision and every use. On short records, local repair uses 5-10$\times$ fewer revision tokens than rebuilding, yet every memory pipeline costs at least twice full re-reading in held-out conditions. In a small pre-specified development sweep, adding task-ineligible documents extended records to about 10,000 tokens; at that length, memory's mean cumulative cost fell below full re-reading's after 2-14 uses, partly through truncated extraction, while source-filtered re-reading remained cheapest. In the replacement study, none of the four primary confirmatory tests reached statistical significance. These results show why the cost of agent memory after evidence revision must be assessed against source-filtered re-reading over the full pipeline.

## Metadata
- **Published**: 2026-10-02T18:13:29Z
- **Authors**: Wenhui Chu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.03902v1)