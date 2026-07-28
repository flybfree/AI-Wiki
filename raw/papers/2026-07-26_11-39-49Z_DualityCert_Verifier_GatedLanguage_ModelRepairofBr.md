---
title: DualityCert: Verifier-Gated Language-Model Repair of Broken Duality Claims in Quantum Field Theory
published: 2026-07-26T11:39:49Z
authors: Xingyang Yu
url: http://arxiv.org/abs/2607.23614v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DualityCert: Verifier-Gated Language-Model Repair of Broken Duality Claims in Quantum Field Theory

## Abstract
We present DualityCert, a symbolic verifier for candidate Seiberg-duality claims in four-dimensional N=1 quiver gauge theories. The verifier evaluates 't Hooft anomaly matching, superpotential R-charge consistency, central-charge matching, and a bounded chiral-ring proxy. A claim that passes receives a consistency certificate, which states that no tested inconsistency was found, not that the duality is proven. We use the verifier as a repair environment for language-model agents, which receive a deliberately broken claim and must edit it until it certifies. On a preregistered benchmark of 145 broken claims, with the analysis fixed before the first confirmatory model call, verifier-gated retry improves final repair success over a single attempt by +8.3 percentage points (pp) on deepseek-chat and +7.1 pp on qwen-plus (Holm-adjusted p<0.002). Under an equal budget of eleven attempts, the stop-first strategy portfolio underperforms independent verifier-filtered resampling by 10.3 percentage points on deepseek-chat but outperforms it by 14.7 points on qwen-plus, reversing the ordering of the two tested verifier-exploitation policies across the two confirmatory models. On qwen-plus, category-level verifier feedback is worth +8.7 pp over content-free retry, and interpretable obligation identities alone are worth +6.4 pp over structurally identical masked feedback. Neither effect is detected on deepseek-chat. Separately, a preregistered MiniMax-M2.5 extension again finds an iteration gain and independent verifier-filtered resampling outperforming the strategy portfolio. Which policy is better thus differs between the two models, while every winning policy uses the same cheap certificate. The verifier, benchmark, protocol, and all per-attempt records are released.

## Metadata
- **Published**: 2026-07-26T11:39:49Z
- **Authors**: Xingyang Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23614v1)