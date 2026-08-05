---
title: DP-MemView: A Memory Interface for Attribute-Level Transcript Privacy in Long-Term LLM Agents
published: 2026-08-04T05:00:10Z
authors: Jong Wook Kim, Byoungjae Min, Kennedy Edemacu, Yoonhyuk Choi, Sae-Hong Cho, Beakcheol Jang
url: http://arxiv.org/abs/2608.03130v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DP-MemView: A Memory Interface for Attribute-Level Transcript Privacy in Long-Term LLM Agents

## Abstract
Long-term memory enables persistent personalization in LLM agents, but repeated memory-conditioned responses can cumulatively reveal protected attributes even when they are never stated explicitly. We formalize this threat as adaptive transcript privacy and introduce DP-MemView, a differentially private interface that privately selects public response-conditioning views and exposes those views---rather than raw memory---to the response LLM. Each private selection is charged to every protected attribute whose memory group intersects the read set. Per-attribute ledgers block any selection that would exceed its cap and return a fixed generic view instead. Under an explicit interface contract, we prove pure B_a-DP for the entire adaptive transcript. We also extend the result to stores that differ across multiple protected groups and bound how much observing the transcript can change an adversary's prior odds. We evaluate the online and preallocated modes with three response LLMs on a controlled adjacent-store benchmark and a public-corpus transfer track. Both modes keep transcript distinguishability near chance while preserving target-required personalization and overall response quality. Further diagnostics show that removing key safeguards causes mismatched output support, missing ledger charges, revealing side channels, or growing long-horizon leakage.

## Metadata
- **Published**: 2026-08-04T05:00:10Z
- **Authors**: Jong Wook Kim, Byoungjae Min, Kennedy Edemacu, Yoonhyuk Choi, Sae-Hong Cho, Beakcheol Jang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03130v1)