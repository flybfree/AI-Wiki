---
title: SARA: An Auditor-in-the-Loop LLM Recommender for Sustainability Reports
url: http://arxiv.org/abs/2611.30839v1
type: paper-summary
date: 2026-11-24
source_paper: 2026-11-23_15-23-50Z_SARA_AnAuditor_in_the_LoopLLMRecommenderforSustain.md
generated_at: 2026-11-24 22:05
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
SARA (Sustainability Reporting Assistant) is a human-in-the-loop recommender system, delivered as a Microsoft Word add-in, designed to support assurance professionals in auditing corporate sustainability reports. It casts auditing as content-based recommendation over a fixed regulatory taxonomy: for each of roughly 1,700 regulatory requirements, it recommends the passages that address that requirement and predicts a compliance verdict, while keeping the auditor in full control. By using topic-prediction filtering rather than feeding the entire draft report to the LLM, SARA makes per-requirement matching cheaper, faster, and more accurate, and it is in production use across PwC Germany's sustainability-assurance practice.

## Key Takeaways
- The auditing task is framed as content-based recommendation over a fixed regulatory taxonomy, mapping a company-specific checklist drawn from about 1,700 requirements onto the relevant passages of lengthy, repeatedly revised draft reports, rather than treating compliance judgment as a single monolithic LLM prompt.
- Topic-prediction filtering is the central efficiency mechanism: on expert-annotated reports, SARA reduces matching cost by roughly sixfold and runtime by 42% compared with feeding the full report to the LLM, while also improving accuracy.
- The system is deliberately auditor-in-the-loop and delivered as a Microsoft Word add-in, so the auditor retains control over recommendations and verdicts; it is already deployed in production across PwC Germany's sustainability-assurance practice.

## Context
Corporate sustainability reporting is expanding in regulatory scope and document length, creating a bottleneck for assurance teams that must reconcile many requirements against frequently revised drafts. Large language models offer a plausible route to automate passage retrieval and compliance triage, but naive full-document prompting is expensive, slow, and less reliable. SARA sits at the intersection of LLM-based information retrieval, recommendation systems, and professional assurance workflows, showing how a constrained, taxonomy-aware design can make LLM assistance practical inside an existing Word-based audit process.

## Implications
For practitioners, SARA demonstrates that targeted filtering and per-requirement recommendation can materially cut cost and latency while preserving human oversight, which is critical in regulated assurance work where accountability cannot be delegated to the model. For the field, it provides a concrete template for embedding LLMs into professional document-review workflows without replacing the expert, and it suggests that fixed regulatory taxonomies plus topic prediction are a reusable pattern for other high-stakes compliance domains. The production deployment at PwC Germany indicates that such systems can move beyond prototypes into routine audit practice, provided the auditor remains in control of final judgments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.30839v1)
