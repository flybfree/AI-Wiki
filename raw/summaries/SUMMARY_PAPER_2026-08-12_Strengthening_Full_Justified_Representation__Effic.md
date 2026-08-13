---
title: Strengthening Full Justified Representation: Efficient Verification and Computation
url: http://arxiv.org/abs/2608.11500v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-11_23-29-08Z_StrengtheningFullJustifiedRepresentation_Efficient.md
generated_at: 2026-08-12 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces FJR+, a strengthened version of full justified representation that can be verified and satisfied in polynomial time, addressing the coNP‑completeness of checking standard FJR. It proves that the Residual‑Budget Greedy algorithm yields a partial committee where every size‑k completion satisfies FJR+ and is priceable under sequential Phragmén, producing a rule that always meets both FJR+ and its sub‑core whenever at least k candidates approve. The authors also present a Droop‑quota variant of FJR+, extend the framework to approval‑based participatory budgeting with arbitrary project costs, and show how a project‑specific RBG computation remains polynomial.

## Key Takeaways
- FJR+ is provably verifiable in polynomial time unlike the original FJR which requires coNP verification.  
- The Residual‑Budget Greedy algorithm guarantees that any completion of size k satisfies FJR+, enabling priceable outcomes via sequential Phragmén.  
- A Droop‑quota version and a cost‑aware participatory budgeting extension are provided, both computable in polynomial time.

## Context
This work advances approximation theory for approval‑based committee selection by replacing an intractable verification problem with a tractable one, aligning computational feasibility with theoretical guarantees. In AI research on voting systems and resource allocation, such results support scalable algorithmic design without sacrificing fairness constraints.

## Implications
Practitioners can rely on FJR+ to construct efficient, provably fair election rules that are both verifiable and priceable, reducing reliance on costly verification steps. The polynomial‑time extensions enable real‑world applications in participatory budgeting where cost structures vary across projects.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11500v1)
