---
title: Fairness Auditing: Lower Bounds on Company Manipulation
published: 2026-08-01T10:11:20Z
authors: Rachit Verma, Padala Manisha, Sujit Gujar
url: http://arxiv.org/abs/2608.00568v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fairness Auditing: Lower Bounds on Company Manipulation

## Abstract
Fairness audits are increasingly mandated in high-stakes applications such as hiring, lending, and automated decision-making. Recent work has established fundamental impossibility results for black-box fairness auditing, showing that sufficiently expressive models can evade any auditing strategy. We complement these results by quantifying the extent of unavoidable post-audit manipulation under finite audit resources. We formulate fairness auditing as a min-max optimization between a computationally unbounded company and a budget-constrained auditor. We study two auditing regimes: (i) a budgeted auditor that certifies fairness using a fixed-size audit set, and (ii) a budgeted α-tolerant auditor that additionally requires the audit set to estimate the fairness of the certified model within an α approximation. For both settings, we derive explicit lower bounds on the worst-case post-audit demographic parity deviation as functions of the audit budget, group imbalance, and fairness tolerance. Finally, we empirically illustrate these theoretical limits using simple audit-set construction heuristics with linear and neural network classifiers. Our results demonstrate that increasing audit resources reduces, but does not eliminate, the scope for post-audit manipulation, highlighting fundamental limitations of finite-budget fairness certification.

## Metadata
- **Published**: 2026-08-01T10:11:20Z
- **Authors**: Rachit Verma, Padala Manisha, Sujit Gujar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00568v1)