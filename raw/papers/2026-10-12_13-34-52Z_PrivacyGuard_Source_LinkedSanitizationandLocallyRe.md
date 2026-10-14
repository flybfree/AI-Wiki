---
title: PrivacyGuard: Source-Linked Sanitization and Locally Resolvable PII References for Cloud GUI Agents
published: 2026-10-12T13:34:52Z
authors: Zian Yuan, Wei Li
url: http://arxiv.org/abs/2610.16778v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PrivacyGuard: Source-Linked Sanitization and Locally Resolvable PII References for Cloud GUI Agents

## Abstract
Cloud graphical user interface (GUI) agents send instructions and screenshots to remote planners, exposing personally identifiable information (PII). Existing placeholder defenses mask detected spans and reuse exact strings. Fragmented or changed forms can expose PII or break entity continuity across turns. PrivacyGuard addresses this private reference problem with source-linked sanitization (SAN) and a structured reference lifecycle (REF). SAN reconstructs fragmented or overlapping evidence and rewrites the complete source extent. REF links changed appearances to session entities and supports locally resolvable references without returning raw values to the upload path. In five-turn sessions scored against common gold, PrivacyGuard reduces audited source-value leakage by 33.55\%--82.60\% relative to the closest prior full-pipeline system in all four reader--language combinations. REF raises strict cross-form continuity from 0.04 under exact-value reuse to 0.81. In reference-required Android tasks, verified completion rises from 8/30 and 7/30 to 17/30 and 20/30. On AndroidLab, PrivacyGuard achieves the highest or tied-highest task-success point estimate among protection pipelines for all four planners. On PrivScreen, it reduces fixed-reader field exposure by 62.72\%--62.84\% relative to the same baseline. PrivacyGuard lowers upload exposure while preserving a locally resolvable task path.

## Metadata
- **Published**: 2026-10-12T13:34:52Z
- **Authors**: Zian Yuan, Wei Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.16778v1)