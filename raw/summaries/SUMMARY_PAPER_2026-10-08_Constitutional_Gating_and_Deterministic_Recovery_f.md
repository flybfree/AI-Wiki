---
title: Constitutional Gating and Deterministic Recovery for Multi-Agent LLM Negotiation: Ablations Against a Stateful Adversarial Gatekeeper
url: http://arxiv.org/abs/2610.11542v1
type: paper-summary
date: 2026-10-08
source_paper: 2026-10-08_09-10-45Z_ConstitutionalGatingandDeterministicRecoveryforMul.md
generated_at: 2026-10-08 21:43
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper evaluates a three-part control stack—comprising a 5-Pillar runtime constitution, a 4-tier agent swarm, and a deterministic deadlock-recovery mechanism called Cognitive Annealing—designed to reduce wasted model calls in multi-agent LLM negotiation systems. Through 30 controlled runs against a fixed-rule adversarial Gatekeeper, the authors demonstrate that while the constitution and Director enable acceptable framing, they do not guarantee reliable negotiation success; however, the deterministic atomic purge and canonical recovery message achieve 5-of-5 deadlock escapes versus 0-of-5 for LLM-only steering, at zero additional model-call cost.

## Key Takeaways
- The constitution and Director components make an acceptable negotiation framing possible but unreliable: baseline configurations achieved 0/5 unlocks, while constitution-augmented runs reached only 1/5 or 2/5. When the swarm did succeed, it unlocked in a single turn using 7–8 calls and roughly 15k tokens, representing a 67–73% reduction below baseline cost; when it failed, it incurred 17–38% more cost than baseline.
- The Monitor and schema hard gate did not reduce unlock rates but produced an audit trail, and critically, LLM-written recovery strikes failed the deterministic pre-flight check 5 out of 5 times even though an LLM Monitor had approved four of them—highlighting a fundamental gap between LLM judgment and deterministic validation.
- Under a honeytrap-to-compliance deadlock scenario, the deterministic Cognitive Annealing mechanism (atomic purge of agent-side context plus a canonical strike message) escaped deadlock in 5 of 5 runs versus 0 of 5 for LLM-only steering, with a Fisher exact test p-value of 0.008, all at the same call budget and with zero model calls consumed by the recovery strike itself.

## Context
Multi-agent LLM systems increasingly face adversarial or stateful counterparts in negotiation, compliance, and safety-critical workflows, where polite loops, malformed outputs, and compliance deadlocks silently consume large token budgets. This paper addresses a practical engineering problem in the growing field of agentic AI orchestration: how to impose deterministic control structures that bound cost and guarantee recovery without relying on the very LLM reasoning that caused the failure in the first place. The use of a fixed-rule Gatekeeper with known acceptance conditions makes the testbed reproducible and shifts evaluation from discovery to execution fidelity.

## Implications
For practitioners building multi-agent pipelines, the findings argue that deterministic recovery mechanisms—atomic context purges and canonical messages—outperform LLM-generated steering in deadlock situations while adding zero marginal model cost, suggesting that safety-critical recovery paths should be hard-coded rather than delegated to model reasoning. The failure of LLM-written strikes to pass deterministic pre-flight checks despite LLM Monitor approval underscores a broader caution: LLM self-evaluation cannot substitute for schema-level validation in production agent systems. Industry deployments of agentic negotiation should prioritize bounded-cost architectures with deterministic stop rules and audit trails over open-ended LLM steering loops.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.11542v1)
