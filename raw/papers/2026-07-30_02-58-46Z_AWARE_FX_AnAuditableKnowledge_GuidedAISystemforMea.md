---
title: AWARE-FX: An Auditable Knowledge-Guided AI System for Measuring Corporate Foreign-Exchange Hedging Disclosure
published: 2026-07-30T02:58:46Z
authors: Qi Wang
url: http://arxiv.org/abs/2607.27611v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AWARE-FX: An Auditable Knowledge-Guided AI System for Measuring Corporate Foreign-Exchange Hedging Disclosure

## Abstract
Corporate annual reports contain weakly structured evidence about foreign-exchange risk management, derivative use, natural hedging, and explicit non-use. This study develops AWARE-FX, an auditable AI/NLP decision-support system that converts report text into traceable firm-year hedging-disclosure measures. The system combines a professional-source lexicon, negation and accounting-status logic, channel-specific financial encoders, exact evidence gates, conservative aggregation, and an audit ledger. Across 24,909 Hong Kong firm-years from 2008-2025, it retrieves and scores 543,527 snippets. Reliability is evaluated through ablations, a stratified 300-snippet human audit, three-seed FinBERT-ModernBERT comparisons, strict 2023-2025 temporal tests, probability calibration, selective prediction, and fixed-prompt generative-model benchmarks. FinBERT has the higher mean F1 in seven of eight encoder task-split comparisons; its temporal F1 ranges from 0.702 to 0.872. Abstaining on the 20% least-confident temporal observations raises retained-sample F1 by 0.050-0.077. Deterministic Qwen3-8B performs strongly on commodity and negation evidence but poorly on foreign-debt and accounting-context labels, showing that a general-purpose LLM does not uniformly replace domain constraints. The strict FX score is negatively associated with linked baseline and stress-period FX exposure, whereas the generic broad score is not. These associations provide external construct validation, not causal estimates of hedging effectiveness. AWARE-FX contributes a tested decision-support architecture in which retrieval, status logic, classification, uncertainty handling, aggregation, and external validation remain separately auditable.

## Metadata
- **Published**: 2026-07-30T02:58:46Z
- **Authors**: Qi Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27611v1)