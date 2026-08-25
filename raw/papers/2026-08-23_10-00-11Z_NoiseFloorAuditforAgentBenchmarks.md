---
title: Noise Floor Audit for Agent Benchmarks
published: 2026-08-23T10:00:11Z
authors: Yihang Chen, Pin Qian, Su Wang, Chong Peng, Huan Xu, Xiyang Wu, Yiqi Sun
url: http://arxiv.org/abs/2608.22331v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Noise Floor Audit for Agent Benchmarks

## Abstract
We audit measurement variability for 3 native tool-calling endpoints across 2 providers on the official BFCL multiple and parallel categories, using matched AST grading. At temperature 0, reruns are nearly deterministic across Groq endpoints and a thinking-enabled Gemini setting: ever-flip fractions are 0.7%, 2.0%, and 2.7%, with mean run correlations of 0.997, 0.966, and 0.961. Semantics-preserving prompt perturbations create the larger floor on all endpoints, with median perturbation paired SDs 11x to 58x larger than rerun paired SDs. The failure character also shifts: malformed-output failures account for 30%, 7%, and <1% of task failures, so marginal accuracy hides not only stability but also failure mode.

## Metadata
- **Published**: 2026-08-23T10:00:11Z
- **Authors**: Yihang Chen, Pin Qian, Su Wang, Chong Peng, Huan Xu, Xiyang Wu, Yiqi Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22331v1)