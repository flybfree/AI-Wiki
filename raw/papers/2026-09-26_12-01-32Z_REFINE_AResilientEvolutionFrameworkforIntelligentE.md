---
title: REFINE: A Resilient Evolution Framework for Intelligent Enterprise Alert Triage in Security Operations Centers
published: 2026-09-26T12:01:32Z
authors: Huimin Chen, Quan Long, Yanhao Wang
url: http://arxiv.org/abs/2609.32516v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# REFINE: A Resilient Evolution Framework for Intelligent Enterprise Alert Triage in Security Operations Centers

## Abstract
Security Operations Centers (SOCs) process large volumes of alerts daily. Alert triage prioritizes high-risk threats while reducing manual review of benign alerts. LLM agents can reason over logs and threat intelligence, but struggle to keep aligned with organization-specific, rapidly evolving SOC operational standards.   We introduce REFINE, an LLM-agent framework for enterprise alert triage. REFINE encodes analyst expertise as structured skills and continuously adapts using analyst disposition feedback. It enforces recall = 1.0 as a hard constraint during evolution to maximize auto-closure of false positives, and identifies judgment blind spots by combining alert distributions with model error boundaries.   Evaluated on four real industrial SOC scenarios across four MITRE ATT&CK phases with temporal split: REFINE achieves recall=1.0 on all evolution sets. On future test windows, it retains recall=1.0 in three scenarios; the degraded case reaches 0.807 recall, still outperforming self-evolution baselines (0.49-0.58).

## Metadata
- **Published**: 2026-09-26T12:01:32Z
- **Authors**: Huimin Chen, Quan Long, Yanhao Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32516v1)