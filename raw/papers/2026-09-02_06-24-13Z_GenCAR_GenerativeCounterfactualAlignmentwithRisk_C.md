---
title: GenCAR: Generative Counterfactual Alignment with Risk-Controlled Selection for Out-of-Distribution Recommendation
published: 2026-09-02T06:24:13Z
authors: Qianqian Wang, Yunshan Li, Jiawen Zeng, Wenwu Gong, Lili Yang
url: http://arxiv.org/abs/2609.02162v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GenCAR: Generative Counterfactual Alignment with Risk-Controlled Selection for Out-of-Distribution Recommendation

## Abstract
Serving useful recommendations under distribution shift is crucial for balancing utility and risk in out-of-distribution (OOD) recommendation. However, most existing OOD methods improve ranking or construct counterfactual candidates without controlling the proxy-label false discovery rate (FDR) of the served set. In this work, we formulate OOD serving as the $α$-Valid Counterfactual Recommendation ($α$-VCR) problem to retain candidate support learned from counterfactual supervision while controlling proxy-label FDR, and propose GenCAR, which couples preference-grounded counterfactual supervision with calibrated set selection. In particular, GenCAR fixes the stable-preference representation while intervening on the environmental factor, grounds offline large language model proposals through preference anchors and trust-radius filtering, and uses conformal $p$-values for Benjamini--Hochberg selection. We theoretically bound conditional counterfactual approximation error and prove finite-sample, distribution-free control of proxy-label FDR under exchangeability and positive regression dependence, with a Benjamini--Yekutieli guarantee under arbitrary dependence. Extensive experiments audit realized proxy false discovery proportions and demonstrate that GenCAR consistently enhances OOD candidate recovery across diverse benchmarks.

## Metadata
- **Published**: 2026-09-02T06:24:13Z
- **Authors**: Qianqian Wang, Yunshan Li, Jiawen Zeng, Wenwu Gong, Lili Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02162v1)