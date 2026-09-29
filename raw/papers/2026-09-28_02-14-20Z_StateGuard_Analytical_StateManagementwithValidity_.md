---
title: StateGuard: Analytical-State Management with Validity-Aware Intervention for Long-Horizon Data Agents
published: 2026-09-28T02:14:20Z
authors: Wenle Liao, Zhao Wang, Jingchao Zhang, Jiajie Jin, Yimeng Xu, Zhicheng Dou
url: http://arxiv.org/abs/2609.34134v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# StateGuard: Analytical-State Management with Validity-Aware Intervention for Long-Horizon Data Agents

## Abstract
LLM-based agents have shown strong capabilities in automated data analysis and are increasingly moving toward long-horizon, multi-stage analytical workflows. However, as the analytical process evolves, constraints, variables, and conclusions remain implicitly embedded in interaction histories, making it difficult for agents to track which analytical artifacts remain valid over increasingly long horizons and changing dependencies. Consequently, stale artifacts may be silently inherited, propagating errors to downstream stages. To address this challenge, we propose StateGuard, an analytical-state validity management framework for long-horizon data agents. StateGuard externalizes evolving analytical progress into a state graph containing constraints, versioned variables, intermediate conclusions, and cross-state relations, treating each state as an executable, verifiable, and traceable object rather than textual memory alone. StateGuard maintains state validity through evidence-grounded verification and hierarchical intervention. To equip StateGuard with these capabilities, we first introduce Manager-Oriented Counterfactual Supervision, which constructs 3K state-centric trajectories through counterfactual runtime synthesis to fine-tune StateGuard for state maintenance, verification, and repair. We then apply Validity-Guided Policy Optimization, using runtime validity evidence to provide fine-grained learning signals for protocol correctness, state grounding, and intervention quality. Experiments on three diverse long-horizon data-analysis benchmarks show that StateGuard consistently improves data-agent performance while reducing dependency-induced downstream error propagation, demonstrating the advantages of explicit analytical-state management for reliable long-horizon data analysis.

## Metadata
- **Published**: 2026-09-28T02:14:20Z
- **Authors**: Wenle Liao, Zhao Wang, Jingchao Zhang, Jiajie Jin, Yimeng Xu, Zhicheng Dou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34134v1)