---
title: When Context Changes: Understanding Update Failures in LLMs
url: http://arxiv.org/abs/2609.38866v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_03-19-14Z_WhenContextChanges_UnderstandingUpdateFailuresinLL.md
generated_at: 2026-09-30 20:41
model: qwen3.6-35b-a3b
---

## Summary
This paper investigates "stale binding," a failure mode where large language models answer using outdated information even when updated context is present in the conversation. The authors introduce Controlled In-Context Memory (CICM) to benchmark this issue and identify "attention drift" as the underlying mechanism, where attention scores favor accumulated old values over the current update. They demonstrate that mathematical analysis of a one-layer transformer reveals how similar attention scores allow multiple old values to dominate the current one, and propose an untrained intervention that

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.38866v1)
