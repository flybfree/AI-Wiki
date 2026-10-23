---
title: HERD: Harness-Evolving Recursive Distillation for Continual Learning
published: 2026-10-22T15:03:20Z
authors: Xun Sun, Thanh Thi Nguyen, Thuy-Trang Vu
url: http://arxiv.org/abs/2610.31401v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HERD: Harness-Evolving Recursive Distillation for Continual Learning

## Abstract
Continual learning requires a model to keep acquiring new skills and knowledge without compromising its existing capabilities. Parametric methods suffer from catastrophic forgetting and loss of plasticity. Non-parametric methods, such as prompts, skills, and harnesses, leverage in-context learning but are limited by context length and lossy plain-text compression. To effectively combine their complementary strengths, we propose HERD (Harness-Evolving Recursive Distillation), a hybrid continual learning framework that learns efficiently in the harness and internalizes experience into cumulative capabilities via distillation. On the harness side, HERD continually refines its skills to capture reusable patterns, while retaining high-residual examples that the skills fail to capture in a bounded memory. On the parameter side, HERD performs drift-constrained distillation with dual anchors, substantially reducing forgetting over long recursive runs. On the 25-stage task stream of TRACE+17, under fixed memory and compute budgets, HERD matches the strongest parametric baseline in new-task acquisition while exhibiting the least forgetting and the strongest retention of general capabilities.

## Metadata
- **Published**: 2026-10-22T15:03:20Z
- **Authors**: Xun Sun, Thanh Thi Nguyen, Thuy-Trang Vu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.31401v1)