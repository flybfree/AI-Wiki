---
title: Human-LLM Deliberation as Interactive Proof: Conditions for Verifiability Without Transparency
published: 2026-09-21T17:00:15Z
authors: Baotong Zhang, Dean Foster, João Sedoc
url: http://arxiv.org/abs/2609.24895v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Human-LLM Deliberation as Interactive Proof: Conditions for Verifiability Without Transparency

## Abstract
When an LLM supplies an argument that a user could not readily construct, how can the user decide whether to accept its claim? Inspired by interactive proofs, we model human-LLM deliberation as an interaction between a prover with unrestricted internal search and a resource-bounded human verifier. The verifier requests and checks supporting details without access to the LLM's internal state. Passed checks accumulate evidence toward an acceptance threshold. We prove anytime-valid soundness against adaptive provers: the probability of ever accepting a false claim is at most a chosen error level, provided the task supplies bounds on false passes and human checking errors that remain valid after every relevant history. A finite-horizon completeness bound additionally requires bounds on the adequacy of honest responses and sufficient diagnostic progress. Further checks can strengthen the evidence for acceptance, but each requires another adequate response and reliable human effort. Whether this tradeoff permits certification depends on the verifier's effort budget, cognitive load, expertise, and fatigue. We identify conditions under which the supplied bounds certify a specified sequence of local checks but not a specified global check under the same resource budgets.

## Metadata
- **Published**: 2026-09-21T17:00:15Z
- **Authors**: Baotong Zhang, Dean Foster, João Sedoc
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.24895v1)