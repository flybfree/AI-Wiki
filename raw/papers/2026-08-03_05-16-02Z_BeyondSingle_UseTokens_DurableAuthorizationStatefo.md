---
title: Beyond Single-Use Tokens: Durable Authorization State for Replay-Resistant LLM Agent Actions
published: 2026-08-03T05:16:02Z
authors: Jinghan Xu, Longze Fan, Zeyuan Wang, Xinjin Li, Hankai Liu
url: http://arxiv.org/abs/2608.01710v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Single-Use Tokens: Durable Authorization State for Replay-Resistant LLM Agent Actions

## Abstract
Tool-using large language model agents frequently replan, retry failed operations, delegate tasks, and resume after crashes. These behaviors can cause one user authorization to be requested and executed multiple times under freshly issued token identifiers, even when each individual token is single-use. We call this failure semantic replay: exceeding the execution budget of a token-independent authorization instance rather than merely reusing an old token identifier. We show that identifier-local token consumption cannot prevent fresh reissuance unless the issuer retains monotonic durable state over the authorized action, confirmation event, and remaining execution budget. We introduce CapLease, an authorization-consumption layer that follows proposal- and authority-level defenses, binds an authenticated user confirmation to a canonical action, and enforces transactional Issue-Prepare-Commit transitions. Across LLM-agent replanning, retry, delegation, concurrency, confirmation-replay, and crash-recovery scenarios, identifier-local tokens permit fresh semantic reissuance, whereas CapLease and an equally stateful Server Ledger prevent duplicate admission and, with an idempotent sink, duplicate external effects. Our results identify durable authorization state, rather than token representation alone, as the systems requirement for replay-resistant agent execution.

## Metadata
- **Published**: 2026-08-03T05:16:02Z
- **Authors**: Jinghan Xu, Longze Fan, Zeyuan Wang, Xinjin Li, Hankai Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01710v1)