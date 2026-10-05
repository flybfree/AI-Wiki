---
title: WebUIProof: Benchmarking WebUI Code Generators with UI-Agent Execution Harness
published: 2026-10-02T00:17:11Z
authors: Yun-Yun Tsai, Yuning Mao, Shiqi Wang, Junfeng Yang, Sinong Wang
url: http://arxiv.org/abs/2610.02617v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# WebUIProof: Benchmarking WebUI Code Generators with UI-Agent Execution Harness

## Abstract
Evaluating WebUI code generation at scale is difficult: outputs may compile and look plausible yet fail under user interaction, and prior benchmarks largely rely on free-form prompts with static checks (build success, screenshots) that miss functional correctness. We introduce WebUIProof, an execution-oriented benchmark that provides structured specifications and dense, executable interaction tests for WebUI generation across two task families: general WebUIs (e.g., dashboards, game, interactive tools) and 3D interactive simulation (e.g., particle/galaxy systems, physics dynamics). WebUIProof includes a UI-agent harness that runs executable interaction tests in a headless browser using an iterative plan--act--observe loop: it locates DOM elements, performs actions, observes resulting UI/DOM changes, and checks the specified assertions. We evaluate across eight commercial LLMs and observe frequent failures on interaction-based requirements even when pages render successfully, especially on 3D simulation interfaces. Finally, we show the UI-agent harness can provide outcome-level training signals. Training compact models (e.g., Qwen2.5 14B and MIMO 7B) with RL rewards derived from executable interaction tests improves functional completion while reducing build failures.

## Metadata
- **Published**: 2026-10-02T00:17:11Z
- **Authors**: Yun-Yun Tsai, Yuning Mao, Shiqi Wang, Junfeng Yang, Sinong Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.02617v1)