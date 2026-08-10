---
title: GRASP: Reinforcing Language Model Anonymizers with Group Relative Policy Optimization
url: http://arxiv.org/abs/2608.06526v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-06_19-12-57Z_GRASP_ReinforcingLanguageModelAnonymizerswithGroup.md
generated_at: 2026-08-09 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces GRASP, a method that combines group relative policy optimization with self-refined anonymization to improve the privacy-utility trade-off in on‑device language model anonymizers. It replaces the DPO‑based baseline by training a single small model as both anonymizer and utility judge using an online reinforcement reward that hides personal attributes while preserving meaning. Experiments show GRASP matches or exceeds frontier models like Gemini 2.5 Flash and Claude, runs entirely offline, and reduces privacy leakage significantly.

## Key Takeaways
- The method trains a local model to simultaneously act as anonymizer, adversary, and utility judge using an online reinforcement reward that hides attributes while preserving meaning.
- GRASP improves the privacy‑utility trade-off over DPO-distilled baselines across three independent LLM judges.
- It removes substantially more private information than baseline methods and runs entirely on‑device at about 1% of GPT‑4o teacher cost.

## Context
Current language model anonymization relies on sending text to external servers for reinforcement learning, which defeats the purpose of privacy protection. Recent DPO approaches distill behavior offline but do not directly optimize the privacy-utility objective online. This work addresses those limitations by integrating a self-reinforcing policy that operates locally.

## Implications
For practitioners, GRASP enables truly private text processing without cloud dependency, reducing cost and exposure risk. The approach could be adopted in consumer apps to protect user data while maintaining utility, setting a new standard for on‑device LLM privacy solutions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06526v1)
