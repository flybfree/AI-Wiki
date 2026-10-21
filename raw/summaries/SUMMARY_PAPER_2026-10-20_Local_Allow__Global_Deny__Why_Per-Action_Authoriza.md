---
title: Local Allow, Global Deny: Why Per-Action Authorization Does Not Compose in LLM Agents
url: http://arxiv.org/abs/2610.27620v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-20_04-35-39Z_LocalAllow_GlobalDeny_WhyPer_ActionAuthorizationDo.md
generated_at: 2026-10-20 21:00
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper demonstrates that per-action authorization mechanisms used in LLM agent guardrails are structurally insufficient for enforcing global policies that span intent, purpose, provenance, consent, and delegation. The authors formalize Compositional Authorization Failures (CAFs)—locally authorized executions that collectively violate a global policy—and prove an impossibility result showing that relational purpose violations cannot be detected by any per-action monitor without false alarms. They provide a constructive witness generator (AL-SYNTH) and empirical evidence across nine LLM judges confirming that per-action views approve CAF witnesses while cross-execution monitoring reveals them.

## Key Takeaways
- The central impossibility result establishes that relational purpose violations form a 2-safety hyperproperty with no per-trace locus of blame. This means any per-action monitor that never raises a false alarm will detect none of these violations, regardless of the underlying model or decision procedure used. The violation only becomes visible under cross-execution monitoring, which none of the six surveyed guardrail implementations support.
- CAFs are characterized along two axes: expressiveness (single-trace safety versus relational k-safety) and observability (a ladder of monitor profiles). This taxonomy reveals that the failure is not a model-specific bug but a structural limitation of the per-action authorization paradigm itself, independent of which LLM or decision procedure is employed.
- AL-SYNTH is a SAT/SMT-based synthesizer that uses no language model and emits minimal CAF witnesses checked against an exhaustive oracle. Empirically, across nine LLM judges, the per-action view approves synthesized witnesses almost without exception—blocking them at a rate comparable to a benign control—yet the same models flag the violation when shown the two executions together, confirming the structural gap.

## Context
As autonomous LLM agents increasingly deploy tool-calling capabilities in production systems, guardrails that screen each tool invocation in isolation have become the dominant safety pattern. This paper addresses a fundamental gap in that paradigm: global policies governing multi-step agent behavior (such as purpose consistency across a chain of actions) cannot be decomposed into per-action checks. The work connects formal methods (hyperproperties, k-safety, SAT/SMT solving) with practical agent safety engineering, bridging a theoretical impossibility result to concrete guardrail implementations.

## Implications
For practitioners building LLM agent systems, this result means that current per-action guardrails provide a false sense of security: they cannot enforce relational policy conjuncts without either comparing executions across time or accepting false alarms. Industry deployments relying on single-call screening will systematically miss purpose drift, consent violations, and delegation failures that emerge only across multi-step interactions. The paper implies that robust agent safety requires architectural changes toward cross-execution monitoring or hybrid approaches that combine per-action screening with periodic relational audits.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.27620v1)
