---
title: MemoGuard: An Adaptive Runtime for Guarding Against Memory Traps in Communication-Limited Robot Navigation
published: 2026-07-17T03:21:30Z
authors: Rajat Bhattacharjya, Hyeonjong Ju, Sing-Yao Wu, Eli Bozorgzadeh, Nikil Dutt
url: http://arxiv.org/abs/2607.15589v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MemoGuard: An Adaptive Runtime for Guarding Against Memory Traps in Communication-Limited Robot Navigation

## Abstract
Communication-limited robots in mission-critical scenarios such as disaster inspection and search-and-rescue must make reliable onboard decisions without access to remote operators or high-capacity reasoning services. Episodic memory reuse is an attractive low-cost fallback, but retrieval similarity does not guarantee execution validity, i.e., a retrieved action may match the current context yet be unsafe due to changed topology, insufficient battery margin, or unreliable prior outcomes. We call such high-similarity but execution-invalid episodes memory traps. This creates a safety-efficiency design space where similarity only reuse minimizes fallback cost but can be unsafe, while always invoking local reasoning improves safety at high computational and energy cost. This paper presents MemoGuard, a lightweight adaptive runtime that validates episodic memories against topology, resource, and outcome contracts before reuse, invoking fallback only when validation fails. In a graph-based corridor-inspection simulator, MemoGuard reduces battery safety violations by 76.6% over similarity-only top-1 reuse while reducing fallback calls by 21.4% over always reasoning. On an NVIDIA Jetson AGX Xavier with local llama3.2:3b fallback reasoning, this corresponds to 3.67 s and 36.97 J of avoided fallback-reasoning overhead per trial. We open-source MemoGuard at https://github.com/hetheiin/memoguard.

## Metadata
- **Published**: 2026-07-17T03:21:30Z
- **Authors**: Rajat Bhattacharjya, Hyeonjong Ju, Sing-Yao Wu, Eli Bozorgzadeh, Nikil Dutt
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.15589v1)