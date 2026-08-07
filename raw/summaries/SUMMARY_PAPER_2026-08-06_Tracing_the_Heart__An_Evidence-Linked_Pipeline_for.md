---
title: Tracing the Heart: An Evidence-Linked Pipeline for Heart-Failure Feature Engineering
url: http://arxiv.org/abs/2608.06366v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_17-57-37Z_TracingtheHeart_AnEvidence_LinkedPipelineforHeart_.md
generated_at: 2026-08-06 23:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Nimblemind Multi-Agent System (nMAS) to automate heart‑failure feature engineering by linking clinical evidence to a rubric. On 500 dummy records, nMAS produced 132 structured and 70 rubric‑scored features, which raised AUROC for HFrEF and HFpEF phenotyping. An LLM audit confirmed 81.5% of maximum points on evidence support.

## Key Takeaways
- The system generated a large number of aggregated features (132 structured + 70 rubric‑scored) that were verified for structural integrity, compliance with the clinical rubric, and provenance traceability.
- Adding these features improved model performance: AUROC rose from 0.895 to 0.963 for HFrEF and from 0.870 to 0.910 for HFpEF.
- Independent LLM assessment scored the evidence support at 81.5% of maximum, indicating strong traceability but room for improvement.

## Context
Automating EHR feature engineering remains a bottleneck in clinical AI due to fragmented data and guideline‑driven reasoning. This work shows that multi‑agent pipelines can produce auditable, rule‑based features without manual coding, addressing the 39‑45% time loss reported by data scientists.

## Implications
Practitioners can adopt nMAS as a reusable framework for other disease domains, reducing development effort and ensuring compliance with clinical guidelines. The approach also provides an audit trail that supports regulatory scrutiny of AI models in cardiology research.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06366v1)
