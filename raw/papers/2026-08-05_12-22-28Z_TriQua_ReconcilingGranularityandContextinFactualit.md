---
title: TriQua: Reconciling Granularity and Context in Factuality Evaluation
published: 2026-08-05T12:22:28Z
authors: Jin Liu, Steffen Thoma, Achim Rettinger
url: http://arxiv.org/abs/2608.05228v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TriQua: Reconciling Granularity and Context in Factuality Evaluation

## Abstract
The "decompose-then-verify" paradigm for LLM factuality evaluation faces a fundamental trade-off: atomic facts, i.e., one sentence conveying one unit of information, often omit essential context, while broader statements lack the granularity needed for precise assessment. To address this, we introduce TriQua, a framework that flexibly models facts based on their complexity. Simple claims are extracted as standard triples, while complex claims are represented as hyperrelational facts by attaching auxiliary contextual qualifiers. This adaptive structure preserves the necessary context for accurate retrieval and verification without sacrificing atomicity. Furthermore, TriQua's verification process directly annotates concrete errors within specific triples and qualifiers, providing fine-grained explainability for error detection. Alongside the framework, we propose TriQuaScore to quantify the factuality of these structured fact units. Empirical evaluations show that TriQuaScore strongly aligns with human annotated factuality scores, TriQua achieves robust decomposition quality, and outperforms existing decomposition-based frameworks in evidence-based fact verification.

## Metadata
- **Published**: 2026-08-05T12:22:28Z
- **Authors**: Jin Liu, Steffen Thoma, Achim Rettinger
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05228v1)