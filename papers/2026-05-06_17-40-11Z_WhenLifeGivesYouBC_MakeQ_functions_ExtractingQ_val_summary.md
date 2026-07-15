---
title: "Summary: When Life Gives You BC, Make Q-functions: Extracting Q-values from Behavior Cloning for On-Robot Reinforcement Learning"
date: 2026-05-06
tags: ['paper', 'research', 'ai']
---
# When Life Gives You BC, Make Q-functions: Extracting Q-values from Behavior Cloning for On-Robot Reinforcement Learning


**Source**: [Original Paper](http://arxiv.org/abs/2605.05172v1)
Saved: 2026-05-07 22:08
Source: 2026-05-06_17-40-11Z_WhenLifeGivesYouBC_MakeQ_functions_ExtractingQ_val.md

---

## Summary
The paper proposes Q2RL, an offline-to-online learning method that starts from a behavior cloning (BC) policy and then extracts a usable Q-function from it with a small amount of interaction. The method combines Q-Estimation, which recovers Q-values from BC, with Q-Gating, which chooses between BC and RL actions based on their estimated values. This aims to preserve good imitation behavior while enabling online improvement without the usual instability from distribution mismatch.

## Key Takeaways
- BC can serve as a stronger starting point if its implicit value structure is recovered.
- Q-Gating helps avoid overwriting useful BC behavior during online RL.
- The approach is practical for real robot learning with limited interaction.

## Context
The work targets manipulation settings where demonstrations are available but further online learning must be sample-efficient. It is evaluated on D4RL and robomimic tasks, including contact-rich and precision manipulation.

## Implications
The method suggests a path to safer, faster on-robot reinforcement learning by reducing the cost of adaptation after imitation learning. It also provides a bridge between supervised imitation and online value-based optimization.

## Original Reference
- Title: When Life Gives You BC, Make Q-functions: Extracting Q-values from Behavior Cloning for On-Robot Reinforcement Learning
- Authors: Lakshita Dodeja, Ondrej Biza, Shivam Vats, Stephen Hart, Stefanie Tellex, Robin Walters, Karl Schmeckpeper, Thomas Weng
- Published: 2026-05-06T17:40:11Z
- URL: http://arxiv.org/abs/2605.05172v1
- Source file: /home/rich/wiki/ai-research/raw/papers/2026-05-06_17-40-11Z_WhenLifeGivesYouBC_MakeQ_functions_ExtractingQ_val.md