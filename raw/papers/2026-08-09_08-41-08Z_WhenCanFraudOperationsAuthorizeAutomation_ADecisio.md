---
title: When Can Fraud Operations Authorize Automation? A Decision-Support Framework for Fresh Audit Evidence and Review Workload
published: 2026-08-09T08:41:08Z
authors: Jie Deng
url: http://arxiv.org/abs/2608.08577v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Can Fraud Operations Authorize Automation? A Decision-Support Framework for Fresh Audit Evidence and Review Workload

## Abstract
Fraud operations must allocate events among automatic approval, analyst review, and automatic blocking even though the labels needed to evaluate these actions are selective and delayed. Predictive scores order cases, but they do not show whether the evidence is current and representative enough to delegate an action to the model. We develop freshness-constrained audit capacity (FCAC), a decision-support framework that treats automation as an authorization decision constrained by action risk, evidence freshness, and shared review capacity. It evaluates candidate action regions from mature randomized audits and a prespecified temporal allowance. Supported regions are automated; unsupported regions remain in review. The resulting decision record reports evidence age, audit demand, total review workload, value exposure, and compatible temporal change. We show that current action risk is unidentified without restricting unobserved label evolution. Under representative randomized audits, label-independent evidence windows, and a prespecified condition linking historical and current action risk, we derive simultaneous finite-sample control of unsafe authorization. Chronological evaluations with simulated audits on IEEE-CIS, ULB-Worldline, and Elliptic++ yield zero-drift automation rates of 84.4%, 67.4%, and 81.3%, with total review workloads of 24.1%, 46.0%, and 43.1%. The experiments reveal an audit-capacity trade-off: sparse auditing delays authorization, whereas intensive auditing eventually increases workload. A separately specified BAF stress test further indicates that fallback thresholds must reflect candidate-specific evidence rather than a common fraction of the risk limit. These findings identify audit freshness and analyst capacity as joint design considerations for fraud decision support.

## Metadata
- **Published**: 2026-08-09T08:41:08Z
- **Authors**: Jie Deng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08577v1)