---
title: LintEval: Benchmarking LLMs on Linter-Guided File Refactoring
published: 2026-10-14T11:36:55Z
authors: Tongwei Deng, Jinyu Zhu, Yue Cao, Chenxu Wang, Yanzhen Zou, Bing Xie
url: http://arxiv.org/abs/2610.20027v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LintEval: Benchmarking LLMs on Linter-Guided File Refactoring

## Abstract
Linters are widely used in code maintenance and real-time IDE editing to surface lint alerts related to performance, style, error-prone, and other patterns in source files. However, existing code benchmarks do not explicitly evaluate linter-guided file refactoring, where models must reduce lint alerts in source files with correct initial functionality while satisfying functionality preservation. We introduce LintEval, a multilingual benchmark for linter-guided file refactoring across C++, Python, and Java, comprising 13,061 programs with correct initial functionality and 171,662 lint alerts extracted using language-specific linters. LintEval jointly evaluates functionality preservation, lint alert reduction, new alert avoidance, and edit minimality. Experiments reveal a persistent trade-off: closed-source commercial models reach up to 90.4% Reduction@P but achieve only 67.1%-68.3% Pass@1, while several open-source small models show low or negative Reduction@P. A controlled fine-tuning study further shows that supervision format matters: refactoring-oriented SFT raises Qwen2.5-Coder-7B Reduction@P from 24.7% to 76.0%. LintEval enables controlled evaluation of models that improve source files under functionality preservation.

## Metadata
- **Published**: 2026-10-14T11:36:55Z
- **Authors**: Tongwei Deng, Jinyu Zhu, Yue Cao, Chenxu Wang, Yanzhen Zou, Bing Xie
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.20027v1)