---
title: FUSE: Feature-Wise Unified Specialization with Cross-Column Exchange for Mixed-Type Tabular Flow Matching
published: 2026-08-07T14:50:12Z
authors: Suman Cha, Seongchan Lee, Dohyun Ko, Hyunjoong Kim
url: http://arxiv.org/abs/2608.07294v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FUSE: Feature-Wise Unified Specialization with Cross-Column Exchange for Mixed-Type Tabular Flow Matching

## Abstract
Generating mixed-type tabular data requires jointly modeling diverse feature distributions and their complex cross-column dependencies. Variational flow matching handles distinct endpoints via factorized distributions, yet leaves feature-specific processing and cross-column interactions implicit within a shared backbone. We introduce Feature-wise Unified Specialization with cross-column Exchange (FUSE) to explicitly separate these roles. FUSE applies separate adaptive mixture modules to numerical and categorical features, allowing each feature to combine shared specialized subnetworks, while joint attention preserves information exchange across all columns. We also characterize the excess population risk from restricted conditioning contexts and bound the continuous Wasserstein generation error by endpoint-prediction risk. Comprehensive experiments on eight tabular datasets demonstrate that FUSE achieves strong and consistent performance across distributional fidelity and downstream utility metrics.

## Metadata
- **Published**: 2026-08-07T14:50:12Z
- **Authors**: Suman Cha, Seongchan Lee, Dohyun Ko, Hyunjoong Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07294v1)