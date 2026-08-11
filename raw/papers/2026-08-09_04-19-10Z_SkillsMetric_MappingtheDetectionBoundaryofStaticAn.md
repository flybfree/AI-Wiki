---
title: SkillsMetric: Mapping the Detection Boundary of Static Analysis for Malicious Agent Skills
published: 2026-08-09T04:19:10Z
authors: Xinze Chen, Chi Zhang, Ping Ji, Yimin Liu
url: http://arxiv.org/abs/2608.08468v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SkillsMetric: Mapping the Detection Boundary of Static Analysis for Malicious Agent Skills

## Abstract
Agent Skills---structured packages of instructions and scripts that augment LLM-based agents---are rapidly proliferating, yet their security properties remain under-explored. We present \textsc{SkillsMetric}, a five-stage static analysis framework that scores skill packages along pattern density, statistical anomaly, dataflow taint, import anomaly, and capability mismatch dimensions. We construct an adversarial evaluation dataset of 2{,}266 skills spanning 16~attack types across code-level, system-level, and semantic-level threats, and evaluate on the full SkillMD-138K corpus. Our framework achieves an AUC of 0.93 and 5-fold cross-validated F1 of 73.4\%$\pm$0.5\%, with strong detection of data exfiltration (93\%) and steganographic payloads (93\%). Crucially, we identify fundamental blind spots: \emph{host destruction} attacks using common shell commands evade all five stages (0\% detection), and \emph{prompt injection} via natural-language manipulation achieves only 42\% detection. These findings establish that static analysis alone is insufficient for skill security, motivating defense-in-depth architectures that combine fast static pre-screening with semantic review.

## Metadata
- **Published**: 2026-08-09T04:19:10Z
- **Authors**: Xinze Chen, Chi Zhang, Ping Ji, Yimin Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08468v1)