---
title: Disclosure-Gated User Simulation for Companion-Agent Evaluation
url: http://arxiv.org/abs/2609.00982v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_09-39-41Z_Disclosure_GatedUserSimulationforCompanion_AgentEv.md
generated_at: 2026-09-01 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a disclosure‑gated user simulation framework designed to evaluate companion agents more honestly by preventing the simulated user from being overly cooperative. The authors train a simulator that learns which information gates each dialogue item belongs to, then shows that only their released simulator maintains ranking order and score stability across 12 systems while matching the original benchmark’s performance.

## Key Takeaways
- The disclosure gate structure creates three observable depth layers that condition how much user information is revealed based on the agent’s behavior.  
- Training the simulator on synthetic data allows it to infer gate placement without needing explicit labels at inference time, and this design prevents rank inflation caused by excessive questioning.  
- Only one of the examined simulators satisfies both order‑preserving ranking and scale‑stable scores; its correlation with the original benchmark is 0.993, whereas prompting a frontier model merely raises scores without improving rankings.

## Context
Current scalable evaluation often relies on large language models to simulate users, but this can mask true system performance by rewarding systems that ask more questions rather than those that elicit genuine user engagement. The disclosure‑gated approach addresses this bias by embedding behavioral constraints directly into the simulation environment.

## Implications
For practitioners developing companion agents, adopting a disclosure‑gated simulator ensures fair benchmarking and reliable ranking comparisons. It also provides a transparent mechanism to detect when evaluation methods are artificially inflating scores, guiding more robust design decisions in AI research and industry practice.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00982v1)
