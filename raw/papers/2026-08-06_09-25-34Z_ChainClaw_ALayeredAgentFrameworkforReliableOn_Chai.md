---
title: ChainClaw: A Layered Agent Framework for Reliable On-Chain Execution
published: 2026-08-06T09:25:34Z
authors: Jiacheng Wei, Zhaoxin Fan, Xin Wen, Yuqin Lan, Dongrun Li, Wenjun Wu, Faguo Wu, Xiao Zhang
url: http://arxiv.org/abs/2608.05790v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ChainClaw: A Layered Agent Framework for Reliable On-Chain Execution

## Abstract
General-purpose large language model agents have achieved strong performance on tool-augmented tasks, yet they rely on assumptions break down in blockchain environments. On-chain execution is stateful, adversarial, and economically irreversible, exposing three fundamental gaps: Reactivity, Irreversibility, and Observability. We propose ChainClaw, a blockchain-native agent framework built on OpenClaw, that addresses all three gaps through a layered architecture comprising an event-driven orchestration layer, a simulation-based safety intelligence layer, and an on-chain monitoring runtime layer, unified by a cross-layer memory subsystem. ChainClaw closes the Reactivity gap via event ingestion and simulation feedback, the Irreversibility gap via a pre-execution safety pipeline with transaction simulation and action guard, and the Observability gap via an on-chain read adapter and transaction monitor. We evaluate ChainClaw on a purpose-built benchmark covering seven tasks across four categories and five dimensions. ChainClaw consistently outperforms representative baselines on both safety and task completion.

## Metadata
- **Published**: 2026-08-06T09:25:34Z
- **Authors**: Jiacheng Wei, Zhaoxin Fan, Xin Wen, Yuqin Lan, Dongrun Li, Wenjun Wu, Faguo Wu, Xiao Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05790v1)