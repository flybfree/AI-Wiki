---
title: dtControl2+$\varepsilon$: Trading Optimality for Explainability in MDPs via Decision Trees
url: http://arxiv.org/abs/2607.25925v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_16-15-11Z_dtControl2___varepsilon__TradingOptimalityforExpla.md
generated_at: 2026-07-28 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a new extension of dtControl2 called dtControl2+ε that allows constructing smaller decision trees while preserving ε‑optimality in Markov decision processes. By allowing an imprecision level ε, the method trades off some detail for simplicity and guarantees that the resulting tree remains within ε of the optimal policy. The tool produces explanations orders of magnitude simpler than existing approaches.

## Key Takeaways
- The construction yields a decision tree whose size is reduced by many orders of magnitude compared to dtControl2 while still satisfying an ε‑optimality constraint.
- The method explicitly trades off detail for simplicity, enabling users to control the amount of explanation provided.
- Missing only a single crucial case can be tolerated as long as the overall error stays within the chosen ε.

## Context
Decision trees are widely used to make AI policies interpretable because they are easy to visualize and reason about. However, large or complex environments generate trees that become unwieldy and hard for humans to understand. The trade‑off between expressiveness and simplicity remains a central challenge in explainable reinforcement learning.

## Implications
This work provides practitioners with a practical way to generate concise policy explanations without sacrificing too much performance. By offering tunable imprecision, it can be applied across industries where both safety and interpretability are critical, such as autonomous driving or healthcare robotics. The approach may inspire future research on compact yet reliable model representations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25925v1)
