---
title: When Agents Talk, Secrets Travel: Topology-Driven Leakage and Recipient-Conditioned Sanitization in Multi-Agent LLM Systems
published: 2026-10-12T01:23:51Z
authors: Sunday Oyinlola Ogundoyin, Muhammad Ikram
url: http://arxiv.org/abs/2610.16039v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Agents Talk, Secrets Travel: Topology-Driven Leakage and Recipient-Conditioned Sanitization in Multi-Agent LLM Systems

## Abstract
Multi-agent LLM systems (MALS) introduce a privacy-leakage problem that conventional sensitivity-based defenses miss, since information disclosed to one authorized agent can propagate through routine coordination to an unauthorized one, without compromise or malicious behavior. This motivates topology-aware enforcement that blocks unauthorized propagation while preserving authorized disclosure. We evaluate 485 scenarios across coordinator-worker, peer-to-peer, and hierarchical topologies, instrumenting seven communication channels and measuring surface leakage and disclosure to topology-introduced recipients. We introduce RECONS, a Detect -> Decide -> Transform sanitizer conditioning intervention on recipient and execution context rather than sensitivity alone. Topology changes where protected information propagates, with disclosure to topology-introduced recipients rising from 0% to 52.2% while surface leakage stays nearly flat at 60.6-62.8%. This effect persists across four generator models and a second orchestration framework, though magnitude and relay paths differ; framework choice separately drives a 150x leakage spread, so topology alone is not sufficient. RECONS reduces residual disclosure from 96.7% without sanitization to 29.25%, preserving 94.1% of authorized disclosures versus 20.5% under blanket redaction. Detection coverage is the dominant bottleneck, accounting for 95.5% of residual disclosures. These results show that privacy enforcement in MALS must reason about the recipient and communication path realized at runtime, not sensitivity or topology assumptions alone.

## Metadata
- **Published**: 2026-10-12T01:23:51Z
- **Authors**: Sunday Oyinlola Ogundoyin, Muhammad Ikram
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.16039v1)