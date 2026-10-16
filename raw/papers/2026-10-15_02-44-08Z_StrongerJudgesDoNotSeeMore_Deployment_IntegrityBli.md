---
title: Stronger Judges Do Not See More: Deployment-Integrity Blindness in LLM Evaluation
published: 2026-10-15T02:44:08Z
authors: Jianchang Su, Dawei Xiang, Yifan Zhang, Wei Zhang
url: http://arxiv.org/abs/2610.21135v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Stronger Judges Do Not See More: Deployment-Integrity Blindness in LLM Evaluation

## Abstract
LLM-agent evaluation reports behavioral scores but leaves the identity of the deployed runtime stack unreported. A tampered deployment that preserves evaluated outputs passes every output-only evaluator. We introduce DIB-Bench, a benchmark that measures this deployment-integrity blindness across 7,560 scored examples, six tamper types, and an evaluator ladder from regex scorers through LLM judges to GPT-5-nano. Stronger evaluators accept more tampered outputs: mean acceptance rises from 88.6% (rule-based) to 94.1% (GPT-5-nano), and a trigger-conditional tamper invisible on the evaluation suite produces 48-100% harmful outputs, rising with model capability. A PAC-style bound shows that tampers with zero output shift are undetectable from outputs at any sample size; a manifest-hash identity channel detects them with zero samples. Behavioral fingerprinting identifies the model component above chance (76.7%) but covers one of six stack components. We also propose a graded deployment-identity descriptor for evaluation reports.

## Metadata
- **Published**: 2026-10-15T02:44:08Z
- **Authors**: Jianchang Su, Dawei Xiang, Yifan Zhang, Wei Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.21135v1)