---
title: FIRE: Failure-Informed Runtime Engineering for Reliable Language-Model Agents
published: 2026-09-22T11:50:35Z
authors: Nikita Agarwal, Nivedit Jain
url: http://arxiv.org/abs/2609.26048v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FIRE: Failure-Informed Runtime Engineering for Reliable Language-Model Agents

## Abstract
Language-model agents often reach a working solution and then fail to consistently deliver it. We study runtime policies: targeted natural-language instructions and action denials applied by the agent harness at states that preceded observed failures, without changing model weights or the user prompt. With this, keeping capability constant, we observe a meaningful unlock in delivered reliability. Across the complete 87-task Terminal-Bench 2.1 suite, with two attempts per task, policies increase repeated success (pass^2) in all three GPT-5.6 tiers: 50.6% to 54.0% for Luna, 55.2% to 60.9% for Terra, and 64.4% to 73.6% for Sol. Sol's best-of-two success changes by 1.2 points while repeated success rises by 9.2, showing that policies chiefly convert reachable solutions into dependable delivery. We further cover 14 tasks under Terra's frozen portfolio. Policy-guided Terra reaches 71.4%, compared with 64.3% for unassisted Sol, at about half the cost, demonstrating how engineering around models could unlock dependability for a use case. To isolate the mechanism we run a randomized five-arm experiment: real policies reach 61% on eligible tasks, versus 39% without a policy, 36% with a timing-matched sham, and 39 to 43% with generic verification or reconsideration. The intended corrective behavior appears in 22 of 24 coded policy attempts, against at most 14 in any other arm. Runtime policies are therefore a practical reliability layer: they make capabilities an agent already possesses substantially more repeatable.

## Metadata
- **Published**: 2026-09-22T11:50:35Z
- **Authors**: Nikita Agarwal, Nivedit Jain
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.26048v1)