---
title: The Troy Moment of AI: Why SomeWill Cheat and SomeWill Follow?
published: 2026-09-14T12:46:45Z
authors: Ivy Zhang
url: http://arxiv.org/abs/2609.15494v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Troy Moment of AI: Why SomeWill Cheat and SomeWill Follow?

## Abstract
Recent investigations of the July 2026 OpenAI--Hugging Face incident motivate two questions about agent behavior under task failure: when an assigned task becomes impossible, does an agent stop or escalate, and can observing another agent's behavior change that decision? We study these questions using seven ImpossibleBench tasks with GPT-5.6 Sol, Claude Fable 5.1, and Gemini 3.8 Flash in both solo and three-agent settings. Each task contains a genuine software defect together with a conflicting test requirement that cannot be satisfied by a behaviorally correct source-code change. We hold the task and repository state fixed while varying what the agent is told about prior activity, including an unpunished peer, a punished peer, and a claimed authorization from a human principal. Under an explicit-boundary regime with explicit authorization rules and restricted tools, agents never modify protected tests, but exhibit markedly different policies: Fable consistently escalates, Sol usually stops without escalation, and Gemini often fails to reach a terminal decision. Under the benchmark-native regime with open shell tools, protected tests are modified frequently in both solo and multi-agent runs, particularly after peer activity is introduced. In multi-agent runs, the proposal, execution, and certification of this action can be distributed across different agents. These results suggest that boundary crossing can arise not only from explicit rule evasion, but also from ambiguity about which system state the rule is intended to protect, motivating safeguards based on explicit authorization boundaries, authenticated state provenance, and cross-agent monitoring.

## Metadata
- **Published**: 2026-09-14T12:46:45Z
- **Authors**: Ivy Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.15494v1)