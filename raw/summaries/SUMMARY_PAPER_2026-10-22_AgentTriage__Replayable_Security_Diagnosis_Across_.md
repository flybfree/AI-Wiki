---
title: AgentTriage: Replayable Security Diagnosis Across Heterogeneous Agent Runtimes
url: http://arxiv.org/abs/2610.30738v1
type: paper-summary
date: 2026-10-22
source_paper: 2026-10-22_05-09-44Z_AgentTriage_ReplayableSecurityDiagnosisAcrossHeter.md
generated_at: 2026-10-22 21:28
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
AgentTriage introduces an executable contract framework for performing replayable security diagnosis across heterogeneous tool-use agent runtimes, addressing the critical gap where agent final responses fail to explain the security events triggered by file writes, code execution, or data transmission. The system normalizes native runtime observations through overlays, constructs typed provenance graphs, and binds diagnostic claims to recorded evidence, achieving 0.858 grounded joint diagnosis accuracy and 0.966 required-evidence coverage across 120 adjudicated cases spanning five distinct runtimes.

## Key Takeaways
- AgentTriage defines a formal contract that admits conclusions only when claims cite canonical runtime events and mandates abstention whenever mandatory evidence is missing, ensuring that diagnoses are grounded in observable, verifiable traces rather than speculative reasoning. This deterministic pipeline joins invocation and result lifecycles, constructs a typed provenance graph, selects a policy-decisive slice, and binds claims to recorded evidence, enabling recomputation without language-model judgment.
- The system demonstrates cross-runtime generalization by capturing all 159 applicable executions across five heterogeneous runtimes under a single contract, with runtime overlays normalizing native observations and an audit of both native and synthesized identifiers ensuring trace integrity. This unified approach eliminates the fragmentation caused by incompatible interfaces across different agent execution environments.
- Quantitative evaluation on 120 adjudicated cases shows AgentTriage achieves a 0.036 unsupported-claim rate and improves joint diagnosis by 0.175 (95% CI [0.092, 0.258]) over the strongest same-schema baseline, providing measurable bounds on diagnostic precision and clearly delineating observation boundaries that require abstention rather than inference.

## Context
As AI agents increasingly interact with external tools, file systems, code execution environments, and data pipelines, the security implications of their actions extend far beyond what their textual responses convey. Existing monitoring approaches struggle because each runtime exposes security-relevant events through proprietary, incompatible interfaces, making cross-platform diagnosis intractable. AgentTriage addresses this fragmentation by formalizing a replayable diagnostic contract that operates independently of any specific runtime's native format, representing a shift from post-hoc LLM-based interpretation toward deterministic, evidence-bound security auditing.

## Implications
For practitioners deploying agent systems in production, AgentTriage provides a reproducible audit mechanism that allows security teams to recompute diagnoses from recorded traces without relying on language-model judgment, reducing both operational cost and the risk of hallucinated security conclusions. The open-source implementation and sanitized evidence release enable the broader community to validate, extend, and adapt the contract to new runtimes, establishing a foundation for standardized security auditing in heterogeneous agent ecosystems. The explicit abstention mechanism also sets a practical boundary for what automated diagnosis can and cannot claim, guiding policy design around evidence availability rather than model confidence.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.30738v1)
