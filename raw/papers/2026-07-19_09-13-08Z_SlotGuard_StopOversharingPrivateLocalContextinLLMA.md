---
title: SlotGuard: Stop Oversharing Private Local Context in LLM Agent Transcri
published: 2026-07-19T09:13:08Z
authors: Haocheng Xia, Yongjoo Park
url: http://arxiv.org/abs/2607.17147v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SlotGuard: Stop Oversharing Private Local Context in LLM Agent Transcri

## Abstract
LLM agents can leak privacy (e.g., paths, emails) and credentials (e.g., API keys) as agent observations (e.g., tool outputs, shell logs, and file reads) are appended to provider-bound transcripts. Existing placeholder redaction is brittle: it can miss embedded or cross-turn references, over-redact benign lookalikes, and destroy the structure useful for reasoning. We present SlotGuard, a local transcript boundary that can hide sensitive data while retaining agents' performance. SlotGuard rewrites structural bindings as typed, suffix-aware slots, replaces secrets with format-preserving synthetic values, links cross-turn references with a lightweight session graph, and restores raw values only inside the trusted runtime. On controlled repository-oriented agent transcripts, SlotGuard removes all 20,814 annotated structurally sensitive characters across 9,229 paths and reduces credential leakage to 0.0\% across 852 planted values. It remains close to raw-transcript task success across four upstream models, while generic redaction drops to 2.5\%. Transcript rewriting takes a median of 14.424~$μ$s per agent turn. The code is publicly accessible at https://github.com/illinoisdata/SlotGuard.

## Metadata
- **Published**: 2026-07-19T09:13:08Z
- **Authors**: Haocheng Xia, Yongjoo Park
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.17147v1)