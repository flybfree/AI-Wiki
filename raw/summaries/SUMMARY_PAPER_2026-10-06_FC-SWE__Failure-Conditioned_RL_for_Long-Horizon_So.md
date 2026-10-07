---
title: FC-SWE: Failure-Conditioned RL for Long-Horizon Software Engineering Agents
url: http://arxiv.org/abs/2610.07898v1
type: paper-summary
date: 2026-10-06
source_paper: 2026-10-06_07-44-12Z_FC_SWE_Failure_ConditionedRLforLong_HorizonSoftwar.md
generated_at: 2026-10-06 21:15
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
FC-SWE introduces a failure-conditioned reinforcement learning framework for repository-level software engineering agents, aiming to make multi-turn tool-use training more sample-efficient by reusing verifier feedback from failed patches. Instead of treating each sampled trajectory independently, FC-SWE restores the repository after a failed patch and conditions a recovery attempt on the failed patch and verifier diagnostics, improving SWE-bench Verified performance over standard GRPO.

## Key Takeaways
- Standard GRPO for SWE agents samples multiple trajectories per issue, tests patches, and compares terminal rewards within fixed groups, but it discards useful verifier feedback from failed patches, limiting the agent’s ability to learn from diagnostic failure information.
- FC-SWE creates recovery trajectories by restoring the repository to its original task state after a failed verification, then using the failed patch and verifier feedback as context for a subsequent attempt, while adapting GRPO with trajectory-local rewards so success in a recovery attempt does not incorrectly reward the earlier failed patch.
- Active-set advantage estimation builds comparison groups from all initial and recovery trajectories actually executed for the same issue, keeping failed attempts in the advantage calculation while excluding unexecuted attempts; this yields 41.7% Resolved@1 and 52.8% Resolved@2 with Qwen3.5-4B and SWE-agent, versus 38.9% and 48.5% for GRPO, and reaches 70.7% Resolved@11 under an eleven-attempt budget despite training with at most two attempts per chain.

## Context
Repository-level software engineering is a long-horizon agentic task because agents must navigate codebases, invoke tools, maintain state, and revise solutions after failures. Recent RL methods such as GRPO improve agent behavior by comparing multiple sampled trajectories, but they often treat failures as terminal events rather than informative states. FC-SWE addresses this gap by making failure feedback part of the training distribution, which is important for agents that must recover from incorrect edits, test failures, or incomplete reasoning.

## Implications
For practitioners, FC-SWE suggests that verifier feedback should be treated as reusable training context rather than discarded after a failed patch, which can improve sample efficiency and reliability in software agent pipelines. For industry workflows, failure-conditioned training may help coding agents become more robust in CI-like settings where tests, linters, and execution logs provide rich diagnostics. For the field, it points toward RL designs that model recovery as a first-class behavior, potentially benefiting other long-horizon tool-use domains where failures are common and informative.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.07898v1)
