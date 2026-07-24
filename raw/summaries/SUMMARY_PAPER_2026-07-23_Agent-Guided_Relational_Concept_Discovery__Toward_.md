---
title: Agent-Guided Relational Concept Discovery: Toward Interpretable Surgical Margin Assessment
url: http://arxiv.org/abs/2607.21437v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_15-44-04Z_Agent_GuidedRelationalConceptDiscovery_TowardInter.md
generated_at: 2026-07-23 22:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Agent-Guided Concept Discovery, a method that automatically uncovers interpretable concepts from raw REIMS data without predefined labels. The framework improves diagnostic performance on skin and breast cancer datasets compared to baselines and demonstrates better generalization in an intraoperative case with fewer false positives.

## Key Takeaways
- A reasoning agent refines semantic descriptions of learned concepts and adjusts their weight based on diagnostic relevance, enabling self‑supervised concept refinement.
- Concepts are grounded against a biochemical knowledge graph to ensure consistency with known metabolic relationships, reducing noise and improving interpretability.
- The approach yields higher balanced accuracy and sensitivity than existing supervised models while producing fewer false positives in real surgical scenarios.

## Context
The integration of deep learning into medical diagnostics is hindered by black‑box predictions and limited transfer to noisy operating room data. Concept‑based learning aims to bridge this gap, but prior methods require costly human annotations that are impractical for mass spectrometry workflows.

## Implications
This framework could enable clinicians to trust AI‑driven margin assessments with transparent, explainable insights, potentially accelerating adoption of automated pathology tools in surgical settings and reducing diagnostic errors.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21437v1)
