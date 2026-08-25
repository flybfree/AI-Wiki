---
title: Search Broadly, Seek Evidence on Both Sides, Decide Narrowly: Evidence-Admissible GraphRAG for Longitudinal Clinical Event Verification
published: 2026-08-22T18:06:10Z
authors: Xingtao Lin, Yubo Feng, Weixin Liu, Hangqi Ren, Junchao Zhou, Caiwan Sun, You Chen
url: http://arxiv.org/abs/2608.22062v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Search Broadly, Seek Evidence on Both Sides, Decide Narrowly: Evidence-Admissible GraphRAG for Longitudinal Clinical Event Verification

## Abstract
Longitudinal clinical event-relation verification determines whether a patient record supports a specified relation among two or more clinical events. This task is challenging because evidence is distributed across structured records, notes, laboratory trajectories, encounters, and time, while negation, temporal mismatch, repeated documentation, and conflicting findings can make retrieved information appear relevant without establishing the relation.   We present MedEventGraph-RAG, an evidence-admissible framework that represents event occurrences in a patient-specific graph and links each occurrence to source evidence, including structured rows, note spans, timestamps, and numerical trajectories. Given a verification query specifying events, relation, and clinical scope, the graph guides discovery of candidate event chains and retrieves evidence from both supporting and contradicting sides. A query-specific evidence contract filters information by patient identity, scope, occurrence binding, and source traceability before a separate assessor determines supported, conflicting, refuted, or insufficient outcomes.   Across ten protocols on i2b2, n2c2, MIMIC-IV, and LUNGUAGE, MedEventGraph-RAG achieves balanced accuracies of 78.6, 67.3, and 96.8 on temporal, medication-adverse-event, and recorded-order verification, improving over the strongest matched baselines by 26.9, 4.9, and 30.4 points. Under evidence masking, it reaches 92.2 balanced accuracy with no false-support predictions. When intermediate events are hidden, it recovers complete source-traceable event chains in 57.9% of i2b2 and 70.0% of LUNGUAGE cases. These results show that separating broad evidence discovery from narrow evidence-admissible assessment improves longitudinal clinical verification and reduces unsupported conclusions.

## Metadata
- **Published**: 2026-08-22T18:06:10Z
- **Authors**: Xingtao Lin, Yubo Feng, Weixin Liu, Hangqi Ren, Junchao Zhou, Caiwan Sun, You Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22062v1)