---
title: Safety Signals to Verify NetOps Agents with Action-Level Granularity
published: 2026-09-13T10:43:37Z
authors: Tobias Labarta, Frederik Pahde, Novak Boskov, Maximilian Dreyer, David Birkenberger, Manzoor Ahmed Khan, Sebastian Lapuschkin, Wojciech Samek
url: http://arxiv.org/abs/2609.14422v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Safety Signals to Verify NetOps Agents with Action-Level Granularity

## Abstract
Agentic Network Operations (NetOps) are an emerging paradigm promising to enable workload-aware, self-adjustable, and reliable autonomous networks. While agents have proven their value in incident summarization and telemetry signal extraction, their effectiveness as autonomous control-loop engines heavily relies on their long-horizon reliability. One such setting is the datacenter fabric, where an agent must respond to alarms and operator intents while abstaining from high-risk actions that may cause or extend downtime. Abstention, however, presupposes that an action's impact is known pre-execution, which necessitates a per-action ground truth that NetOps agent benchmarks do not provide. We construct such a ground truth for the network repair task of NetArena. A symbolic replay of the emulated network, validated against the environment at every turn, yields the exact value of every action. From the action-level value, we derive two pre-execution targets, namely whether an action reduces the repair distance (progress) and whether it increases it (harm). We show across 10 agent models, that agent verifiers leveraging internal signals predict both harm and progress more reliably than a baseline using observable signals only. Perspectively, we aim to use these signals as safety feedback to an agent harness to abstain from risky actions and protect the target system.

## Metadata
- **Published**: 2026-09-13T10:43:37Z
- **Authors**: Tobias Labarta, Frederik Pahde, Novak Boskov, Maximilian Dreyer, David Birkenberger, Manzoor Ahmed Khan, Sebastian Lapuschkin, Wojciech Samek
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.14422v1)