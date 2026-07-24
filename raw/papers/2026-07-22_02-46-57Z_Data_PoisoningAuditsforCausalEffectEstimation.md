---
title: Data-Poisoning Audits for Causal Effect Estimation
published: 2026-07-22T02:46:57Z
authors: Kwangho Kim
url: http://arxiv.org/abs/2607.19692v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Data-Poisoning Audits for Causal Effect Estimation

## Abstract
Observational causal analyses increasingly pool records across sites, vendors, and collection systems, creating vulnerability to append-only attacks in which plausible records are strategically selected to alter a reported treatment effect. We develop a data-poisoning audit for augmented inverse-probability-weighted estimation. The analyst specifies a finite catalog of feasible records, an append budget, and nested source capacities, and the adversary selects a feasible subset to maximize movement in a prespecified direction. With preprocessing and nuisance fits held fixed, we propose a greedy scan that computes the exact finite-sample worst-case movement at every append budget. To account for nuisance refitting, we go on to derive a total-influence score combining each record's direct contribution with its effect through the propensity and outcome models. We further obtain a conservative finite-budget bound for the fully refitted estimate. Extensive simulations validate the exact result and show that total influence improves local refit prediction, while multisite and public-data analyses demonstrate material sensitivity at small append budgets. By translating adversarial data-composition risk into movement curves and critical budgets, the framework supports more reliable causal reporting and the design of source-level safeguards.

## Metadata
- **Published**: 2026-07-22T02:46:57Z
- **Authors**: Kwangho Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19692v1)