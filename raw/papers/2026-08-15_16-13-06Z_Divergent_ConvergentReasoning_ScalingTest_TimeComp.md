---
title: Divergent-Convergent Reasoning: Scaling Test-Time Compute through Structured Solution Synthesis
published: 2026-08-15T16:13:06Z
authors: Bo Wen, Yuhao Chen, Erhan Bilal, Carla Agurto Rios, Chen Wang, Junchen Jiang
url: http://arxiv.org/abs/2608.15303v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Divergent-Convergent Reasoning: Scaling Test-Time Compute through Structured Solution Synthesis

## Abstract
Test-time compute can substantially improve Large Language Model (LLM) reasoning performance, yet how and when additional compute helps remains poorly understood. We study Divergent-Convergent Reasoning (DCR), a simple two-phase primitive consisting of an exploration phase that generates multiple candidate solutions followed by a convergent reconciliation phase. We present three core results. First, we show that even a single reconciliation step can reliably amplify correct minority reports: across datasets, DCR often recovers the correct answer when correct exploration outputs are in the minority, a regime where majority voting fails. Second, we introduce recursive DCR, an autoregressive reconciliation system that iteratively analyzes disagreements and allocates additional test-time compute. Recursive DCR achieves higher accuracy than fixed-compute baselines-reaching 93.3% on AIME 2024 and 92.0% on AIME 2025-while using roughly 27% less compute on average, demonstrating that attentive resource allocation is superior to uniform scaling. Third, we analyze disagreement among exploration outputs via a simple, training-free dispersion metric. Dispersion reveals a structured relationship between disagreement and test-time gains: in regimes where DCR is effective, higher disagreement among exploration outputs is associated with larger accuracy improvements from reconciliation. Together, these results show that disagreement, often viewed as noise, can be systematically exploited to improve test-time reasoning and reveal emerging scaling laws for agentic LLM systems.

## Metadata
- **Published**: 2026-08-15T16:13:06Z
- **Authors**: Bo Wen, Yuhao Chen, Erhan Bilal, Carla Agurto Rios, Chen Wang, Junchen Jiang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15303v1)