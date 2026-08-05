---
title: AI Forensics Across White-, Grey-, and Black-Box Access: A Process Model and Research Agenda for Post-Incident Investigation of AI Systems
url: http://arxiv.org/abs/2608.03520v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_12-04-57Z_AIForensicsAcrossWhite__Grey__andBlack_BoxAccess_A.md
generated_at: 2026-08-05 01:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes a unified process model for investigating AI‑related incidents by categorizing investigator access as white, grey, or black box. It outlines how each access level influences data collection, preservation, analysis, and reporting, and introduces an order of volatility that ranks runtime state, context windows, logs, retrieval stores, model artifacts, and training lineage.

## Key Takeaways
- The framework distinguishes three access levels—white box (full system code), grey box (partial documentation), black box (no internal details)—and shows how each limits what can be gathered, stored, or analyzed.  
- A process‑model matrix maps these access constraints to the four forensic phases: collection, preservation, analysis, and reporting, highlighting gaps such as black‑box preservation that require new methods.  
- The volatility order ranks artifacts from most transient (runtime state) to most stable (training lineage), guiding which data must be captured at what stage of an incident.

## Context
AI systems now drive critical decisions across domains like finance, healthcare, and autonomous vehicles, making post‑incident investigation essential for accountability. Existing AI forensics research often isolates specific techniques or system types, leaving a fragmented understanding of how investigators can reconstruct behavior when they lack deep insight into the model’s internals.

## Implications
For practitioners, this model offers a roadmap to prioritize data capture based on access and volatility, reducing investigative effort. For researchers, it highlights open challenges—especially black‑box preservation and model version attestation—that must be addressed to build robust AI auditability standards.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03520v1)
