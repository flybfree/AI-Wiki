---
title: DelistBench: Evaluating Search-Enabled LLMs for Auditable Corporate-Event Database Completion
published: 2026-08-24T03:46:20Z
authors: Xuan Yao, Li Shuping, Dai Yang, Zhou Yi, Ke-Wei Huang
url: http://arxiv.org/abs/2608.22770v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DelistBench: Evaluating Search-Enabled LLMs for Auditable Corporate-Event Database Completion

## Abstract
Financial institutions need an independent way to detect missing, stale, and misclassified corporate-event records in vendor databases. We introduce Search-to-Record, a database-assurance task in which search-enabled large language models reconstruct institution-defined event records from public sources for a known security universe and historical cutoff, and DelistBench, a 1,200-record benchmark for security-level delisting announcements. We evaluate five models in paired closed-book and web-enabled conditions. Web access raises announcement-date accuracy within seven days by 34.0 to 48.0 percentage points and event-status accuracy by approximately 2.8 to 21.7 points; the best system achieves 81.5% overall joint accuracy within seven days. Economy web systems achieve 75.9-78.3% overall joint accuracy within seven days at 4.5-6.6% of the API cost of the most expensive web system. Risk-based triage identifies low-error subsets, although the highest-coverage operating point still sends 27.3% of the balanced test set to review. The evaluation identifies web retrieval as the main source of timing gains and shows that low-cost systems can approach the best system's accuracy. Together, Search-to-Record, DelistBench, and the evaluation provide concrete deployment guidance: calibrate triage to local event prevalence and market mix, preserve positive-event recall, and route positive and ambiguous cases to targeted review.

## Metadata
- **Published**: 2026-08-24T03:46:20Z
- **Authors**: Xuan Yao, Li Shuping, Dai Yang, Zhou Yi, Ke-Wei Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22770v1)