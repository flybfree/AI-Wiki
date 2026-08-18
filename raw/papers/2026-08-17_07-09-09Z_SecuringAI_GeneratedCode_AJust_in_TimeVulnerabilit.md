---
title: Securing AI-Generated Code: A Just-in-Time Vulnerability Detection and Remediation Pipeline
published: 2026-08-17T07:09:09Z
authors: Mikhail Surikov
url: http://arxiv.org/abs/2608.16187v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Securing AI-Generated Code: A Just-in-Time Vulnerability Detection and Remediation Pipeline

## Abstract
AI-assisted development tools generate vulnerable code at significant rates, yet few automated mechanisms exist to detect, enrich, fix, and verify security issues at development velocity, particularly ones that ground remediation in real-world threat context. This paper presents an automated security evaluation pipeline that generates Python code from LLMSecEval prompts, scans for vulnerabilities using CodeQL and Bandit in parallel with an independent Code Validator LLM, enriches the Code Validator findings with MITRE ATT&CK techniques, CWE Observed Examples, and Python best practice guidelines, generates fixes via the Code Generation LLM, and re-scans with CodeQL and Bandit to verify outcomes. Two pipeline configurations were evaluated: Pipeline 1 (P1), using enriched Code Validator findings only, and Pipeline 2 (P2), where it additionally receives the initial CodeQL and Bandit findings. Both configurations were run across four Claude models: Opus 4.8, Sonnet 4.6, Sonnet 5, and Haiku 4.5, producing 80 runs against 26 LLMSecEval prompts covering 9 CWE categories.   P1 reduced static analyzer findings across all four models, ranging from -9% (Opus 4.8) to -54% (Sonnet 5). P2 deepened these reductions further, ranging from -29% (Opus 4.8) to -69% (Haiku 4.5), with P2 outperforming P1 for every model. Verdict consistency averaged approximately 81% modal agreement across all configurations, with P2 marginally more stable than P1. Remediation introduced new vulnerabilities in 15-22% of cases: roughly 70% involved a single new finding, and P2 reduced churn for three of four models, with Sonnet 5 as the sole exception. Notably, the best Code Generation LLM (Opus 4.8) was not the best pipeline performer, as Sonnet 4.6 produced the lowest residual findings and highest pass rate after P2 remediation, suggesting that pipeline effectiveness and first-draft security are distinct properties.

## Metadata
- **Published**: 2026-08-17T07:09:09Z
- **Authors**: Mikhail Surikov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16187v1)