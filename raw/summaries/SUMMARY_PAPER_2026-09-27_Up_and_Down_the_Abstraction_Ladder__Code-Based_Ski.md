---
title: Up and Down the Abstraction Ladder: Code-Based Skills for Language Agents
url: http://arxiv.org/abs/2609.31076v1
type: paper-summary
date: 2026-09-27
source_paper: 2026-09-25_10-15-45Z_UpandDowntheAbstractionLadder_Code_BasedSkillsforL.md
generated_at: 2026-09-27 21:20
model: qwen3.6-35b-a3b
---

## Summary
This paper investigates the impact of code-based action abstractions, termed "skills," on the performance, efficiency, and learning capabilities of language agents operating in complex, long-horizon environments like NetHack. The authors demonstrate that utilizing a library of reusable skills significantly enhances agent productivity by tripling game progression and reducing inference costs by 86% compared to primitive actions alone. Furthermore, combining skills with access to primitives preserves these efficiency gains while maintaining necessary flexibility for handling out-of-distribution scenarios, and skill-based agents exhibit substantially accelerated learning rates during reinforcement training.

## Key Takeaways
- Code-based skills drastically improve agent performance and efficiency; in zero-shot evaluations, agents using skills nearly triple their game progression compared to those restricted to primitive actions while simultaneously reducing inference costs per episode by 86%.
- A hybrid approach that combines semantic skills with access to low-level primitives offers the optimal balance, retaining the

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.31076v1)
