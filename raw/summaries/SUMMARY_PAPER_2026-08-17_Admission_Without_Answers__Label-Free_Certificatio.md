---
title: Admission Without Answers: Label-Free Certification and Experience Learning for LLM-Based Optimization Modeling
url: http://arxiv.org/abs/2608.15565v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_06-18-54Z_AdmissionWithoutAnswers_Label_FreeCertificationand.md
generated_at: 2026-08-17 21:33
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes AdmitOR, a label‑free admission gate for optimization model learners that leverages calibrated external behavioral evidence to decide whether to accept, abstain, or escalate candidates. Experiments on a 300‑problem stream show that AdmitOR achieves an admission precision of 0.927, markedly outperforming majority vote (0.871) and execution success (0.726), while reducing poisoned admissions by factors of three to eight compared with existing methods.

## Key Takeaways
- On a label‑blind stream of 300 problems, admitting every executable model results in roughly one admission being poisoned for every four, highlighting the danger of overly permissive acceptance criteria.  
- Single‑instance agreement accepts models that match at one value but differ elsewhere, indicating that pairwise similarity is insufficient for reliable labeling without ground truth.  
- AdmitOR’s calibrated false‑discovery threshold raises admission precision to 0.927, yielding a 3.1× improvement over majority vote and an 8.0× reduction in poisoned admissions relative to execution success.

## Context
Label‑free learning is essential because real ticket streams lack explicit answers; existing agents must infer knowledge from observable behavior alone. Current admission mechanisms often rely on simplistic majority voting or execution checks, which can propagate errors when the underlying data distribution deviates from labeled benchmarks. This paper addresses that gap by introducing a calibrated, evidence‑based gate.

## Implications
For practitioners developing large‑scale optimization solvers, AdmitOR offers a more reliable way to filter candidate models without relying on unavailable labels, improving downstream learning quality and reducing false positives. The approach’s focus on calibrated thresholds sets a new standard for label‑free admission in AI research and could be adapted across domains where ground truth is scarce.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15565v1)
