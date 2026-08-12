---
title: Observational Policy Ranking for SMB Financial Guidance from Multi-Action Accounting Logs
published: 2026-08-10T14:46:10Z
authors: Shrutendra Harsola, Vignesh Subrahmaniam, Vikas Raturi, Kamalika Das, Xiang Gao, Kratika Gupta, Ruocheng Guo, Padmaja Jonnalagedda, Ananya Pramod, Sricharan Kumar
url: http://arxiv.org/abs/2608.10050v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Observational Policy Ranking for SMB Financial Guidance from Multi-Action Accounting Logs

## Abstract
Small and medium-sized businesses need timely financial guidance, yet historical accounting logs record self-selected and often co-occurring business changes rather than randomized recommendations. We formulate this setting as observational policy ranking: from pre-decision financial information, a policy selects one of 34 ledger-derived business-change categories for a target financial KPI. Using 85,078 company-month observations from 7,505 firms, we introduce Covariate-Adjusted Residual Policy Learning (CAR-PL), an action-wise R-learner that operates directly on multi-hot logs and regularizes selection by observational support. We compare CAR-PL with an uplift T-Learner, a conservative contextual value model, a zero-shot LLM, and non-personalized references on company-disjoint held-out firms under a shared model-assisted scoring rule. CAR-PL has the highest Gross Profit point estimate (0.084), the T-Learner has the highest Revenue point estimate (0.085), and the contextual value model has the highest Quick Ratio point estimate (0.062). CAR-PL and the T-Learner are not statistically separated on either growth KPI in matched company-clustered comparisons, while CAR-PL selects 33-34 categories and produces less concentrated selections across the catalog. Outcome-model-only scoring retains the same KPI-level point-estimate leader or top pair, and category rankings remain similar when the all-zero treatment reference is replaced by the most common training co-action pattern. These findings support objective-specific ranking of SMB financial guidance from multi-action accounting logs.

## Metadata
- **Published**: 2026-08-10T14:46:10Z
- **Authors**: Shrutendra Harsola, Vignesh Subrahmaniam, Vikas Raturi, Kamalika Das, Xiang Gao, Kratika Gupta, Ruocheng Guo, Padmaja Jonnalagedda, Ananya Pramod, Sricharan Kumar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10050v1)