---
title: How to Speculate about Uncertainty in Agentic Coding? A Draft-Model Gate Method
published: 2026-09-04T15:30:22Z
authors: Konstantin Grotov, Valentin Malykh
url: http://arxiv.org/abs/2609.05274v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# How to Speculate about Uncertainty in Agentic Coding? A Draft-Model Gate Method

## Abstract
LLM agents deployed for software engineering fail expensively: they act confidently wrong, and bad actions are recognized only after costly execution and retry. We present Speculative Uncertainty (SU), a method that recovers a predictive failure signal for a black-box agent from its output tokens alone, with no access to logits, weights, activations, or repeated sampling. Inverting speculative decoding, a small open-weight draft model scores the agent's already-generated trajectory in a single forward pass. From these speculative cross-likelihoods we extract phase-aware features by separating the reasoning and action spans, and calibrate them against a verifiable objective. SU produces a failure-likelihood score that any downstream policy, such as routing, human intervention, or extra test-time compute, can consume directly. To show the signal is actionable, we instantiate one such policy, a pre-execution veto gate, on software engineering agents Qwen3-Coder-480B and closed-source Claude 3.5 Sonnet, cutting execution error rate by 6-8 percentage points and token cost by 14-19% in deployment, transferring to out-of-distribution benchmarks without retraining, and generalizing across agent models.

## Metadata
- **Published**: 2026-09-04T15:30:22Z
- **Authors**: Konstantin Grotov, Valentin Malykh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05274v1)