---
title: Cognitive Admission Control: Risk-Conditioned Assurance for Consequential Actions in Agentic Distributed Systems
published: 2026-09-14T20:20:54Z
authors: Jun He, Deying Yu
url: http://arxiv.org/abs/2609.16313v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cognitive Admission Control: Risk-Conditioned Assurance for Consequential Actions in Agentic Distributed Systems

## Abstract
In agentic distributed systems, an agent may be authorized to mutate external infrastructure while lacking evidence that the mutation is ready to execute. Cognitive Admission Control (CAC) makes this evidence requirement explicit. A policy maps a typed action and its modeled risk to assurance obligations specifying predicates, evidence classes, scope, freshness, and witness-set constraints. A deterministic evaluator distinguishes satisfied, violated, and unresolved obligations; unresolved conditions produce targeted evidence-acquisition requests. Successful admission produces a certificate binding the action, its witness manifest, and dispatch-time guards.   We formalize the admission calculus and the assumptions connecting it to mediated execution. The guarantees are policy-relative: physical safety additionally requires sound evidence, an adequate environment model, and preservation of relevant conditions through the effect. A TypeScript prototype is evaluated in 2,730 controlled local trials with independent effect observation and matched fault schedules. Across 390 CAC trials, 120 effects complete without modeled harm and no harmful effects occur. A live-policy baseline achieves the same completion count but admits the constructed correlated-witness failure. Mechanism ablations isolate guard, evidence-class, structural-cut, and remediation behavior. A further 9,000 measurements exercise the complete local dispatch path with persistent replay protection. These results establish tested implementation behaviors and local costs, not production failure rates or comparisons of language-model capability.

## Metadata
- **Published**: 2026-09-14T20:20:54Z
- **Authors**: Jun He, Deying Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.16313v1)