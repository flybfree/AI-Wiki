---
title: Training Small LLMs as Spatial Multi-Agent Policies
published: 2026-08-02T18:14:40Z
authors: Yi Mao, Andrew Perrault
url: http://arxiv.org/abs/2608.01425v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Training Small LLMs as Spatial Multi-Agent Policies

## Abstract
Training LLM-based multi-agent systems with multi-agent reinforcement learning is rapidly gaining traction, and a parallel line of work argues that such systems should be judged by their behavior, not only their reward. We take up both threads in spatial cooperative games, where small frozen LLMs prompted with low-level actions fail outright, earning zero reward. Guided by the options/semi-MDP framework---and, because option execution is asynchronous across agents, its multi-agent extension in macro-action Dec-POMDPs---we equip each game with a library of symbolic \emph{options}: typed, state-feasible, short-horizon behaviors executed by a symbolic planner. Each library is drafted by a frontier coding model from the game's source code; the feasibility guards that filter each menu are then synthesized mechanically from cheap random-policy burn-in rollouts---a guard is adopted only if it explains repeated execution failures while hiding no logged success---so no guard is authored, selected, or reward-tuned by hand. Each agent's LLM acts as its policy over options, with a private per-agent LoRA adapter trained by a per-agent variant of multi-agent GRPO (PA-MAGRPO); this lifts frozen bases from zero reward to competent play across three games and four small backbones. Behavioral audits then reveal that reward and cooperation decouple: a rising reward curve may simply mean that one agent has learned to run the entire task alone while its partner idles---cooperation emerges only when the task makes it necessary. Reward alone is thus an unreliable readout of cooperation; behavioral evaluation must sit alongside it.

## Metadata
- **Published**: 2026-08-02T18:14:40Z
- **Authors**: Yi Mao, Andrew Perrault
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01425v1)