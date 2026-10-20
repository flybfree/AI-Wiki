---
title: Auditor-Assisted Summary-Channel Verification for Hosted LLM Identity Substitution
published: 2026-10-19T08:09:11Z
authors: Ziyi Zhang, Ziyao Wang, Guoheng Sun, Ang Li, Jian Li
url: http://arxiv.org/abs/2610.25982v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Auditor-Assisted Summary-Channel Verification for Hosted LLM Identity Substitution

## Abstract
Hosted LLM services increasingly expose model identity as a product claim, but external users and auditors often cannot inspect which model configuration served a request. We study an auditor-assisted regime in which a trusted auditor enrolls claimed identities and prepares verification material before deployment, while audit-time verification uses only the claimed identity and released output, without runtime access to model internals, inference logs, routing decisions, or provider metadata. We propose SUMMARK, a summary-channel watermarking framework that uses user-visible reasoning summaries as a keyed audit surface. During setup, SUMMARK constructs identity-specific vocabulary carriers, trains lightweight summary adapters, and calibrates per-identity thresholds. At deployment time, a keyed statistical test assesses whether the released summary is consistent with the claimed identity and, when needed, attributes the most likely enrolled identity. Across model families, scales, and task domains, SUMMARK reliably detects cross-family and cross-scale substitutions at low false-positive rates while preserving task-facing answer quality. We further study FP16->INT8/INT4 precision-consistency diagnostics and robustness under bounded post-processing, rewriting stress tests, and text-only spoofing, revealing both strong performance and clear failure boundaries. Our code is publicly available at https://github.com/trinitr0toluene/Summark.

## Metadata
- **Published**: 2026-10-19T08:09:11Z
- **Authors**: Ziyi Zhang, Ziyao Wang, Guoheng Sun, Ang Li, Jian Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.25982v1)