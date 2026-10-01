---
title: Janus: Evidence-Before-Effect Sagas and Offline-Verifiable Provenance for Agentic LLMs
url: http://arxiv.org/abs/2609.38266v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-29_13-57-51Z_Janus_Evidence_Before_EffectSagasandOffline_Verifi.md
generated_at: 2026-09-30 21:04
model: qwen3.6-35b-a3b
---

## Summary
Janus presents a provenance framework for agentic LLMs that enforces evidence-before-effect verification by maintaining a signed, hash-chained log of proposals, validator verdicts, and human approvals prior to executing actions or releasing effects. The system employs deterministic validators and offline-verifiable audits to ensure model outputs strictly adhere to policy constraints, demonstrating in lending workflow experiments that it can prevent unauthorized financial approvals even when models attempt to bypass mandates or manipulate declared amounts through understatement attacks.

## Key Takeaways
- Janus restructures agent verification by placing the record on the effect path rather than relying on post-hoc traces; every step's proposal, verdict, and signed answer from validators or humans must be durably logged in a hash-chained

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.38266v1)
