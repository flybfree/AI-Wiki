---
title: Belief-Calibrated Optimization: An Explicit World Model for Agentic Optimization
url: http://arxiv.org/abs/2609.01861v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-01_20-47-04Z_Belief_CalibratedOptimization_AnExplicitWorldModel.md
generated_at: 2026-09-02 20:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes Belief-Calibrated Optimization (BCO), a method that records the coding agent’s belief about how the environment will respond to edits as an explicit persistent in‑context document. By continuously revising this world model, BCO enables agents to select better candidates than those driven only by scores and traces. On five benchmarks it achieves higher train passrates than a control lacking only the world model.

## Key Takeaways
- The belief about environment response is written down as a persistent in‑context document rather than remaining implicit in reasoning or parameters.
- BCO’s world model is continuously revised with each candidate evaluation, forming a coherent account of how edits affect outcomes.
- After a target‑model swap the BCO scaffold outperforms other scaffolds except when context windows overflow.

## Context
Current LLM agents rely on frozen models and coding loops that lack explicit knowledge of how their actions will be judged. This paper shows that making this belief explicit can close performance gaps across diverse tasks.

## Implications
For practitioners, BCO suggests a simple yet powerful way to improve agentic optimization without retraining the model. The reusable document could inform future adaptive systems where environment dynamics shift over time.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01861v1)
