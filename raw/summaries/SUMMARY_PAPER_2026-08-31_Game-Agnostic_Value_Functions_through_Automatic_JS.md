---
title: Game-Agnostic Value Functions through Automatic JSON Feature Extraction
url: http://arxiv.org/abs/2608.30056v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-30_21-45-36Z_Game_AgnosticValueFunctionsthroughAutomaticJSONFea.md
generated_at: 2026-08-31 22:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces JSON-Bag VF, a game-agnostic method for training value functions using JSON-Bag prototypes from game trajectories. It demonstrates that Random Forest feature selection and stage-specific feature selection enhance performance compared to baseline OSLA agents. The analysis shows feature selection is the most important factor improving JSON-Bag VF.

## Key Takeaways
- Feature selection via Random Forest markedly improves JSON-Bag VF, outperforming agents without it.
- Stage-specific feature selection further boosts performance beyond generic prototypes.
- JSON-Bag OSLA surpasses baseline OSLA in most of the six tabletop games tested.

## Context
Game‑playing AI research often relies on game‑specific representations that limit generalization. This work proposes a universal approach using tokenized JSON descriptions, enabling agents to learn value functions across diverse titles without domain adaptation. The integration of automated feature selection aligns with trends toward efficient and interpretable model design in reinforcement learning.

## Implications
Practitioners can adopt JSON-Bag VF as a lightweight alternative to handcrafted features for rapid prototyping. By emphasizing feature selection, the method offers insights into which attributes drive value estimation, supporting more transparent AI systems. The findings may inspire broader adoption of generic trajectory representations in multi‑game environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30056v1)
