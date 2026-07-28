---
title: Confidently Wrong: Exception Chain Collapse in Frontier LLM Rule Evaluation
published: 2026-07-25T22:40:02Z
authors: Paul Simpson, John Kozak, Lisa Doake
url: http://arxiv.org/abs/2607.23386v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Confidently Wrong: Exception Chain Collapse in Frontier LLM Rule Evaluation

## Abstract
We document a failure class in frontier large language models -- exception chain collapse -- observed in eligibility evaluation under nested conditional rules of the form "A is required UNLESS B applies, UNLESS C overrides B". The failure reproduces at first observation, but its empirical surface is unstable: between March and April 2026 several failure cells closed silently under the same model alias, with no version bump (GPT-5.4 on construction insurance moved from 96.6% to 100%, same prompt and harness). For regulated workflows, frontier-model accuracy is a moving compliance boundary that shifts without notice. We present the Aethis Eligibility Module, a neuro-symbolic architecture in which LLMs author rules from authoritative sources and an SMT-based layer executes them deterministically, consistent with the authored specification regardless of model drift, reasoning-effort defaults, or prompt format. Three evidence bases: (i) a controlled benchmark of 225 scenarios across four regulatory domains documents the pattern and, in replication, the drift that partially closed it; (ii) a 20-scenario adversarial extension on construction insurance, where the engine scores 20/20, as does one of four frontier configurations (GPT-5.4 at low reasoning effort), while the other three, including Anthropic's strongest model at evaluation time, fail the same coverage-gap edge case; (iii) external validation on nine peer-reviewed LegalBench tasks, 949 held-out cases, where the engine is significantly more accurate than all three frontier models (combined McNemar's p <= 0.003), with margins up to +41 points on the curated multi-prong tasks against the Anthropic models. The contribution is to relocate uncertainty from the inference boundary, where it is silent, to the specification boundary, where it is deliberate and audited. All scenarios, rule encodings, and results are public and reproducible.

## Metadata
- **Published**: 2026-07-25T22:40:02Z
- **Authors**: Paul Simpson, John Kozak, Lisa Doake
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23386v1)