---
title: GANDR: Claim Auditing for Verifiable Legal Answer Generation
url: http://arxiv.org/abs/2609.10293v1
type: paper-summary
date: 2026-09-09
source_paper: 2026-09-09_15-08-09Z_GANDR_ClaimAuditingforVerifiableLegalAnswerGenerat.md
generated_at: 2026-09-09 20:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces GANDR, a two‑agent framework that separates answer drafting from claim auditing in legal reasoning. The system produces per‑claim audit traces and enforces strict citation resolution, achieving 70.8 % strict accuracy on a benchmark while outperforming baselines by over eleven points.

## Key Takeaways
- GANDR’s two‑agent design creates a drafter that writes structured answers and a critic that audits each claim against its source, producing detailed audit traces.
- The system requires every citation to resolve to the exact passage retrieved, which yields 70.8 % strict accuracy on the legal benchmark.
- Reversing the protocol‑anchored commit rule drops strict accuracy by 22.7 points, highlighting the importance of the commit rule for verification.

## Context
Current grounded‑generation models evaluate answers holistically, allowing fabricated citations to pass as correct. Legal domains demand per‑claim verification because a single false claim can mislead practitioners. GANDR addresses this gap with a rigorous audit protocol and strict correctness criteria.

## Implications
For legal AI tools, GANDR demonstrates that separating drafting from verification improves reliability and trustworthiness. Practitioners can rely on the system’s audit traces to identify under‑supported claims, reducing risk of misinformation in high‑stakes decision making.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.10293v1)
