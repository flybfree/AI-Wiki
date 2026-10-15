---
title: Policy-Verified Self-Training: Learning Agent Compliance from Verifiable Policy Rewards
published: 2026-10-14T01:16:15Z
authors: Min-Young Yu
url: http://arxiv.org/abs/2610.19372v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Policy-Verified Self-Training: Learning Agent Compliance from Verifiable Policy Rewards

## Abstract
Runtime policy verifiers can prevent agents from executing disallowed actions, but their decisions are typically used only for enforcement and discarded afterward. We ask whether these decisions can instead become verifiable policy rewards for training the agents they guard. We introduce Policy-Verified Self-Training (PVST), a post-training paradigm in which an agent generates its own interaction trajectories and an executable policy verifier, here a deterministic gate compiled from a written policy, evaluates whether each action complies. Compliant trajectories are reinforced, and violations become negatives for preference optimization; beyond the gate and the benchmark's task-success signal, PVST needs no stronger teacher model, no human preference labels and no attack-specific supervision, although rollouts are collected in the benchmark's attacked environment. On held-out AgentDojo tasks under prompt injection, policy-verified preference training of Qwen3-8B reduces violating trajectories from 37.2% to 10.3 $\pm$ 0.9% (three seeds) and successful attacks from 12.4% to 0.5% at equal or higher pooled task utility, although utility falls on travel, compared with 22.0% when negatives are selected by an attack oracle and 31.9 $\pm$ 0.9% with negatives that contain no violation. The learned behavior holds under an attack template never used in training (37.7% to 11.0%) and on a suite excluded from training (34.8% to 16.7%), and the retained verifier's intervention rate falls from 39.2% to 8.8% (seed 0). Our analysis identifies two conditions under which the verdict is most informative: success must not already imply compliance, and guarded actions must appear in both permitted and forbidden contexts.

## Metadata
- **Published**: 2026-10-14T01:16:15Z
- **Authors**: Min-Young Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.19372v1)