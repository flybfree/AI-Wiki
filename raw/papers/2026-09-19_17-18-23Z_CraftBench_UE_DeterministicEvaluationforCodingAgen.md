---
title: CraftBench-UE: Deterministic Evaluation for Coding Agents in Unreal Engine
published: 2026-09-19T17:18:23Z
authors: Shutong Wu, Kevin Calderone, Andy Tsen
url: http://arxiv.org/abs/2609.23142v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CraftBench-UE: Deterministic Evaluation for Coding Agents in Unreal Engine

## Abstract
Building gameplay features in a game engine requires more than code, as code that compiles and runs does not necessarily implement the requested gameplay. We introduce CraftBenchUE, an evaluation harness that runs agents in an isolated Unreal Engine environment, reconstructs their saved submissions in fresh projects, and applies deterministic build, asset, and runtime checks without an LLM judge. Based on the harness, we built a benchmark consisting of 70 tasks spanning C++ source, Blueprint assets, and editor scripting. We evaluate seven models under two editor-tool configurations, with a file-and-shell baseline on C++ tasks. We further pair tasks that specify the same gameplay and use the same runtime tests, but require C++ and Blueprint as the deliverables. Across the 10 paired tasks, C++ completion rates exceed Blueprint by 30.0 and 42.9 percentage points in the two tool configurations. Among on-time Blueprint submissions in this paired set that pass asset checks, 42.2% and 50.0% fail explicit runtime assertions. These submissions satisfy asset requirements but fail the required gameplay tests. We will release the harness, task benchmark, and our trajectory findings with the report.

## Metadata
- **Published**: 2026-09-19T17:18:23Z
- **Authors**: Shutong Wu, Kevin Calderone, Andy Tsen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.23142v1)