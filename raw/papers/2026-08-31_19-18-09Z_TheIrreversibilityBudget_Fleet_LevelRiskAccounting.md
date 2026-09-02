---
title: The Irreversibility Budget: Fleet-Level Risk Accounting and Admission Control for Agent Operating Systems
published: 2026-08-31T19:18:09Z
authors: Bardia Mohammadi, Laurent Bindschaedler
url: http://arxiv.org/abs/2609.00275v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Irreversibility Budget: Fleet-Level Risk Accounting and Admission Control for Agent Operating Systems

## Abstract
Fleets of LLM agents now externalize effects that cannot be fully undone: they move money, deploy code, delete data, and disclose information. Current controls check one effect at a time, so a fleet of individually authorized agents can overdraw its principal's risk under a shared trigger while every local gate stays correct. We propose the irreversibility budget, a cumulative account of residual value-at-risk that a trusted runtime maintains for each principal across agents, workflows, and tenants. Treating irreversibility as a first-class resource, the runtime charges each effect its residual loss below the agent and denies the marginal effect once the aggregate would overdraw the budget. Getting the price right is hard, because effects are heterogeneous, adversarially declared, and correlated. We perform a controlled study in which per-effect gates admit fleet-level overdraws of up to 48 times the tenant's risk limit while the budget holds every correctly charged run within that limit. Conservative, dependency-aware pricing remains the central open problem for a deployable design.

## Metadata
- **Published**: 2026-08-31T19:18:09Z
- **Authors**: Bardia Mohammadi, Laurent Bindschaedler
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00275v1)