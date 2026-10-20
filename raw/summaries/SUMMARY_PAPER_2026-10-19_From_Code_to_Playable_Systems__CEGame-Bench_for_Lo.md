---
title: From Code to Playable Systems: CEGame-Bench for Long-Horizon Game Creation Agents
url: http://arxiv.org/abs/2610.26098v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-19_09-59-25Z_FromCodetoPlayableSystems_CEGame_BenchforLong_Hori.md
generated_at: 2026-10-19 23:56
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces CEGame-Bench, the first benchmark designed to evaluate game-creation agents across five production engines (Defold, Godot, Roblox Studio, Unity, and Unreal Engine) on the full pipeline from empty project to playable, completable game. The authors find that while agents achieve high integration scores, they consistently fail to produce games that players can actually finish, with only 16% of runs reaching an ending, revealing a critical artifact-to-play gap in current agent capabilities.

## Key Takeaways
- CEGame-Bench shifts evaluation from single-engine or one-prompt browser games to long-horizon, multi-engine game creation where agents must build complete games from scratch using a design document as a contract, with runs averaging up to 295 steps and 65 million tokens, and acceptance determined solely by real-input playtesting rather than successful compilation or build output.
- Under four different agent scaffolds, models earn most integration points but typically score under half the gameplay points, and only 16% of generated games reach their ending, whereas reference games built by human engineers assisted by coding agents score near the maximum, isolating the failure squarely within the agents themselves rather than the engines or tooling.
- Engine choice significantly affects outcomes: no two engines rank agent configurations identically (Kendall's tau ranging from 0.14 to 0.62), and the same game typically scores higher on Unity and Unreal Engine because those engines enforce stricter pre-play validation. The authors also release Game Completion Boost, an agent skill for requirement-driven playtesting and repair that improves execution-based scores across three models by 14.1 to 24.3 points.

## Context
Current AI agent benchmarks for code generation and software creation overwhelmingly measure whether code compiles or passes unit tests, but game development demands a fundamentally different success criterion: a player must be able to launch, complete, and return to a persistent world. By spanning five production engines with distinct architectures, scripting languages, and validation pipelines, CEGame-Bench exposes how brittle agent performance is across toolchains and how poorly current scaffolds generalize beyond single-engine toy tasks. This positions the benchmark as a stress test for long-horizon autonomous agents in a domain where the final artifact must be interactively playable, not merely syntactically correct.

## Implications
For practitioners building game-development copilots or autonomous creative agents, the findings indicate that compile-and-test validation is insufficient and that requirement-driven playtesting loops, as demonstrated by Game Completion Boost, are necessary to close the gap between generated code and a shippable game. For the broader AI research community, the engine-dependent ranking divergence (Kendall's tau 0.14–0.62) warns against benchmarking agents on a single engine and calls for multi-engine evaluation protocols before claiming general-purpose software creation capability. Industry teams evaluating AI-assisted game pipelines should treat execution-based acceptance as the primary gate rather than build success, and should invest in agent skills that iteratively repair gameplay defects rather than merely generating code.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.26098v1)
