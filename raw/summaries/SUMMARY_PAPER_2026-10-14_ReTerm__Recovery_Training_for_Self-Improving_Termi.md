---
title: ReTerm: Recovery Training for Self-Improving Terminal Agents
url: http://arxiv.org/abs/2610.18484v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_14-44-24Z_ReTerm_RecoveryTrainingforSelf_ImprovingTerminalAg.md
generated_at: 2026-10-14 00:28
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
ReTerm introduces a self-improving terminal agent framework that addresses a critical failure mode in coding agents: the inability to recover from errors during long-running task execution. By training on the agent's own failed trajectories and generating multiple independent recovery attempts through a novel reinforcement learning algorithm called ReTerm-GRPO, the system enables agents to learn recovery strategies from their own mistakes. The resulting ReTerm-9B model, built on Qwen3.5-9B, achieves 34.8% Pass@1 on Terminal-Bench 2.0, a 14.6-point improvement over the base model.

## Key Takeaways
- ReTerm constructs a custom data pipeline producing ReTerm-10K, a high-quality dataset of recovery demonstrations specifically designed for supervised fine-tuning cold start. This dataset captures effective strategies for recovering from command errors, faulty implementations, and other execution failures that commonly derail terminal agents during complex coding tasks.
- The proposed ReTerm-GRPO algorithm is an online reinforcement learning method that forks from the agent's own failure states to generate multiple independent self-recovery attempts. Rather than relying on external reward signals or curated examples, the agent learns from whether its own generated recovery attempts successfully complete the task, creating a self-improving loop grounded in its own experience.
- Comparative analysis demonstrates that ReTerm-GRPO achieves consistently higher recovery rates across diverse error categories compared to standard GRPO training, indicating that the failure-state-forking mechanism provides a more targeted and effective learning signal than generic reinforcement learning approaches applied to terminal agent tasks.

## Context
Terminal agents have become a prominent paradigm in AI-assisted software engineering, enabling autonomous execution of complex coding workflows through command-line interaction. However, a persistent bottleneck in this field is error recovery: agents that encounter runtime errors, incorrect implementations, or cascading failures during multi-step tasks often lack the strategic flexibility to diagnose and correct their mistakes, leading to task abandonment. This paper addresses that gap by proposing a training methodology that explicitly targets recovery behavior rather than initial task execution, contributing to the broader research direction of making autonomous agents more robust and self-correcting over extended interactions.

## Implications
For practitioners building autonomous coding agents, ReTerm demonstrates that targeted recovery training can yield substantial performance gains without requiring larger model architectures or additional human-annotated data, making the approach accessible for teams with limited resources. The open-source release of code, data, and model lowers the barrier for the community to adopt and extend recovery-focused training pipelines. More broadly, the self-improving paradigm—where agents learn from their own failures through structured RL—suggests a scalable path toward more reliable autonomous agents across domains beyond terminal coding, including software debugging, infrastructure management, and multi-step planning tasks where error recovery is as important as initial execution.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.18484v1)
