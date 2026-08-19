---
title: Cross-View Correspondence Is a Measurement Intervention: Two-Sided Validation for Agent Evaluation and Credit Assignment
published: 2026-08-18T12:39:21Z
authors: Zhen Zhang, Ahmad Hafez, Amr Alanwar
url: http://arxiv.org/abs/2608.17713v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cross-View Correspondence Is a Measurement Intervention: Two-Sided Validation for Agent Evaluation and Credit Assignment

## Abstract
Agent evaluations and trace-based learning often compare outputs across transformed views through a post-response correspondence treated as neutral preprocessing. We show that this correspondence is a measurement intervention: omitting it can manufacture sensitivity, an over-aggressive map can manufacture invariance, and multiple optimal correspondences can leave mechanism labels and signed learning credit unidentified. We develop a validity theory and audit with three components: two-sided validation of nuisance removal and response preservation, all-optima identification of downstream conclusions, and uncertainty propagation after validity is established. We characterize the linear feasibility boundary for response-preserving nuisance removal, compute sharp ranges over exact-optimum correspondence sets, and give a distribution-free certificate that retains a credit coordinate only when all exact optima agree on its nonzero sign. Across public code and SQL pipelines, two deterministic optimal tracebacks disagree on temporal localization for 55.9% of 1,586 nonzero trajectory pairs; two frozen 800-rollout tool-use audits, including a task-and-seed-disjoint replication, expose exact-optimum reversals of intended turn-level credit, although a clean public quick-start subset shows none. A pre-registered transport gate failed on natural responses; frozen corrected and held-out controls then show that a map calibrated only on benign examples erases every retained harmful response, while two-sided validation selects response-preserving alternatives. Cross-view correspondence must therefore be declared, validated, and propagated into uncertainty before agent evaluation or credit assignment supports a point conclusion.

## Metadata
- **Published**: 2026-08-18T12:39:21Z
- **Authors**: Zhen Zhang, Ahmad Hafez, Amr Alanwar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17713v1)