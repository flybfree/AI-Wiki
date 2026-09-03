---
title: ClaimReceipt: Verifying Evidence Sufficiency and Coverage in Agent Evaluations
url: http://arxiv.org/abs/2609.01992v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_02-00-02Z_ClaimReceipt_VerifyingEvidenceSufficiencyandCovera.md
generated_at: 2026-09-02 20:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces ClaimReceipt, a specification‑based verifier that checks whether evidence is sufficient for a claim and whether the retained records cover the committed experiment set. On historical data it reproduces all audit verdicts with zero false positives, and in a prospective test it matches preregistered predictions when omissions are introduced. The verification adds only 0.021% of inference time.

## Key Takeaways
- CR‑2 reproduces every manually labeled audit verdict on 1,392 records, proving both sufficiency and coverage checks work correctly.
- Withholding a terminal receipt yields INCONCLUSIVE_COVERAGE while withholding all private openings keeps protocol verification but makes economic claims inconclusive, matching predictions.
- The verifier’s runtime impact is negligible (0.021% of model inference) and storage overhead is minimal (9.9 KB per transaction).

## Context
Agent evaluations often rely on generic logs that cannot reliably answer evidentiary questions, leading to ambiguous audit outcomes. This work provides a concrete framework for linking evidence to claims in AI‑driven systems.

## Implications
For practitioners, ClaimReceipt offers a lightweight tool to ensure trustworthy claim verification without sacrificing performance. The methodology can be adopted across industries where evidence integrity is critical, such as finance and e‑commerce.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01992v1)
