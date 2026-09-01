---
title: Automated Testing of LLM-Based Post Hoc Explainers Using Model Checking as an Oracle
published: 2026-08-31T10:54:37Z
authors: Dennis Gross, Helge Spieker
url: http://arxiv.org/abs/2608.30581v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Automated Testing of LLM-Based Post Hoc Explainers Using Model Checking as an Oracle

## Abstract
Large language models (LLMs) are used as post hoc explainers of sequential decision-making policies, producing natural-language explanations of why an action was chosen. However, LLMs often generate plausible but incorrect statements, and no existing approach systematically tests whether such explanations are faithful to the underlying environment. Two classic software testing challenges stand in the way: there is no oracle for the correctness of an explanation, and the test inputs, natural language queries about a policy's behavior, lack the structure needed for systematic test case generation. We address both. Probabilistic model checking provides the test oracle, computing exact reference results against which LLM answers are graded automatically. A taxonomy of post hoc query categories structures the input space around the environment-level facts from which policy explanations are composed; test cases generated from it are prioritized by question-specific diagnostic difficulty scores. Across seven MDP environments, the testing separates three open-weight LLMs: a reasoning model passes 85% of test cases, a mid-size model 70%, and a 1B model falls below the random baseline, while prioritization surfaces significantly harder cases than random selection. Our results indicate how trustworthy LLM-generated explanations are in model-free settings, where the same LLMs are used but no oracle exists to verify them.

## Metadata
- **Published**: 2026-08-31T10:54:37Z
- **Authors**: Dennis Gross, Helge Spieker
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30581v1)