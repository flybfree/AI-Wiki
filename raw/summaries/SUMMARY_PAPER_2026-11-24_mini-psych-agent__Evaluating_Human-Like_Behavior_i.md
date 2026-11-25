---
title: mini-psych-agent: Evaluating Human-Like Behavior in LLM Agents through Interactive Psychological Environments
url: http://arxiv.org/abs/2611.30365v1
type: paper-summary
date: 2026-11-24
source_paper: 2026-11-23_09-34-35Z_mini_psych_agent_EvaluatingHuman_LikeBehaviorinLLM.md
generated_at: 2026-11-24 21:42
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
The paper introduces mini-psych-agent, a framework that transforms psychological tasks into interactive, dynamic environments for evaluating LLM agents. It argues that an LLM's behavior is jointly determined by the backbone model, its harness, and the test-time compute budget, so the same underlying model can behave markedly differently across agentic workflows—analogous to how one person varies under different incentives and levels of deliberation. By letting agents act and observe changing states, and by scoring behavioral trajectories against a learned human-policy model, the authors show that human-likeness varies with agentic configuration and task, and that memory raises compatibility mainly by making choices more predictable rather than more human-like.

## Key Takeaways
- Behavior is configuration-dependent: the same underlying LLM can produce markedly different performance depending on the agentic workflow (harness) and the amount of test-time compute allocated, mirroring how a person behaves differently under different incentives and deliberation levels.
- Static text-transcribed psychological tasks are a poor fit for agent evaluation: they replay fixed, language-rendered experiments as static prompts, whereas agents act in ways that alter future observations and task states; conversely, dynamic environments used to evaluate LLM agents rarely ask whether the resulting behavior is human-like.
- Human-likeness is measurable but configuration-sensitive: using a learned human-policy model to evaluate how compatible behavioral trajectories are with human behavior, the authors find that compatibility varies across environments with the LLM's agentic configuration and the psychological task, and that memory raises it mainly by making choices more predictable rather than more human-like.

## Context
LLM agent evaluation has largely split into two camps: psychology-inspired tasks that are typically transcribed into static prompts, and dynamic environments that measure task success but rarely ask whether the resulting behavior resembles human behavior. This paper matters because it connects these two traditions, treating the agentic scaffold and compute budget as first-class determinants of behavior rather than fixed plumbing. It reframes evaluation around behavioral trajectories and their compatibility with human policy rather than only final outcomes.

## Implications
For practitioners and researchers, the result argues against reporting a single model score without specifying the harness, memory, and test-time compute used, since these can change both performance and human-likeness. It suggests psychology-inspired interactive environments as a more holistic evaluation standard that accounts for the backbone model and its agentic scaffold together. It also cautions that adding memory should not be assumed to make agents more human-like; gains may reflect predictability rather than genuinely human-compatible reasoning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.30365v1)
