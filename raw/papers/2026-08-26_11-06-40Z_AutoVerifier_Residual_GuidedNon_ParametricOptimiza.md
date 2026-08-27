---
title: AutoVerifier: Residual-Guided Non-Parametric Optimization for Reference-Based Answer Verification
published: 2026-08-26T11:06:40Z
authors: Zebei Zhao, Zhihao Shi, Minqi Shi
url: http://arxiv.org/abs/2608.25637v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AutoVerifier: Residual-Guided Non-Parametric Optimization for Reference-Based Answer Verification

## Abstract
Reference-based verifiers are important for evaluating reasoning models and providing accurate outcome rewards in reinforcement learning with verifiable rewards. To improve verification accuracy, prior work has explored rule-based, model-based, and tool-augmented verifiers for checking answer equivalence across diverse answer forms. However, the equivalence of answer forms such as $1+3.14$ and $1+π$ may depend on the question and scoring criterion. We frame such implicit assumptions as verifier inductive biases. To address this challenge, we propose AutoVerifier, a residual-guided non-parametric optimization method that learns these biases from recurring verifier errors. Specifically, AutoVerifier records these biases in rule cards and promotes them to code modules or prompt guidance only after replay validation detects no direct regressions, keeping accepted updates auditable, editable, and reusable. Experiments on four verifier benchmarks demonstrate that AutoVerifier outperforms state-of-the-art verifiers by a large margin.

## Metadata
- **Published**: 2026-08-26T11:06:40Z
- **Authors**: Zebei Zhao, Zhihao Shi, Minqi Shi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25637v1)