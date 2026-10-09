---
title: NOMOS: Compiling Written Policies into Statically Verified Tool-Call Gates for LLM Agents
published: 2026-10-08T00:23:22Z
authors: Min-Young Yu, Tony Kim, Jang Won Choi
url: http://arxiv.org/abs/2610.11030v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# NOMOS: Compiling Written Policies into Statically Verified Tool-Call Gates for LLM Agents

## Abstract
Tool-using LLM agents violate the policies they are deployed to enforce, often silently. Prior defenses hand-write rules, query an LLM verifier per action, or compile policies through heavyweight formal machinery. Naive compilation fails: extracted rules block the tool satisfying their own precondition, or read arguments their tool lacks. NOMOS, a four-pass compiler, turns a natural-language policy into a deterministic tool-call gate; static verification with tool-schema-level checks alone (no prover, solver, or LLM) repairs or rejects 37% (airline) and 13% (retail) of candidates, without which most shipped rules are inoperable. Replaying compiled rules over undefended transcripts flags bindings that refuse legitimate work (a development binding refused 95.9% of task-passing calls); no evaluation binding is flagged. On $τ^2$-bench the gate cuts violations of reference-encoded clauses among state-changing calls from 66.3% to 2.6% (airline) and 30.8% to 6.9% (retail), raising airline task success significantly for $2 \le k \le 4$; a 26B on-premise compilation is not significantly worse than hand-written or frontier-compiled rules. Unlike AgentDojo's shipped defenses, it reaches a zero attack success rate (ASR) on banking, where nine attack families collapse onto three structural rules. On the other three suites its ASR is at most 3.6%, from goals with no tool call to govern and one write admitted by a binding weaker than its clause; a second agent model, Llama-3.3-70B, reproduces the effect on both benchmarks. Decisions take microseconds without an LLM call, at a domain-dependent benign-utility cost; compilation runs on-premise on open-weight gemma-4-26B.

## Metadata
- **Published**: 2026-10-08T00:23:22Z
- **Authors**: Min-Young Yu, Tony Kim, Jang Won Choi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.11030v1)