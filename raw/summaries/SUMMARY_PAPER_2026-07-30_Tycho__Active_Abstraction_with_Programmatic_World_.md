---
title: Tycho: Active Abstraction with Programmatic World Models for ARC-AGI-3
url: http://arxiv.org/abs/2607.28287v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_14-34-41Z_Tycho_ActiveAbstractionwithProgrammaticWorldModels.md
generated_at: 2026-07-30 20:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Tycho a coding agent that builds and uses game-specific models to solve ARC-AGI-3 by separating observations from animation. It evaluates four orchestration policies on 25 public games with Claude Opus 4.8 showing the highest Relative Human Action Efficiency achieved is 88.49.

## Key Takeaways
- Tycho constructs a testable model from costly interaction and decides when to use it, achieving 88.49 RHAE.
- GPT-5.6 Sol and Opus 5 reach perfect 100 RHAE completing all levels with balanced human-replay ranks.
- Automatic repair after verification failures yields 83.07 RHAE showing tradeoff between model accuracy and efficiency.

## Context
Active abstraction is a core challenge for AGI where agents must infer rules while minimizing costly actions, a problem relevant to reinforcement learning and simulation-based reasoning.

## Implications
This approach could reduce sample inefficiency in AI agents by integrating model building with decision making, offering tools for industry applications that require rapid adaptation to new environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28287v1)
