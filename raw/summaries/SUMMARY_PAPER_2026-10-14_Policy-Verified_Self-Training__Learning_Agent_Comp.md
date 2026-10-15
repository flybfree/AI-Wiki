---
title: Policy-Verified Self-Training: Learning Agent Compliance from Verifiable Policy Rewards
url: http://arxiv.org/abs/2610.19372v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-14_01-16-15Z_Policy_VerifiedSelf_Training_LearningAgentComplian.md
generated_at: 2026-10-14 20:59
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Policy-Verified Self-Training (PVST), a post-training paradigm that repurposes runtime policy verifier decisions—typically used only for enforcement—as verifiable rewards for training the very agents they guard. By having an agent generate its own interaction trajectories and evaluating compliance through a deterministic gate compiled from a written policy, PVST reinforces compliant trajectories and treats violations as negatives for preference optimization. Applied to Qwen3-8B on AgentDojo tasks under prompt injection, the method reduces violating trajectories from 37.2% to 10.3% and successful attacks from 12.4% to 0.5% while maintaining task utility, demonstrating that policy compliance can be learned without external supervision.

## Key Takeaways
- PVST eliminates the need for a stronger teacher model, human preference labels, or attack-specific supervision by using a deterministic policy gate compiled from written policy text as the sole reward signal beyond the benchmark's task-success metric. This makes the training pipeline self-contained and scalable to new policy domains without costly annotation pipelines.
- The method demonstrates strong generalization: learned compliance behavior transfers to attack templates never seen during training (reducing violations from 37.7% to 11.0%) and to benchmark suites excluded from training (34.8% to 16.7%), indicating the agent learns policy structure rather than memorizing specific attack patterns.
- The paper identifies two critical conditions for informative verifier verdicts: task success must not already imply compliance (otherwise the reward signal is redundant), and guarded actions must appear in both permitted and forbidden contexts (otherwise the agent cannot learn the boundary). Additionally, the retained verifier's intervention rate drops from 39.2% to 8.8%, showing the agent internalizes policy constraints and requires less external enforcement over time.

## Context
As LLM-based agents are increasingly deployed in regulated environments—finance, healthcare, legal compliance—runtime policy verifiers have become standard enforcement mechanisms, yet their rich compliance signals are discarded after each decision. This paper addresses a fundamental gap in the agent training pipeline: the disconnect between enforcement infrastructure and learning infrastructure. It sits at the intersection of RLHF/preference optimization research, agentic safety, and formal policy verification, proposing a bridge that converts operational guardrails into training data without additional human oversight.

## Implications
For practitioners deploying policy-governed agents, PVST offers a practical path to reducing verifier intervention rates over time, lowering operational costs and latency while improving agent autonomy within compliance boundaries. For the broader field, it suggests that existing enforcement infrastructure can be repurposed as a scalable, label-free training signal, potentially accelerating the adoption of self-improving agents in regulated industries without requiring expensive human-in-the-loop annotation or access to frontier teacher models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.19372v1)
