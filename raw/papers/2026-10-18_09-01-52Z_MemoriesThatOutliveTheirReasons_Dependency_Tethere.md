---
title: Memories That Outlive Their Reasons: Dependency-Tethered Memory for Tool-Using LLM Agents
published: 2026-10-18T09:01:52Z
authors: Yiqi Wang, Jinqian Ju, Jiaqi Zhang, Zhangkai Wu, Yiqun Duan, Zequn Sun, Taotao Cai, Mingkai Zheng
url: http://arxiv.org/abs/2610.25123v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Memories That Outlive Their Reasons: Dependency-Tethered Memory for Tool-Using LLM Agents

## Abstract
Agents now act on the Web, publishing packages, models and datasets through registry APIs, and remembering past verifications spares them the work. But a verdict rests on premises. When a signing key is revoked, everything built on it stops passing, yet the advisory names only the key, and the old verdicts of its dependents may never share a retrieval window with it. This non-locality of invalidation turns memory into a liability: in long simulated chats, an agent reading a memory of atomic facts publishes 62% of the objects whose failure lies upstream, each backed by a record that was true when written. Yet derivation is local even when invalidation is not. Tether records, at write time, the exact versions each verdict derives from, and at read time withdraws any verdict whose support has failed anywhere in the store; the agent reads the same fields as before. On Fallout, a generator of versioned worlds with hypothesis-blind simulated histories shared by every memory, Tether publishes 0.3% of upstream-failing objects across three domains when relations are stated with their verdicts, with 37% fewer verification calls than checking everything. A-Mem and Graphiti re-verify most candidates (0.83-0.86 checks per candidate), which limits their savings, yet publish 9% of upstream-failing objects; Mem0 relies on memory more and publishes 42%. Flushing every verdict on any failure is as safe as Tether but costs 32% more checks. The gain over fact memory holds with three open-weight backbones and against a whole-store window. These gains depend on capturing dependencies: when relations arrive in sessions apart from their verdicts, Tether's downstream unsafe publication rate rises to 9.4-22.1%, and a weak writer that misses edges loses safety in the same way.

## Metadata
- **Published**: 2026-10-18T09:01:52Z
- **Authors**: Yiqi Wang, Jinqian Ju, Jiaqi Zhang, Zhangkai Wu, Yiqun Duan, Zequn Sun, Taotao Cai, Mingkai Zheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.25123v1)