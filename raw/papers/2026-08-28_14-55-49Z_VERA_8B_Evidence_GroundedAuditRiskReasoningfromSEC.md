---
title: VERA-8B: Evidence-Grounded Audit Risk Reasoning from SEC Filings
published: 2026-08-28T14:55:49Z
authors: Menghan Liu, Elynn Chen
url: http://arxiv.org/abs/2608.28402v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VERA-8B: Evidence-Grounded Audit Risk Reasoning from SEC Filings

## Abstract
Across audit applications, judgments must be supported by reasonable evidence. However, standard financial language models prioritize fluency over evidence. They are built for general financial reasoning and may produce plausible but ambiguous answers, creating a grounding gap that makes them unsuitable for audit work. We address this gap with VERA-8B, a new end-to-end audit reasoning system that identifies audit risks before enforcement actions occur. Constructing such a model raises several challenges, as no prior machine learning work targets pre-enforcement audit prediction. To our knowledge, we are the first to unify SFT and GRPO for evidence-grounded audit reasoning under one evidence standard, achieving performance that surpasses all evaluated baselines. Because auditing cannot tolerate unsupported claims, we introduce abstention and uncertainty qualification to defer uncertain or evidence-incomplete cases. Finally, we design an AuditBridge to ground model reasoning for practical audit work. It transforms raw filings into verified records and then into reviewer-ready reports, bridging finance and computation with broad generality. Together, these components produce auditable, review-ready outputs suitable for practical audit work.

## Metadata
- **Published**: 2026-08-28T14:55:49Z
- **Authors**: Menghan Liu, Elynn Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28402v1)