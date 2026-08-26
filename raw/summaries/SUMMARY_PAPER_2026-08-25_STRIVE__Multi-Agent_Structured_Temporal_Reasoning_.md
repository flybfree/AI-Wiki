---
title: STRIVE: Multi-Agent Structured Temporal Reasoning with Integrated Verification for Longitudinal Radiology Report Generation
url: http://arxiv.org/abs/2608.24237v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_08-43-15Z_STRIVE_Multi_AgentStructuredTemporalReasoningwithI.md
generated_at: 2026-08-25 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces STRIVE, a multi‑agent framework for longitudinal radiology report generation that separates diagnosis, attribute estimation, and temporal change reasoning into distinct agents producing explicit evidence. The Temporal Change Agent uses Progression‑Aware GRPO with a verifiable reward shaping direction‑preserving errors favorably while penalizing reversals. Verification occurs via a deterministic Consistency Gate before report generation and a Validation Agent that checks if the final report is supported by the aggregated clinical evidence, achieving superior clinical efficacy on Longitudinal‑MIMIC.

## Key Takeaways
- The authors decompose LRRG into three specialized agents—Diagnosis, Attribute, and Temporal Change—that generate transparent intermediate outputs, reducing interference between tasks.  
- The Temporal Change Agent is further enhanced with Progression‑Aware GRPO, a verifiable reward that rewards direction‑preserving errors and penalizes direction reversals, improving temporal reasoning accuracy.  
- STRIVE employs two verification stages: a deterministic Consistency Gate to reconcile agent outputs before report generation and a Validation Agent to ensure the final report is grounded in the combined clinical evidence.

## Context
Longitudinal radiology report generation remains challenging because existing models treat diagnosis, attribute estimation, and change detection as joint implicit tasks, leading to opaque decision making. This work addresses these limitations by introducing modular agents that produce verifiable intermediate evidence, aligning with broader AI trends toward explainable and auditable reasoning pipelines.

## Implications
For clinicians, STRIVE’s transparent evidence generation can improve trust in automated reports and facilitate error tracing. For industry stakeholders, the framework demonstrates a path to more reliable longitudinal analysis, potentially reducing misdiagnosis rates and supporting regulatory compliance in medical imaging services.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24237v1)
