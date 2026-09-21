---
title: GameLogicBench: Evaluating Coding Agents on Runtime Game Logic with Tick-Level State Assertions
url: http://arxiv.org/abs/2609.21562v1
type: paper-summary
date: 2026-09-20
source_paper: 2026-09-18_09-51-41Z_GameLogicBench_EvaluatingCodingAgentsonRuntimeGame.md
generated_at: 2026-09-20 20:10
model: freedomaisvr/gemma-4-12b-it
---

## Summary
The paper introduces GameLogicBench, a novel benchmark designed to evaluate the ability of coding agents to implement and maintain complex gameplay logic within Godot projects. Unlike previous benchmarks that rely on visual output or final state analysis, this framework utilizes automated evaluators to check game rules at every simulation tick across 1,451 test cases. The study demonstrates that while current models can handle isolated mechanics, their performance significantly degrades as tasks scale toward repository-level features, highlighting a need for more robust validation methods like "mutant" testing to filter out incorrect logic.

## Key Takeaways
- The benchmark consists of 72 gameplay-logic tasks across 403 hand-designed scenarios, providing a diverse range of challenges from isolated mechanics to multi-system interactions and repository-scale features.
- A core innovation is the use of tick-level state assertions, which ensure that the evaluator measures whether the agent's code adheres to game rules throughout the entire execution rather than just checking if the final result appears correct.
- The researchers found that without using "mutant" validation—which checks for specific missing capabilities or incorrect behaviors—many AI submissions would pass despite being logically flawed. 
- Analysis showed that agents tend to inspect code more frequently and make a higher number of tool calls as the complexity of the task increases, particularly when dealing with repository-scale features.

## Context
This research addresses a critical gap in the evaluation of autonomous coding agents, specifically within domains like game development where "correctness" is defined by consistent rule adherence over time rather than a single output. As AI models become more capable of writing code, the field needs objective, reproducible metrics that can distinguish between a model that produces "plausible-looking" code and one that produces functionally correct logic in complex environments.

## Implications
For researchers and developers, these findings suggest that simply providing an AI agent with internet access or a "runnable" environment is insufficient for ensuring high-quality software production; rigorous, automated verification of internal logic is required. The study highlights the importance of creating benchmarks that can detect subtle logical errors, suggesting that future AI development should focus on improving an agent's ability to reason through multi-step dependencies and complex system interactions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.21562v1)
