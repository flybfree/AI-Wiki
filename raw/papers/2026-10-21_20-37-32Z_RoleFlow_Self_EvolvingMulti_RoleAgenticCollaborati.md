---
title: RoleFlow: Self-Evolving Multi-Role Agentic Collaboration via Structural Adaptation
published: 2026-10-21T20:37:32Z
authors: Yi Ge, Pan Wang, Xuehao Cui, Zian Zeng, Xu Hu, Heng Huang, Furong Huang
url: http://arxiv.org/abs/2610.30429v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RoleFlow: Self-Evolving Multi-Role Agentic Collaboration via Structural Adaptation

## Abstract
Large language model (LLM) based multi-agent systems often rely on predefined collaboration structures, limiting their adaptability to evolving task requirements. Although recent approaches enable dynamic orchestration, trajectory-level rewards they apply assign one outcome to each decision, ofen struggling to identify the contributions of individual structural changes. We propose RoleFlow, a self-evolving multi-role agentic system that refines collaboration structures through feedback-driven atomic edits and on-demand role synthesis. To make structural adaptation learnable, we introduce Single-Edit Counterfactual Policy Optimization (SECPO), which evaluates each edit against its no-edit counterpart at the same chain state and assigns targeted credit to edit-specific tokens. Across seven benchmarks spanning four domains, RoleFlow achieves the optimal average performance, surpassing the strongest competitor by 4.7 points. It leads on all three multi-hop QA benchmarks by 3.2-7.5 F1 points and also shows supremacy on mathematical reasoning, web interaction, and code generation. Further analyses demonstrate cross-benchmark transferability, training-data efficiency, and cross-executor generalization.

## Metadata
- **Published**: 2026-10-21T20:37:32Z
- **Authors**: Yi Ge, Pan Wang, Xuehao Cui, Zian Zeng, Xu Hu, Heng Huang, Furong Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.30429v1)