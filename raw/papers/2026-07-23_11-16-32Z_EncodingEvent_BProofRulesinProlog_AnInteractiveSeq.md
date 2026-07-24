---
title: Encoding Event-B Proof Rules in Prolog: An Interactive Sequent Prover for ProB
published: 2026-07-23T11:16:32Z
authors: Katharina Engels, Jan Gruteser, Michael Leuschel
url: http://arxiv.org/abs/2607.21191v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Encoding Event-B Proof Rules in Prolog: An Interactive Sequent Prover for ProB

## Abstract
Event-B is a formal method rooted in predicate logic and set theory. We encoded over 600 proof rules in Prolog, enabling a systematic, comprehensible proof analysis and construction. By integrating the proof rules into the Prolog-based validation tool ProB, we obtain an interactive proof system with proof tree visualisation. This has advantages in teaching, giving students direct control over the selection of proof rules. Our tool can import proof obligations from the Rodin platform and provides multiple exports: a trace file for proof replay in ProB, an interactive HTML document for tool-independent exploration of the proof tree, and an export back to Rodin, allowing the ProB prover to be used as second chain. Compared to the previous implementation of the proof rules in Java, the encoding in Prolog is more compact, maintainable and extensible. While a preliminary iterative deepening prover with simple heuristics is already available and useful for finding short proofs, we aim to obtain fast automatic provers in the future.

## Metadata
- **Published**: 2026-07-23T11:16:32Z
- **Authors**: Katharina Engels, Jan Gruteser, Michael Leuschel
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.21191v1)