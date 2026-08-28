---
title: BALMS: Benchmarking Agentic LLMs for Longitudinal Mental Health Sensing
published: 2026-08-27T15:00:17Z
authors: Yu Yvonne Wu, Arvind Pillai, Yuliang Chen, Yuwei Zhang, Sudarshan Regmi, Tess Z. Griffin, Michael V. Heinz, Lisa A. Marsch, Nicholas C. Jacobson, Andrew Campbell
url: http://arxiv.org/abs/2608.27219v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BALMS: Benchmarking Agentic LLMs for Longitudinal Mental Health Sensing

## Abstract
Mental health assessment relies on episodic self-report scales, which convert subjective states such as stress into numerical scores but provide only sparse snapshots of wellbeing. Wearable devices offer longitudinal behavioral and physiological signals for continuous, low-burden monitoring. Recent LLM-driven personal-health agents enable natural language queries over wearable signals, but mainly handle short-term, retrieval-based lookups (e.g., highest step count over a week). They do not evaluate whether agents can reason over long-term signals to predict wellbeing scores paired with evidence-grounded rationales. To address this gap, we introduce BALMS, the first systematic benchmark of LLM-based agentic systems for longitudinal mental health sensing. BALMS spans 3 real-world longitudinal datasets, 2 task families (closed-form wellbeing-score prediction and rationale generation auto-graded by an LLM-as-Judge), 3 agentic paradigms evaluated across 5 open- and closed-source LLM backbones. We find that zero-shot agents rarely outperform a simple mean baseline, except with stronger backbones or compact, semantically meaningful features. Chain-of-thought prompting improves reasoning-oriented backbones, but does not guarantee temporal grounding or numerical correctness. Together with more analysis on efficiency and temporal scaling, BALMS highlights the need for longitudinal mental health agents that selectively retrieve history, ground temporal evidence, and reason over interpretable behavioral features.

## Metadata
- **Published**: 2026-08-27T15:00:17Z
- **Authors**: Yu Yvonne Wu, Arvind Pillai, Yuliang Chen, Yuwei Zhang, Sudarshan Regmi, Tess Z. Griffin, Michael V. Heinz, Lisa A. Marsch, Nicholas C. Jacobson, Andrew Campbell
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27219v1)