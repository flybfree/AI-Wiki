---
title: Fair ASR: Re-Evaluating Black-Box Jailbreaks under Shared Target-Call Budgets
published: 2026-08-18T04:26:39Z
authors: Zhida He, Xiaoyu Wen, Han Qi, Ziyuan Zhou, Peng Yu, Jiajia Li, Chaochao Lu, Qiaosheng Zhang
url: http://arxiv.org/abs/2608.17360v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fair ASR: Re-Evaluating Black-Box Jailbreaks under Shared Target-Call Budgets

## Abstract
Reliable jailbreak evaluation is essential for assessing LLM safety, but most existing studies rely solely on attack success rate (ASR) without accounting for its dependence on attack budgets, resulting in unfair comparisons across methods. Existing compute-aware evaluations reduce heterogeneous resources into FLOPs, which is difficult to estimate for black-box models and fails to capture resource-specific constraints. To provide a comparable evaluation basis, we introduce Fair-ASR, an evaluation protocol for black-box jailbreak attacks under shared target-call budgets B, using target calls as a directly observable and method-agnostic comparison axis while tracking attacker calls separately for efficiency analysis. We re-evaluate 11 representative attacks under the Fair-ASR protocol and find that attack rankings change substantially across target-call budgets, simple stochastic perturbations and hand-crafted templates remain highly competitive under equal target access, and no evaluated LLM-driven method is efficient in both target and attacker calls. Motivated by this efficiency gap, we introduce ReCode, a compositional budget-efficient attack that combines desensitization rewriting with two effective low-cost primitives identified by Fair-ASR. Under a budget of 20 target calls, ReCode achieves 85% ASR on GPT-5 while requiring only 7.19 attacker calls per request on average, showing strong efficiency in both target and attacker calls.

## Metadata
- **Published**: 2026-08-18T04:26:39Z
- **Authors**: Zhida He, Xiaoyu Wen, Han Qi, Ziyuan Zhou, Peng Yu, Jiajia Li, Chaochao Lu, Qiaosheng Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17360v1)