---
title: Grounded Normative Rule Generation with Structured Search
published: 2026-08-23T05:43:42Z
authors: Fanqi Kong, Huaxiao Yin, Ruijie Zhang, Xiaoyuan Zhang, Yizhe Huang, Jian Gao, Shuo Chen, Song-Chun Zhu
url: http://arxiv.org/abs/2608.22229v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Grounded Normative Rule Generation with Structured Search

## Abstract
Normative rules like institutional charters and workplace policies must be both human-readable and operationally verifiable against actual environment records. However, current language generation and structured-output benchmarks primarily reward surface fluency or schema compliance, leaving operational grounding weakly tested. This creates a critical vulnerability where standard language models generate plausible-sounding policies that fail during enforcement because they rely on unavailable data logs or misaligned scopes. To address this challenge, we formalize the problem as Grounded Normative Rule Synthesis (GNRS) and introduce GNRS-Search, a framework that utilizes Markov Chain Monte Carlo (MCMC) sampling to optimize a discrete, five-slot And-Or Graph (AOG). By explicitly decoupling intermediate operational structure from final prose generation, this method isolates executable feasibility from writing style and allows rule failures to be localized prior to surface realization. We evaluate our approach on GNRS-Bench, a benchmark spanning 116 controlled goals across eight scene families, and RealCharter-Bench, which evaluates transfer to 53 real-derived policy tasks with hidden source clauses. GNRS-Search raises average rubric quality from 68.8% to 81.0% and ranks first under a disclosed executable composite metric, while systematic slot interventions confirm that performance gains stem from robust operational logic rather than rhetorical tuning. Ultimately, by transforming automated rule drafting into an inspectable search problem, this work provides a foundational paradigm for deploying verifiable and compliance-ready personal agents within regulated environments.

## Metadata
- **Published**: 2026-08-23T05:43:42Z
- **Authors**: Fanqi Kong, Huaxiao Yin, Ruijie Zhang, Xiaoyuan Zhang, Yizhe Huang, Jian Gao, Shuo Chen, Song-Chun Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22229v1)