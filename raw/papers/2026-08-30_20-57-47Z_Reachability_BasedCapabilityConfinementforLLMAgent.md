---
title: Reachability-Based Capability Confinement for LLM Agents under Indirect Prompt Injection
published: 2026-08-30T20:57:47Z
authors: Wujie Xiong, Rabimba Karanjai, Yang Lu, Weidong Shi, Lei Xu
url: http://arxiv.org/abs/2608.30041v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reachability-Based Capability Confinement for LLM Agents under Indirect Prompt Injection

## Abstract
Large language model agents place outputs from external skills into their execution context, allowing attacker-controlled data to influence later privileged actions. Existing defenses mainly classify untrusted content or authorize proposed operations. They do not directly address how an agent's future authority should change once untrusted data enters its state. We present SkillGuard, a harness-level enforcement layer that treats this event as contamination and restricts future capabilities to disconnect the resulting state from deployer-defined forbidden states. Given sound skill summaries and policies, SkillGuard represents security-relevant transitions with a Skill Impact Graph, specifies admissible control over skill parameters via steerability signatures, and mediates invocations with an inline reference monitor. Following contamination, it computes weighted capability restrictions using binary, fractional, or fractional-flow strategies without auxiliary language-model inference. We evaluate SkillGuard on four AgentDojo suites with two backend LLMs, Gemini 2.5 Flash and Llama3.3-70B, against an LLM-only No Defense baseline and three defenses at different system layers: Spotlighting, CaMeL, and AttriGuard. We construct a compositional attack benchmark in which each attack combines observations individually insufficient to induce target violation and evaluate the same baselines on it. Under AgentDojo's Tool Knowledge attacks, SkillGuard eliminates attack success on three of four suites for both backends and reduces it to 4.8% and 14.3% on Slack. Against compositional attacks, it outperforms every baseline on Llama and matches the strongest baseline on Gemini at higher benign utility. Fractional-flow restriction preserves substantially more capabilities than binary restriction at the same attack success rate. Across both settings, SkillGuard adds no model calls or token overhead.

## Metadata
- **Published**: 2026-08-30T20:57:47Z
- **Authors**: Wujie Xiong, Rabimba Karanjai, Yang Lu, Weidong Shi, Lei Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30041v1)