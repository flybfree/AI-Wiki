---
title: Maestro: Agentic Formal Proof Development by Coordination
published: 2026-10-19T07:21:10Z
authors: Haoyu Li, Zeren Shui, Yuhao Zhang, Ferhat Erata, Benjamin Mikek, Murali Krishna Ramanathan, Hao Zhou
url: http://arxiv.org/abs/2610.25920v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Maestro: Agentic Formal Proof Development by Coordination

## Abstract
Lean is increasingly used to verify mathematical proofs and software produced by LLM agents, but writing formal proofs remains hard. Existing prover systems take a divide-and-conquer approach that recursively decomposes hard proof obligations into easier lemmas and splits again any lemma that resists proof. However, a lemma can resist proof for different reasons, including insufficient guidance, a false statement, or a flaw in the decomposition that produced it. Existing systems cannot tell these apart as a failed attempt reports little beyond its failure, and responses are confined to the failing node without considering the rest of the proof or revising the plan above it. The system may thus keep decomposing obligations along a flawed proof direction until the budget runs out, causing the whole proof attempt to fail. We introduce Maestro, a Lean prover harness that handles failures through global coordination. Provers report why they failed, not just that they failed, and a coordinator that sees the whole proof chooses an appropriate response, such as guiding a stuck prover, correcting a false lemma, or retracting a flawed subtree and replanning it. The same harness extends to verified code synthesis, where a checked counterexample sends the code back for repair. We evaluate Maestro with four frontier LLMs on seven mathematics and three software verification benchmarks. It proves more targets than each model's native coding agent (Claude Code or Codex) on every benchmark the agent has not already saturated, with the largest gains on research-level mathematics. With Claude Opus 5, it discovers its own proofs of 34 of the 48 theorems in the June 2026 release of arXivLean, against 19 for the native agent. It also outperforms all published prover systems on every benchmark they share, solving 669/672 PutnamBench, 59/60 Lean-IMO-Bench, and 6/6 IMO 2026.

## Metadata
- **Published**: 2026-10-19T07:21:10Z
- **Authors**: Haoyu Li, Zeren Shui, Yuhao Zhang, Ferhat Erata, Benjamin Mikek, Murali Krishna Ramanathan, Hao Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.25920v1)