---
title: Encoding Event-B Proof Rules in Prolog: An Interactive Sequent Prover for ProB
url: http://arxiv.org/abs/2607.21191v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_11-16-32Z_EncodingEvent_BProofRulesinProlog_AnInteractiveSeq.md
generated_at: 2026-07-23 22:34
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper presents a Prolog encoding of over six hundred Event-B proof rules and integrates them into the ProB tool to create an interactive sequent prover. The system supports proof analysis, construction, and visualisation through a tree representation. It can import obligations from Rodin and export traces, HTML documents, or back to Rodin.

## Key Takeaways
- Over six hundred Event-B proof rules are encoded in Prolog, making the rule set compact, maintainable, and extensible compared with earlier Java implementations.
- The interactive prover allows users to select proof steps directly, providing a transparent learning experience for students.
- Export options include trace files for replay in ProB, an HTML document for tool‑independent exploration, and back‑compatibility with Rodin.

## Context
Event-B is a formal verification method that translates natural language specifications into predicate logic. Traditional implementations rely on heavyweight Java frameworks, limiting accessibility. This Prolog approach aligns with the trend toward lightweight, rule‑based AI tools that can be integrated into existing workflows without large infrastructure changes.

## Implications
For educators, the interactive prover lowers barriers to proof construction and deepens understanding of logical reasoning. For industry practitioners, embedding such a system within ProB enables rapid validation of complex specifications while preserving traceability across verification pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21191v1)
