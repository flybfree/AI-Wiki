---
title: Validity-Aware Jailbreak Evaluation for Large Language Models
published: 2026-08-31T23:57:53Z
authors: Qilong Wu, Sahil Wadhwa, Pranab Mohanty, Giri Iyengar, Varun Chandrasekaran
url: http://arxiv.org/abs/2609.00498v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Validity-Aware Jailbreak Evaluation for Large Language Models

## Abstract
Jailbreak robustness has become central to large language model (LLM) safety evaluation, yet prevailing methodologies rely primarily on refusal behavior, semantic resemblance, and intent-matching heuristics that emphasize linguistic plausibility rather than correctness. We identify a key limitation in existing evaluations: many jailbreak intents depend on instructional validity rather than epistemic factuality, allowing realistic-looking responses to be labeled successful despite being factually or procedurally incorrect. To address this gap, we propose Sequential Epistemic and Action-Level Validation (SEAV), a verification-centric jailbreak evaluation framework that decomposes responses into ordered steps and evaluates both validity and correctness. SEAV combines LLM-as-a-judge mechanisms for semantic interpretation with retrieval-grounded verification using external knowledge sources, assessing whether generated content is factually correct, structurally consistent, and operationally capable of advancing harmful objectives. Empirically, SEAV cuts the false-positive rate on SD-A (a curated strategic-dishonesty diagnostic) by 14.9\,pp vs. the strongest baseline, and reclassifies 22.1\%--51.0\% of sampled prior-labeled successes as invalid across three of four public benchmarks. Together, these results show that enforcing correctness substantially reshapes measured robustness: many previously labeled jailbreak successes are reclassified as invalid, and results are stable across the tested search backends and evaluator models. Code and data are available at https://github.com/Ardor-Wu/SEAV.

## Metadata
- **Published**: 2026-08-31T23:57:53Z
- **Authors**: Qilong Wu, Sahil Wadhwa, Pranab Mohanty, Giri Iyengar, Varun Chandrasekaran
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00498v1)