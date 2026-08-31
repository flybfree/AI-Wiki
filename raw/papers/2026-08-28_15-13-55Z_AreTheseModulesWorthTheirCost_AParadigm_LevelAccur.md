---
title: Are These Modules Worth Their Cost? A Paradigm-Level Accuracy-Cost Analysis of In-context Learning Text-to-SQL
published: 2026-08-28T15:13:55Z
authors: Jiayan Lin, Yujia Liu, Zijin Hong, Zheng Yuan, Yilin Xiao, Hao Chen, Qinggang Zhang, Xiao Huang, Feiran Huang
url: http://arxiv.org/abs/2608.28432v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Are These Modules Worth Their Cost? A Paradigm-Level Accuracy-Cost Analysis of In-context Learning Text-to-SQL

## Abstract
Recent advances in in-context learning (ICL) text-to-SQL have substantially improved execution accuracy on public benchmarks by assembling increasingly elaborate pipelines around the base generator, yet existing studies typically report aggregate end-to-end accuracy, without quantifying the marginal accuracy-cost contribution of individual design choices. Consequently, providing a unified, paradigm-level cost-accuracy quantification remains a critical challenge for understanding and configuring modern text-to-SQL. To address this, we instantiate 17 paradigm-level configurations across five recurring modules of the ICL text-to-SQL pipeline under a single controlled implementation, and attribute each paradigm's marginal contribution and incurred cost across all four backbones spanning diverse capability levels and reasoning styles. Our analysis reveals that execution-feedback refinement is the only paradigm whose benefit holds universally at consistently low cost, while most other modules help only under backbone-dependent conditions. Token accounting shows that input demand is more closely tied to pipeline structure, whereas output demand is more sensitive to backbone generation behavior. Cross-module analysis further shows that stacking improves accuracy on most backbones, although how the gains compose varies with backbone capability. We also find that a fixed budget is often better spent engineering a more elaborate pipeline over a mid-tier backbone than upgrading to a frontier model with a lean pipeline. These findings distill into an actionable, cost-aware tiered guideline that transfers to five additional backbones without per-paradigm search.

## Metadata
- **Published**: 2026-08-28T15:13:55Z
- **Authors**: Jiayan Lin, Yujia Liu, Zijin Hong, Zheng Yuan, Yilin Xiao, Hao Chen, Qinggang Zhang, Xiao Huang, Feiran Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28432v1)