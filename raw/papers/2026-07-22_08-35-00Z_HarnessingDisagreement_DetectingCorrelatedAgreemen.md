---
title: Harnessing Disagreement: Detecting Correlated Agreement Blindness in Multi-Agent Triage
published: 2026-07-22T08:35:00Z
authors: Shay Seiya McDonnell, Avantika Singh, Quoc-Viet Pham, Vratislav Havlik, Gregory M. P. O'Hare
url: http://arxiv.org/abs/2607.19899v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Harnessing Disagreement: Detecting Correlated Agreement Blindness in Multi-Agent Triage

## Abstract
Disagreement-triggered escalation can create a structural blind spot in multi-agent arbitration: as base learners improve, they tend to converge, weakening safety monitoring where correlated failures concentrate. We term this correlated agreement blindness and present ARAT (Arbitrated Reasoning Agents for Alarm Triage), a directed-star system combining an inductive Random Forest (RF) agent, an analogical case-based k-nearest neighbour (k-NN) agent, and a calibrated meta-model to mitigate this effect. On 82,332 holdout samples from the UNSW-NB15 network intrusion detection dataset, 57.2% of errors occur under agreement and 90.6% of dangerous under-predictions evade disagreement-based monitoring even after conservative override; ablation shows that strengthening base learners increases error correlation while reducing disagreement. ARAT reduces under-prediction relative to soft voting from 4.80% to 1.70% via conservative override (-2.6pp) and a safety-flag gate (-0.5pp), demonstrating architectural gains. Cross-dataset validation on clinical readmission supports these indicators, suggesting that diversification improves safety only when it generates productive disagreement rather than convergence. These results indicate that disagreement-triggered escalation can be blind to correlated failure, a risk that may intensify as agentic pipelines deploy increasingly capable, correlated models.

## Metadata
- **Published**: 2026-07-22T08:35:00Z
- **Authors**: Shay Seiya McDonnell, Avantika Singh, Quoc-Viet Pham, Vratislav Havlik, Gregory M. P. O'Hare
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19899v1)