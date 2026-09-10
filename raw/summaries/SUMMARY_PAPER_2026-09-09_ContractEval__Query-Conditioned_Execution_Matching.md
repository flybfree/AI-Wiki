---
title: ContractEval: Query-Conditioned Execution Matching for Procedural Instruction Conformance
url: http://arxiv.org/abs/2609.09458v1
type: paper-summary
date: 2026-09-09
source_paper: 2026-09-08_21-21-16Z_ContractEval_Query_ConditionedExecutionMatchingfor.md
generated_at: 2026-09-09 20:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ContractEval, a diagnostic framework that explicitly maps query‑active obligations to response or trace evidence, distinguishing procedural failures such as omissions, wrong branches, ordering errors, extra actions, invariant breaches, and output‑contract violations. On a controlled suite of audited contracts, Output‑Only and Trace‑Aware judges miss many injected structural failures, while ContractEval detects and localizes all of them under gold expected and observed graphs. LLM‑backed extraction preserves much of this signal but remains sensitive to calibration.

## Key Takeaways
- ContractEval treats procedural instructions as query‑active obligations that are matched against response or trace evidence, turning implicit conformance into explicit, localized failures.
- The framework outperforms both output‑only and trace‑aware evaluation methods by catching structural errors that these judges overlook on audited protocols.
- Although LLM extraction retains much of the diagnostic signal, its performance is still affected by calibration issues.

## Context
As large language models transition from answering questions to executing procedural tasks, failures become subtle and often invisible in final outputs. Current evaluation methods either ignore activity (output‑only) or only partially capture it (trace‑aware), leaving active obligations undetected. ContractEval addresses this gap by providing a systematic way to expose which obligations were supposed to be satisfied for each query.

## Implications
ContractEval makes procedural conformance auditable rather than an implicit assumption embedded in answer quality, enabling developers and auditors to pinpoint exact compliance issues. This shift is crucial for industries relying on automated procedural execution, such as robotics, software testing, and AI‑driven workflow orchestration, where traceable failures are essential for safety and reliability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.09458v1)
