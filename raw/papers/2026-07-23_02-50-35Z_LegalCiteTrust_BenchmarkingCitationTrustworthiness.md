---
title: LegalCiteTrust: Benchmarking Citation Trustworthiness in Chinese Long-Form Legal Research Reports
published: 2026-07-23T02:50:35Z
authors: Yunhan Li, Mingjie Xie, Zeyang Shi, Gengshen Wu, Min Yang
url: http://arxiv.org/abs/2607.20872v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LegalCiteTrust: Benchmarking Citation Trustworthiness in Chinese Long-Form Legal Research Reports

## Abstract
Long-form legal research reports increasingly rely on LLMs and agentic research systems, but their reliability depends not only on answering the task, but also on whether cited legal authorities are trustworthy. A citation can be risky even when it points to a real source: the report may omit limiting conditions, misdescribe the authority, or use it to support a stronger claim than the source allows. We introduce LegalCiteTrust, a benchmark for evaluating citation trustworthiness in Chinese long-form legal research reports. It contains 72 densely annotated report-level tasks and evaluates reports along three dimensions: Coverage, Support, and Citation Trustworthiness. Citation Trustworthiness is operationalized through citation-level Existence, Fidelity, and Applicability (E/F/A). Experiments on general-purpose LLMs, deep-research systems, and legal-specific systems show that task completion, evidence richness, citation density, and citation reliability expose different system behaviors. Retrieval tools can improve evidence support without reliably improving the Trust score, while E/F/A-based revision improves Trust and Final score more clearly than existence-only filtering. These results suggest that trustworthy legal research generation requires citation-aware evidence governance after retrieval: systems must not only retrieve legal authorities, but also select, describe, and apply them reliably.

## Metadata
- **Published**: 2026-07-23T02:50:35Z
- **Authors**: Yunhan Li, Mingjie Xie, Zeyang Shi, Gengshen Wu, Min Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20872v1)