---
title: Beyond Natural Language: An Agent-Native Language for Autonomous Science
published: 2026-09-21T21:19:46Z
authors: Yifeng He, Jiachen Liu
url: http://arxiv.org/abs/2609.25421v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Natural Language: An Agent-Native Language for Autonomous Science

## Abstract
As autonomous AI agents take on every stage of scientific inquiry, research output is expanding far beyond human review capacity. Yet scientific communication still relies on natural-language prose: an informal medium prone to ambiguity, hidden assumptions, and untracked limitations that machines cannot reliably audit. We introduce Lara, a machine-checkable language and protocol for checking and revising support for research claims. By turning research arguments into executable artifacts, Lara provides an epistemic kernel for autonomous science: it enables automated validation pipelines for research agents, lets declared bridges connect arguments across papers into an auditable network, and allows both humans and machines to recheck the standing of an encoded claim in milliseconds. In a Lara program, authors explicitly declare their claims, supporting evidence and assumptions, and known objections or limitations. A lightweight, deterministic checker adjudicates these interactions, assigning each claim a reproducible status: "justified", "defeated", "contested", or "gap", which marks a claim whose support is incomplete and locates the unanswered question. Case studies cover empirical review, a philosophical debate without measurements, and the loss of support when an assumed axiom is withdrawn. We establish the metatheory of claim checking and cross-context argument transport, and mechanize the semantic guarantees in Lean 4 (roughly 117,000 lines), leaving three arguments on paper. The audited public metatheory is "sorry"-free and uses only Lean's three standard axioms; some executable examples additionally trust native evaluation.

## Metadata
- **Published**: 2026-09-21T21:19:46Z
- **Authors**: Yifeng He, Jiachen Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.25421v1)