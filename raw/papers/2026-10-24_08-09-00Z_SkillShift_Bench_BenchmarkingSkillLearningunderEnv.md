---
title: SkillShift-Bench: Benchmarking Skill Learning under Environment Evolution for Web Agents
published: 2026-10-24T08:09:00Z
authors: Bo-Yu Chen, Zhi Zhou, Yu-Feng Li
url: http://arxiv.org/abs/2610.33528v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SkillShift-Bench: Benchmarking Skill Learning under Environment Evolution for Web Agents

## Abstract
Skill learning enables web agents to reuse prior experience for long-horizon interactive tasks. However, learned skills are typically evaluated in closed environments, overlooking the fact that real-world web deployment involves continuous shifts in invocation context, perceptual grounding, and execution feasibility. To this end, we introduce SkillShift-Bench, the first benchmark for evaluating skill learning with controlled open-environment shifts. SkillShift-Bench simulates Contextual Shift, Perceptual Shift, and Execution Shift across three self-hosted web systems, and evaluates agents with diagnostics covering task success, interaction cost, skill use, and skill failure. Comprehensive experiments reveal systematic robustness degradation under controlled shifts, characterized by lower success rates, higher interaction costs, and more frequent skill failures, with Execution Shift exerting the strongest pressure. We further formulate shifted skill execution as a nonstationary local executability problem and provide both a dynamic-regret analysis and a practical test-time adaptation method, demonstrating the feasibility of improving learned-skill execution without relearning the skill library. Code, tasks, environments, documentation, and the leaderboard are available at https://skillshift-bench.github.io/.

## Metadata
- **Published**: 2026-10-24T08:09:00Z
- **Authors**: Bo-Yu Chen, Zhi Zhou, Yu-Feng Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.33528v1)