---
title: Computation, Not Memory: Chain-of-Thought and State Tracking in LLM Agents
published: 2026-10-19T04:18:24Z
authors: Pedram Mouseli, Massieh Moayedi
url: http://arxiv.org/abs/2610.25760v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Computation, Not Memory: Chain-of-Thought and State Tracking in LLM Agents

## Abstract
Language-model agents often reason before they act, and the value of monitoring that reasoning depends on how it relates to their actions. We ask how an agent's actions depend on its reasoning when the correct action depends on a changing state. In a small file-system task, background events announce which file's lock has been toggled but not its new value. The agent therefore has to reconstruct the current locks from its history before it can move files safely. With Qwen3-8B and Qwen3.5-9B, we separate two roles of reasoning: generating it before each action, and retaining earlier reasoning in the prompt. Most of the reduction in lock-violating commands comes from reasoning written at the moment of action. Retaining earlier reasoning adds little to rule-following, although it helps one model complete the task. The benefit depends on what the reasoning says. Filler text, reasoning written for another history and an accurate table of the state do not reproduce it. When we give the agent reasoning written for a history that differs in one lock value, the agent acts on that reasoning even against its own history. Without reasoning, linear probes recover the state from the model's activations about as well as a text classifier recovers it from the transcript. However, decoding accuracy does not predict which interventions change the agent's actions. In this setting, the benefit of reasoning for rule-following comes mainly from generating it at each step. The state that can be decoded without reasoning is a limited guide to how the agent acts.

## Metadata
- **Published**: 2026-10-19T04:18:24Z
- **Authors**: Pedram Mouseli, Massieh Moayedi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.25760v1)