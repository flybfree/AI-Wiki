---
title: Harness Policy Distillation: Aligning Agent Policies with Runtime Semantics
url: http://arxiv.org/abs/2610.20261v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-14_14-28-02Z_HarnessPolicyDistillation_AligningAgentPolicieswit.md
generated_at: 2026-10-14 22:01
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Harness Policy Distillation (HPD), a training framework that explicitly targets the runtime control semantics embedded in agent deployment harnesses, rather than relying solely on trajectory-level action supervision. By replaying reference trajectories through the product-specific runtime harness to recover implicit control semantics and representing them as privileged control documents at each model-call boundary, HPD enables a shared model to internalize harness-compatible decision-making. On TRAJECT-Bench using the Pi harness, Qwen3-8B trained with HPD achieves 22.98% autonomous task success and 49.23% runtime compliance, a dramatic improvement over the unadapted model's 3.09% and 19.90%.

## Key Takeaways
- HPD addresses a critical gap in agent training: ordinary trajectory supervision captures which action was taken but leaves the runtime semantics—such as which actions are executable, how state advances, and when the loop terminates—completely implicit. HPD makes these control semantics an explicit training target alongside actions, ensuring the model learns not just what to do but how the harness constrains and governs execution.
- The method works by replaying reference trajectories through the harness to recover runtime semantics, encoding them as control documents at each model-call boundary. A teacher model uses these privileged control documents to generate actions, and harness verification ensures all generated targets are executable under the runtime contract. The student model is then jointly trained on both the control-state privileged information and native history, internalizing the semantics into its policy without any additional inference-time scaffolding.
- The empirical results demonstrate that harness-verified teacher actions substantially improve the native deployment policy, while joint control-state supervision provides further gains in both task completion and runtime compliance. At deployment, the trained model operates through the original harness interface with no control document or supplementary information required, making the approach practical for production agent systems.

## Context
This work sits at the intersection of agent training, policy distillation, and runtime-aware model alignment. As general-purpose language models are increasingly deployed as autonomous agents inside product-specific harnesses, a fundamental mismatch emerges between the model's learned behavior and the runtime contract governing execution. Prior approaches to agent fine-tuning treat trajectories as flat action sequences, ignoring the structured control logic that determines valid transitions. HPD reframes the problem by treating the harness itself as a source of dense, structured supervision, bridging the gap between model training and deployment-time execution semantics.

## Implications
For practitioners building agentic systems, HPD offers a practical recipe for adapting open-weight models to specific product harnesses without requiring architectural changes or inference-time overhead, potentially reducing the gap between benchmark performance and real-world task completion. For the broader field, the paper signals that runtime semantics—often treated as engineering plumbing—should be elevated to first-class training signals, which could reshape how agent training pipelines are designed across industries deploying autonomous agents in software development, robotics, and enterprise automation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.20261v1)
