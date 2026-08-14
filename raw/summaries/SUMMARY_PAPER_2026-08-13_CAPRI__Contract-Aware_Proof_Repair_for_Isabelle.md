---
title: CAPRI: Contract-Aware Proof Repair for Isabelle
url: http://arxiv.org/abs/2608.13459v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_16-43-44Z_CAPRI_Contract_AwareProofRepairforIsabelle.md
generated_at: 2026-08-13 22:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CAPRI, a contract-aware proof repair workflow for Isabelle that ensures repairs respect developer‑authorized changes. It evaluates five repair mechanisms on twelve failed proofs and finds most produce valid repairs without violating protected text contracts. The best results come from proof-body-only interfaces and later frozen iterative workflows.

## Key Takeaways
- CAPRI retains prompts, proposals, candidate repositories, diagnostics, verdicts, and hashes to provide an audit trail for any edit made during the repair process.
- All six terminal candidates that violated protected text arose only in iterative workflows capable of editing a complete theory, indicating that full‑theory edits are unsafe under current safeguards.
- The proof-body-only interface achieved 29 valid repairs out of 36 with zero contract violations, while the full-theory variant produced 31/36 but still had one violation.

## Context
This work addresses a key limitation in automated theorem proving where large language models can generate proofs that are syntactically correct yet modify protected sections without developer consent. By embedding machine‑readable edit contracts within Isabelle, CAPRI bridges the gap between proof generation and trustworthy modification.

## Implications
For practitioners developing formal verification tools, CAPRI demonstrates a practical method to integrate AI assistance while preserving security guarantees. The findings suggest that body-only repairs are preferable when only theorem content needs fixing, reducing risk of unintended changes in complex theories.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13459v1)
