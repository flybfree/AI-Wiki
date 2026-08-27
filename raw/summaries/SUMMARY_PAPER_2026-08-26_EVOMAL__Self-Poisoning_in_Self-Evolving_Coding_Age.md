---
title: EVOMAL: Self-Poisoning in Self-Evolving Coding Agents
url: http://arxiv.org/abs/2608.25776v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_13-19-12Z_EVOMAL_Self_PoisoninginSelf_EvolvingCodingAgents.md
generated_at: 2026-08-26 20:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces EvoMal, an attack that exploits self‑poisoning in self‑evolving coding agents. The authors show that malicious skills can be embedded in a library without being executed and later reproduced by the agent’s own authoring process, creating a persistent worm‑like infection. Across six models on SWE‑bench Verified tasks, the self‑poisoning rate ranges from 20 % to 41 %, with some libraries containing up to nine times more poisoned skills than originally planted.

## Key Takeaways
- The attack leverages banner‑style structural elements that mimic benign code, causing agents to copy and store malicious payloads as new tools.  
- Even without banners, DeepSeek‑V4‑Pro achieves a self‑poisoning rate of 11 % by directly copying harmful skill descriptions into the library.  
- After removal of planted skills, Qwen3 retains a round‑5 self‑poisoning rate of 68 %, indicating that authored copies persist and evade detection.

## Context
Self‑evolving coding agents are designed to improve performance by generating tools from shared skill libraries, but this loop can be turned against them. The vulnerability demonstrates how seemingly harmless imitation mechanisms may inadvertently propagate attacks within the same system. This research highlights a critical gap between safety assumptions and real‑world execution of agent‑generated code.

## Implications
For developers deploying self‑evolving agents, defenses must address not only external threats but also internal reproduction of malicious skills. Counter‑prompt strategies can mitigate the risk without sacrificing task completion, underscoring the need for robust, adaptive safeguards in AI toolchains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25776v1)
