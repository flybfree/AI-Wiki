---
title: SCOPE: Synthetic Conditional Objectives for Policy Evolution in Black-Box Combinatorial Optimization
published: 2026-07-30T03:42:18Z
authors: Nguyen Viet Tuan Kiet, Nguyen Huu Duc, Le Cong Bang, Tran Cong Dao, Huynh Thi Thanh Binh
url: http://arxiv.org/abs/2607.27630v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SCOPE: Synthetic Conditional Objectives for Policy Evolution in Black-Box Combinatorial Optimization

## Abstract
Black-box combinatorial optimization requires systematically identifying high-quality solutions under a limited evaluation budget, yet the unknown objective function provides little guidance for deciding where the search should explore next. We introduce SCOPE, a general framework for Synthetic Conditional Objectives for Policy Evolution in Black-Box Combinatorial Optimization. Rather than directly optimizing the inaccessible objective, SCOPE learns a set of synthetic objectives conditioned on the accumulated search history, where each objective is designed to expose a distinct and potentially useful preference over candidate solutions. These objectives are then used to evolve search policies that generate diverse candidates, whose true quality is subsequently assessed through black-box evaluations. The outer loop adaptively updates and selects synthetic objectives according to how effectively their induced policies discover promising regions. In contrast, the inner loop returns a portfolio of top-performing policies to reduce the risk of relying on a single surrogate preference. This formulation reframes objective design as a mechanism for guiding policy exploration, enabling the search process to exploit observed evidence while maintaining structured diversity across discrete solution spaces. Extensive experiments across multiple benchmark problems demonstrate that SCOPE consistently improves black-box search performance under limited evaluation budgets and generalizes well across diverse combinatorial structures.

## Metadata
- **Published**: 2026-07-30T03:42:18Z
- **Authors**: Nguyen Viet Tuan Kiet, Nguyen Huu Duc, Le Cong Bang, Tran Cong Dao, Huynh Thi Thanh Binh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27630v1)