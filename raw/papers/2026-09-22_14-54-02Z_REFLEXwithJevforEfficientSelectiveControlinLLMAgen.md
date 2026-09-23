---
title: REFLEX with Jev for Efficient Selective Control in LLM Agents
published: 2026-09-22T14:54:02Z
authors: Tiantong Wu, Wei Yang Bryan Lim
url: http://arxiv.org/abs/2609.26532v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# REFLEX with Jev for Efficient Selective Control in LLM Agents

## Abstract
LLM agents often use generative models for bounded decisions, raising the question of when these decisions can be handled more efficiently without reducing task success. We study REFLEX, an agent architecture that uses Jev as a fast, typed decision layer and calls a strong LLM when confidence is low, or generation is required. On a frozen 100-task benchmark, REFLEX achieves 95% success with 72.7% fewer strong-model calls than a strong-only agent, with reductions persisting across three fallback families. Controlled interventions show that reliability depends on action-set size and near-valid alternatives near authorization boundaries. External BFCL and $τ$-style evaluations reveal limited advantages over a cheap generative cascade when ordinary routing is already highly accurate. These findings identify when selective control with Jev can reduce computation and where its benefits are limited.

## Metadata
- **Published**: 2026-09-22T14:54:02Z
- **Authors**: Tiantong Wu, Wei Yang Bryan Lim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.26532v1)