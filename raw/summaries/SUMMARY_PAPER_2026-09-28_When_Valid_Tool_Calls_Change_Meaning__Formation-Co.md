---
title: When Valid Tool Calls Change Meaning: Formation-Consistent Dispatch for LLM Agents
url: http://arxiv.org/abs/2609.35088v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_13-04-04Z_WhenValidToolCallsChangeMeaning_Formation_Consiste.md
generated_at: 2026-09-28 23:07
model: qwen3.6-35b-a3b
---

## Summary
This paper addresses schema-epoch drift, a security vulnerability in LLM agents where tool calls remain schema-valid but acquire unintended effects due to changes in implementation selection during rollout or delayed approval. The authors introduce Formation-Consistent Dispatch (FCD), which connects formation analysis to execution authority by verifying that call effects align with provenance-bound summaries of official sources, ensuring consistency across source updates and retirement transitions. Experimental evaluations demonstrate that FCD successfully blocks calls with unintended public effects while preserving safe operations, outperforming static pinning or broad approval strategies in dynamic deployment scenarios.

##

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.35088v1)
