---
title: DASH: Decoupled Adaptive Surrogate - Acquisition Harness for Automated Bayesian Optimization
published: 2026-08-01T12:53:34Z
authors: Changquan Zhao, Yuxiang Sun, Ruihao Zhu, Cheng Hua, Yulian He
url: http://arxiv.org/abs/2608.00641v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DASH: Decoupled Adaptive Surrogate - Acquisition Harness for Automated Bayesian Optimization

## Abstract
Bayesian optimization (BO) relies on a surrogate model and an acquisition function, yet the most suitable choices vary across tasks and optimization stages. Automated Bayesian optimization (AutoBO) addresses this variability by adapting BO components online. However, existing AutoBO methods either adapt one component, leaving the other mismatched and creating a bottleneck, or jointly select surrogate--acquisition pairs under a shared criterion, overlooking their distinct roles: surrogate selection depends on predictive reliability, whereas acquisition adaptation should respond to campaign context.In this paper, we propose DASH, a Decoupled Adaptive Surrogate--Acquisition Harness for large-language- model (LLM)-enhanced AutoBO. DASH selects surrogates by predictive reliability, uncertainty calibration, and ranking consistency; its two-stage acquisition controller periodically reallocates quotas across acquisition functions, builds a BO shortlist accordingly, and delegates final selection to an LLM. DASH also incorporates an integrated harness, consisting of knowledge-guided warm start and structured memory, to ground optimization in domain knowledge and accumulated feedback. Across four chemical optimization tasks, DASH outperforms the best AutoBO baseline by 12.51% in trajectory-level Acceleration Factor and 5.00% in endpoint Enhancement Factor. Results remain strong across LLM backbones, and ablations verify the complementary contributions of all components. Full-table and behavioral contamination checks find no detectable evidence that direct benchmark memorization or source-cell leakage explains these gains.

## Metadata
- **Published**: 2026-08-01T12:53:34Z
- **Authors**: Changquan Zhao, Yuxiang Sun, Ruihao Zhu, Cheng Hua, Yulian He
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00641v1)