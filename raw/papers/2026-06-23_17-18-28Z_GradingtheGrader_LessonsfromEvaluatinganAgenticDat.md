---
title: Grading the Grader: Lessons from Evaluating an Agentic Data Analysis System
published: 2026-06-23T17:18:28Z
authors: Tian Zheng, Kai-Tai Hsu
url: http://arxiv.org/abs/2606.24839v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Grading the Grader: Lessons from Evaluating an Agentic Data Analysis System

## Abstract
Agentic data analysis systems produce rich outputs, including code, numerical results, and verbal diagnostics. This makes them more challenging to evaluate than single-turn LLM responses. It is therefore necessary to distinguish genuine disagreement between an agent's output and a ground-truth answer from grading artifacts. We investigate how reliably automated graders assess such a system and what strategies improve grading quality by applying LAMBDA, a multi-agent data-analysis system, on 153 numerical QRData tasks from DSGym. We develop and evaluate a three-layer human-AI grading cascade: strict regex matching, LLM-based lenient grading, and snippet-based human inspection, which combines non-GenAI and GenAI strategies with different failure profiles. Both automated graders achieve 100% observed precision (0/70 false positives). The lenient grader's recall is 97% against human labels. A keyword-anchored extraction pipeline raises the strict grader's recall by 60 percentage points over a last-number heuristic; the lenient grader is architecturally parser-independent. An iterative nudge mechanism raises grading run success from 36% to 97% and lenient-pass rates from 16% to 46%; comparing nudging with and without original-question re-injection shows that re-injection offers no benefit, confirming the nudge as an answer template cue. We further observe in this case study that variable type is the task metadata field most consistently associated with grading pipeline dynamics and observed outcome grades.

## Metadata
- **Published**: 2026-06-23T17:18:28Z
- **Authors**: Tian Zheng, Kai-Tai Hsu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.24839v1)