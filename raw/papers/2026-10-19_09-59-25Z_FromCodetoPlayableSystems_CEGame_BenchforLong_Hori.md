---
title: From Code to Playable Systems: CEGame-Bench for Long-Horizon Game Creation Agents
published: 2026-10-19T09:59:25Z
authors: Zixuan Dong, Yanghai Wang, Hanyan Bian, Jiaxi Tao, Junze Li, Jiadong Wang, Xinyu Che, Lin Liu, Baoyun Peng, Xiaodong Wang, Jiaheng Liu
url: http://arxiv.org/abs/2610.26098v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Code to Playable Systems: CEGame-Bench for Long-Horizon Game Creation Agents

## Abstract
A game ships when a player can launch it, finish it, and return to a saved world, none of which a successful build guarantees, yet game-creation agents are mostly tested on one engine or on one-prompt browser games. We present CEGame-Bench, the first long-horizon benchmark for complete-game creation across five production engines: Defold, Godot, Roblox Studio, Unity, and Unreal Engine. Agents build each game from an empty project and a design document in runs averaging up to 295 steps and 65M tokens; the document doubles as a contract, and a hidden evaluator accepts a game only by real-input play. Under four scaffolds, agents earn most integration points but usually under half the gameplay points, and their games reach the ending in only 16% of runs, while references built by engineers with coding agents score near the maximum, which places this artifact-to-play gap in the agents. No two engines rank configurations alike (Kendall's tau 0.14-0.62), and the same game usually scores higher on Unity and Unreal Engine, which check more before play. We release Game Completion Boost, an agent skill for requirement-driven playtesting and repair that raises the execution-based score of three models by 14.1-24.3 points.

## Metadata
- **Published**: 2026-10-19T09:59:25Z
- **Authors**: Zixuan Dong, Yanghai Wang, Hanyan Bian, Jiaxi Tao, Junze Li, Jiadong Wang, Xinyu Che, Lin Liu, Baoyun Peng, Xiaodong Wang, Jiaheng Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.26098v1)