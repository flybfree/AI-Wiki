---
title: Cross-Agent Campaign Attribution: Linking Asynchronous Attacks Across LLM Agents
published: 2026-07-21T08:01:51Z
authors: SangJin Park, Myungsub Choi, Jineok Kim, Minseung Kang
url: http://arxiv.org/abs/2607.18826v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cross-Agent Campaign Attribution: Linking Asynchronous Attacks Across LLM Agents

## Abstract
LLM-agent defenses are typically evaluated one session at a time. In deployment, however, attacks can be distributed across independent agents, teams, and runtimes, leaving each local guardrail with only a sparse fragment. We formalize cross-agent asynchronous campaign attribution: linking sessions from the same latent adversarial campaign without shared runtime state, test-time campaign labels, or attacker identity oracles. We introduce Asynchronous Attribution Fingerprint Vectors ($A^2FV$), a lightweight proxy-side reference protocol for scoring pairwise campaign similarity from proxy-observable tool-use, timing, and prompt residue. We also construct SCD-v1, a controlled persona-matched benchmark with benign traffic, isolated attacks, multi-session campaigns, matched non-oracle evasion, and leakage audits. On SCD-v1, $A^2FV$ achieves 0.82 pairwise AUC for campaign linking, while score-only adaptations of per-session detectors and chunked LLM judges remain near chance under the same task. The strongest fixed signal is carried by structural and stylometric residue, while timing is retained as a diagnostic channel for richer proxy traces. Crossed-style controls show that the signal is partly style-sensitive but not reducible to style alone. Static and dimension-aware non-oracle stress tests further show that pairwise separability persists under controlled evasion. These results establish cross-agent campaign attribution as a distinct evaluation layer for securing LLM agents in the wild.

## Metadata
- **Published**: 2026-07-21T08:01:51Z
- **Authors**: SangJin Park, Myungsub Choi, Jineok Kim, Minseung Kang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18826v1)