---
title: FlowBalance: Verifier-Grounded Self-Improvement from On-Policy Reasoning Experience
published: 2026-09-03T00:47:11Z
authors: Zixun Huang, Kishan Panaganti, Haitao Mi, Leowei Liang
url: http://arxiv.org/abs/2609.03241v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FlowBalance: Verifier-Grounded Self-Improvement from On-Policy Reasoning Experience

## Abstract
A reasoning model can improve from its own on-policy experience, but this inner loop is fragile: terminal verifiers provide reliable yet sparse supervision, while dense same-model guidance can reinforce false confidence or overconcentrate learning on a narrow solution mode. We introduce FlowBalance, a verifier-grounded self-improvement method that learns a normalized distribution over complete responses. For each on-policy trajectory, a frozen training-time view of the same policy uses privileged context to produce token-level log-probability gains, which are aggregated into a trajectory-level self-guidance score. FlowBalance calibrates this score with the verifier-derived group advantage: guidance is retained on positive-advantage trajectories, reversed on negative-advantage trajectories, and disabled when the rollout group provides no outcome preference. The resulting energy exponentially reweights a reference policy, and profiled trajectory balance fits the normalized target with one log-partition estimate per rollout group. This realizes outcome-calibrated self-guidance via trajectory balance, without a separate token-level imitation loss. Our analysis establishes within-group contrast preservation, a minimum-change reverse-KL characterization, monotonic verifier control of target reward, and an exact correction against false-positive self-guidance on rejected responses. On mathematical reasoning, FlowBalance improves average performance over FlowRL on both Qwen3-4B and Qwen3-8B, while also improving training speed and stability, avoiding direct OPSD's response-length collapse, and exhibiting higher correct-strategy diversity in a controlled AIME24 diagnostic.

## Metadata
- **Published**: 2026-09-03T00:47:11Z
- **Authors**: Zixun Huang, Kishan Panaganti, Haitao Mi, Leowei Liang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03241v1)