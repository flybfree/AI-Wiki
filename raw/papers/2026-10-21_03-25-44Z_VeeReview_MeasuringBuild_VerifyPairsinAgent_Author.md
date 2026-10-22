---
title: VeeReview: Measuring Build-Verify Pairs in Agent-Authored Pull Requests from a V-Model Perspective
published: 2026-10-21T03:25:44Z
authors: Gabriel Dautovi, Jie JW Wu
url: http://arxiv.org/abs/2610.29143v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VeeReview: Measuring Build-Verify Pairs in Agent-Authored Pull Requests from a V-Model Perspective

## Abstract
Context: Reviewing a pull request requires verification evidence that addresses the proposed change. Coding agent benchmarks and studies of pull request outcomes do not directly assess this relationship. Objective: We test whether the V-Model's build and verify pairs can measure verification evidence in pull requests and support comparisons between agent-authored and human-authored changes. Method: VeeReview classifies four build and verify pairs using repository signals and a language-model judge. Three pairs use model judgements constrained by deterministic signals, and a rule over the diff and repository tree decides Module Design-Unit Test. We evaluated VeeReview against a 25-pull request reference set labelled by two raters and applied it to 1,454 matched pairs of agent and human pull requests from 741 repositories. Results: VeeReview assigned lower build-only rates to agent-authored pull requests on all four pairs, contrary to the preregistered hypothesis (mixed-effects odds ratios 0.52 to 0.86). Architecture-Integration was not significant. Standardization for linked issues, shipped tests and size reduced matched-rate differences by 34% to 60%, and the rule-decided pair's standardized interval included zero. The instrument did not meet its preregistered calibration criterion: agreement with adjudicated labels was 4% to 60% against a required 80%, and inter-rater agreement was weak (kappa = 0.154). Conclusions: The rule-decided pair shows that a process measure judged by a language model partly reflects how a pull request is presented rather than the verification work behind it. We report the cohort differences as observations made with this instrument, and we argue that such measures need a mechanically decided component and a validated human reference before they can support comparisons of verification practice.

## Metadata
- **Published**: 2026-10-21T03:25:44Z
- **Authors**: Gabriel Dautovi, Jie JW Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.29143v1)