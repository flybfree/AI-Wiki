---
title: "Summary: 2026-05-25_17-59-36Z_FromModelScalingtoSystemScaling_ScalingtheHarnessi.md"
date: 2026-05-25
tags: ['paper', 'research', 'ai']
---
# Summary: 2026-05-25_17-59-36Z_FromModelScalingtoSystemScaling_ScalingtheHarnessi.md


**Source**: [Original Paper](http://arxiv.org/abs/2605.26112v1)
Saved: 2026-05-26 00:01
Source: 2026-05-25_17-59-36Z_FromModelScalingtoSystemScaling_ScalingtheHarnessi.md
Model: None

---


## Summary  
The paper argues that the next bottleneck in advancing agentic AI lies not in improving foundation models alone but in scaling the structured execution “harness” that integrates memory, retrieval, tool use, and governance into a persistent, auditable system. It proposes a research agenda to evaluate this harness through three core bottlenecks—context governance, trustworthy memory, and dynamic skill routing—and introduces a reference harness called CheetahClaws for systematic comparison with existing systems like Claude Code and OpenClaw. The authors claim that future progress will depend equally on stronger models and well‑designed system architectures.

## Key Contributions  
- [Finding 1] System scaling is the next major bottleneck, requiring design of auditable, modular, and verifiable architectures around foundation models.  
- [Finding 2] Agent performance emerges from the interaction among the foundation model, memory substrate, context constructor, skill‑routing layer, orchestration loop, and verification‑and‑governance layer; these form the “agent harness.”  
- [Finding 3] A research agenda for harness‑level benchmarks is outlined that measures trajectory quality, memory hygiene, context efficiency, communication fidelity, verification cost, and safe evolution over time.

## Methodology  
The authors develop CheetahClaws—a Python‑native reference harness—that implements the six layers described above. They compare it with two existing systems (Claude Code and OpenClaw) by running a suite of tasks that require long‑horizon execution, tool use, memory management, and verification. The experiments evaluate each bottleneck’s impact on overall agent behavior.

## Results  
The comparative study shows that CheetahClaws achieves higher trajectory quality and lower verification costs than Claude Code and OpenClaw, indicating that systematic harness design can outperform incremental model improvements alone. Memory hygiene metrics (e.g., contamination rates) are also significantly better in the reference harness, confirming its trustworthy memory implementation.

## Significance  
By shifting focus from one‑shot task success to holistic system evaluation, this work provides a framework for measuring real agentic behavior over time. It underscores that safe, reliable agents will require disciplined engineering of their execution layers as much as stronger models, guiding future research and deployment practices.

## Related Concepts

- [[concepts/ai-agents/agentic-workflows-hub.md|Agentic Workflows Hub]]
- [[concepts/llm-models/llm-models-hub.md|LLM Models Hub]]
- [[concepts/evaluation-benchmarks/evaluation-benchmarks-hub.md|Evaluation Benchmarks Hub]]
- [[concepts/audio-speech/audio-speech-hub.md|Audio Speech Hub]]
