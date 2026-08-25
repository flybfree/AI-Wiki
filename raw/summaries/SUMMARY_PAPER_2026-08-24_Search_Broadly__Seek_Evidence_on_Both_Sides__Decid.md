---
title: Search Broadly, Seek Evidence on Both Sides, Decide Narrowly: Evidence-Admissible GraphRAG for Longitudinal Clinical Event Verification
url: http://arxiv.org/abs/2608.22062v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-22_18-06-10Z_SearchBroadly_SeekEvidenceonBothSides_DecideNarrow.md
generated_at: 2026-08-24 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MedEventGraph-RAG, an evidence-admissible framework for longitudinal clinical event-relation verification that separates broad evidence discovery from narrow assessment. It achieves balanced accuracy of 78.6 on temporal verification across multiple datasets and improves over baselines by up to 30 points. The approach reduces false-support predictions under evidence masking.

## Key Takeaways
- MedEventGraph-RAG represents patient events as a graph linked to source evidence such as structured rows, note spans, timestamps, and numerical trajectories, enabling precise retrieval of both supporting and contradicting information.
- The query-specific evidence contract filters results by patient identity, clinical scope, occurrence binding, and traceability before human assessors decide outcomes, ensuring balanced accuracy across temporal, medication-adverse-event, and recorded-order verification tasks.
- Under evidence masking the system reaches 92.2 balanced accuracy with no false-support predictions, demonstrating robustness when intermediate events are hidden.

## Context
Longitudinal clinical event-relation verification is a critical task in patient monitoring where evidence spans diverse sources and time points, leading to ambiguous or unsupported conclusions. Current methods often conflate broad retrieval with narrow assessment, resulting in high false-positive rates. This work addresses the gap by formalizing an evidence-admissible pipeline that aligns discovery with evaluation.

## Implications
Practitioners can rely on MedEventGraph-RAG to generate traceable event chains and avoid unwarranted clinical conclusions, enhancing trust in AI-assisted longitudinal analysis. The framework’s ability to recover complete source-traceable chains even when events are partially hidden supports real-world deployment where data is incomplete or noisy.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22062v1)
