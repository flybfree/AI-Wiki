---
title: From Errors to Proofs: Minimal-Core-Guided Repair for Neuro-Symbolic Constraint Solving
published: 2026-08-14T14:48:36Z
authors: Dipankar Sarkar
url: http://arxiv.org/abs/2608.14771v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Errors to Proofs: Minimal-Core-Guided Repair for Neuro-Symbolic Constraint Solving

## Abstract
Making language models solve constraint problems reliably often means having them translate the problem into a formal specification and delegating the search to a sound solver. But the translation is itself a language-model task, and an unfaithful translation makes the solver faithfully solve the wrong problem. Existing pipelines repair only translations that crash, returning the solver's error message and falling silent when the program runs but is wrong. We replace the error message with a proof: when the generated program is unsatisfiable, we extract a minimal unsatisfiable core over the model's own constraints and hand it back the exact set that cannot hold together, a leakage-free signal that localizes the fault. On a new benchmark of 77 problems with an exact oracle, translation to Answer Set Programming is faithful on six of seven domains and fails only on aggregate coverage scheduling, which concentrates the translation tax in one diagnosable pattern. A minimal core, rather than a bare error, is what stops a weaker model from fabricating solutions to infeasible problems, cutting fabrication from 79% to 7%. A strong chain-of-thought baseline meanwhile matches the symbolic route on accuracy, so the route's value is not accuracy but certificates and its refusal to fabricate.

## Metadata
- **Published**: 2026-08-14T14:48:36Z
- **Authors**: Dipankar Sarkar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14771v1)