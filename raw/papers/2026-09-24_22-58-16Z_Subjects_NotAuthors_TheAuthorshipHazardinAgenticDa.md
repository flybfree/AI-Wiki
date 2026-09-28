---
title: Subjects, Not Authors: The Authorship Hazard in Agentic Dataspaces
published: 2026-09-24T22:58:16Z
authors: Seungho Lee, Changbin Lee
url: http://arxiv.org/abs/2609.30614v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Subjects, Not Authors: The Authorship Hazard in Agentic Dataspaces

## Abstract
Dataspace connectors decide whether a transfer may occur, not what the transferred value contains, tolerable for contracted applications, not for LLM agents that compose tool calls and spawn sub-agents. Research on agents that generate governance artifacts evaluates output quality; who may authorize an artifact for use falls between that literature and the governance literature, and neither owns it. A published policy is what a dataspace's decision point enforces, so publication is a governance event, and an agent that is both policy subject and policy author writes the norms that bind it. We name this the authorship hazard and state one principle: an agent is a subject of the governance plane, never an author of it. Its authorization channel to publication is closed by construction; its influence channel, drafting what humans approve, is treated as an enforcement problem. On a frozen corpus of agent drafts, publishing without approval reverses 80 authorization decisions, most through drafts that change only a field's sensitivity classification and no policy text; a classifier that reads the policy diff misses every such draft, necessarily. Treating classification as authorship routes them all to review; the registry-held classification this requires is designed and modelled here, not yet implemented in the prototype. At the execution boundary, protected fields reach the model in 105 of 105 cases under prompt-stated duties and in 0 of 105 when the ODRL duty is compiled into an invocation-time tool-call constraint, but where the value is not confined to a named field the compiled condition exposes it in 7 of 7. A centrally provisioned approval pool does not scale to the participant volume that motivates the problem.

## Metadata
- **Published**: 2026-09-24T22:58:16Z
- **Authors**: Seungho Lee, Changbin Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.30614v1)