---
title: Conversation as Measurement in Clinical Encounters: Observable Phase Structure, Partially Observable Patient State
published: 2026-08-09T19:16:10Z
authors: Lily Chen, Ted Mau, Michael Gensheimer, Brian Anthony Nuyen, Nancy Jiang, James Zou
url: http://arxiv.org/abs/2608.08868v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Conversation as Measurement in Clinical Encounters: Observable Phase Structure, Partially Observable Patient State

## Abstract
Many modern AI systems analyze conversational traces to infer aspects of human interaction and state, implicitly assuming that such information is recoverable from conversation. We study observability: whether a target is recoverable from conversational transcripts alone. Observability is difficult to assess because transcripts may provide only a partial view of many targets, and large-scale analysis requires model-based annotation, making true limits of the conversational signal hard to distinguish from annotator error. We therefore study clinical encounters, where patient-reported outcome measures (PROMs) provide an external anchor for patient state, and visits follow broadly structured patterns. We study observability of patient state and conversational phase structure using 439 real-world clinical encounter transcripts spanning 134 hours, including 245 ENT transcripts paired with 273 PROM surveys. We operationalize patient state using PROM scores for voice, cough, and swallowing; phase structure using conversational phase segmentation. To make these analyses credible at scale, we use a PHI-compliant GPT-5 deployment for transcript annotation and conduct 40 hours of manual validation, reducing the risk that apparent limits of observability simply reflect annotator error. Our core finding is an observability asymmetry: phase structure is observable and useful for characterizing clinical encounter organization, while patient state is only partially observable, even in a setting designed to elicit patient symptoms and experiences, cautioning against transcript-only inference of human state.

## Metadata
- **Published**: 2026-08-09T19:16:10Z
- **Authors**: Lily Chen, Ted Mau, Michael Gensheimer, Brian Anthony Nuyen, Nancy Jiang, James Zou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08868v1)