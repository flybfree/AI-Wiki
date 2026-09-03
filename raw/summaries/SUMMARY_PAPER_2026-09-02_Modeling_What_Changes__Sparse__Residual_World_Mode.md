---
title: Modeling What Changes: Sparse, Residual World Models for Object-Centric Manipulation
url: http://arxiv.org/abs/2609.02046v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_03-20-09Z_ModelingWhatChanges_Sparse_ResidualWorldModelsforO.md
generated_at: 2026-09-02 20:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a sparse residual world model that explicitly tracks per-object changes instead of re‑predicting the entire scene. Experiments on a MuJoCo tabletop pushing benchmark show it is significantly more accurate and parameter‑efficient than dense models, especially when few objects move. The model also transfers well across object counts and performs well in planning scenarios.

## Key Takeaways
- The sparse/residual architecture reduces parameters from 8.6 to 11.1 times fewer while improving prediction accuracy by 2.5 to 4.6 times on the benchmark.
- Change‑detection F1 remains high (0.80–0.87) whereas dense baselines degrade, and transfer across object counts is retained at 99.4 percent F1 with no retraining.
- In autoregressive rollouts the sparse model hugs the no‑motion floor, limiting error accumulation compared to the drifting dense model.
- Sampling‑based planners fail with pure prediction models but succeed when using the sparse model featurized for visited states (0.23 success over three seeds), confirming planner soundness.

## Context
Object‑centric physical AI struggles with efficiency and interpretability because monolithic world models waste capacity on unchanged parts of a scene. This work demonstrates that focusing only on dynamic elements can yield better predictions, lower compute cost, and more robust planning without sacrificing accuracy.

## Implications
For robotics and simulation engineers, the sparse residual approach offers a practical bias for real‑time control and planning pipelines. By releasing code and data generators, the community can adopt this model to build scalable object‑centric AI systems that are both efficient and interpretable.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02046v1)
