---
title: The OCUDU dApp Platform: An Open Runtime and E3 Interface for Real-Time AI-RAN
published: 2026-09-07T18:03:21Z
authors: Timothy O'Shea, Matthew Pennybacker, Andriy Kharchenko
url: http://arxiv.org/abs/2609.07843v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The OCUDU dApp Platform: An Open Runtime and E3 Interface for Real-Time AI-RAN

## Abstract
Machine learning has shown its largest gains in the band below 10 ms inside a 3GPP new radio (NR) 5G distributed unit (DU): link adaptation, per-slot scheduling, channel estimation, and the receiver itself. No open platform has let independently built software run there. Prior dApp frameworks reached the band only as external observers of an export stream. This paper is a guided introduction to the OCUDU dApp platform, an open runtime and E3 interface under which signed AI-RAN applications execute inside a production DU under three timing contracts: resident on the GPU receive chain (Class A), inside the scheduler's 100 us admitted deadline (Class B), or as never-blocking observers whose results the scheduler consumes (Class C). The conventional path is never displaced, and every authority is typed, validated, and operator-bounded. The paper explains how the runtime, the embedded E3 agent, and the three public repositories fit together; shows a dApp's source, its signed package, and its lifecycle state machine; defines the contracts a module is written against; and shows how one management surface serves a Python script, an operator's console, and an LLM agent. On a GB10 gNB with attached handsets, dApps of all three classes, including an out-of-tree neural equalizer, ran together on a live cell without a single fallback, and equalizer variants were compared over the air by lifecycle operations alone. Every measured checkpoint is reported with its conditions and its gaps. Platform, SDK, and a zero-hardware quickstart are public under BSD-3-Clause-Clear as a preview release of the OCUDU AI-RAN Working Group 2, inviting feedback, new use cases, and independent vetting ahead of upstreaming into the OCUDU mainline.

## Metadata
- **Published**: 2026-09-07T18:03:21Z
- **Authors**: Timothy O'Shea, Matthew Pennybacker, Andriy Kharchenko
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.07843v1)