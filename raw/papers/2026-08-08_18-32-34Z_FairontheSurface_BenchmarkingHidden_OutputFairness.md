---
title: Fair on the Surface? Benchmarking Hidden-Output Fairness Gaps in LLM Recommenders
published: 2026-08-08T18:32:34Z
authors: Chan Aristella Lu, Arya Fayyazi, Junhao Zhang, Saeid Shokoufa, Yue Xing, Zhen Xiang, Kyu Hyung Lee, Mehdi Kamal, Massoud Pedram
url: http://arxiv.org/abs/2608.08284v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fair on the Surface? Benchmarking Hidden-Output Fairness Gaps in LLM Recommenders

## Abstract
Fairness audits for LLM-based recommenders have largely focused on observable outputs, implicitly assuming that stable recommendations reflect stable internal processing. We challenge this assumption with FairGap, the first benchmark to jointly evaluate recommendation fairness at two levels: observable output shift (OBS) and hidden representation shift (IBS), measured through controlled counterfactual identity probes across gender, age, and race. Their relationship is summarized via Representation-Output Alignment (ROA), with quadrant diagnostics for identifying user-level hidden-output mismatch. Applied to six open-weight LLM families across three domains, FairGap reveals pervasive hidden-output decoupling: ROA rarely exceeds 0.22, and a non-negligible user population shows stable outputs despite substantial internal shifts, a mode that output-only audits cannot detect by design. Further, activation steering that reduces IBS by up to 8x simultaneously worsens OBS, demonstrating a fundamental tension between internal and output-level fairness that existing frameworks are unequipped to diagnose.

## Metadata
- **Published**: 2026-08-08T18:32:34Z
- **Authors**: Chan Aristella Lu, Arya Fayyazi, Junhao Zhang, Saeid Shokoufa, Yue Xing, Zhen Xiang, Kyu Hyung Lee, Mehdi Kamal, Massoud Pedram
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08284v1)