---
title: Before Reasoning Fails: Pre-Evidence Procedural Failures in Agentic RAG
published: 2026-08-03T10:09:19Z
authors: Daeyoung Roh, Donghee Han
url: http://arxiv.org/abs/2608.02011v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Before Reasoning Fails: Pre-Evidence Procedural Failures in Agentic RAG

## Abstract
Agentic retrieval-augmented generation (RAG) systems can fail before evidence-conditioned reasoning is tested: an agent may retrieve candidate snippets but finalize without inspecting them. We study this failure mode as a procedural property of the agent trajectory, decomposing wrong answers into pre-evidence discipline failures and post-gold-read failures using saved tool-call traces, retrieved evidence, read passages, and final answers. Across 12,000 paired trajectories on HotpotQA, 2WikiMultiHopQA, and MuSiQue, the two failure types are largely non-redundant: the both-trigger rate is in [11.2%, 13.1%] across regex and spaCy entity extractors. We then evaluate Read-Gate, a minimal runtime invariant requiring an agent to read after search and before finalization. Forced reading improves LLM-Acc by 14.9-19.9 points on trajectories that would otherwise skip reading and by 3.2-9.4 points on full minimal-reasoning cells. Additional diagnostics show that larger hidden thinking budgets do not necessarily increase evidence inspection. Together, these results indicate that evidence-gathering should be evaluated as a trajectory-level control problem, separately from answer-side reasoning.

## Metadata
- **Published**: 2026-08-03T10:09:19Z
- **Authors**: Daeyoung Roh, Donghee Han
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02011v1)