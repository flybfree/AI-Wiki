---
title: Recursive Harness Distillation across Agents for Robot Manipulation
url: http://arxiv.org/abs/2609.33378v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-27_09-01-15Z_RecursiveHarnessDistillationacrossAgentsforRobotMa.md
generated_at: 2026-09-28 23:13
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces Recursive Harness Distillation, a framework that enhances robot manipulation by accumulating intervention experience into reusable playbooks without updating model parameters. A strong agent distills its interaction knowledge to guide a lighter agent, which then refines the playbook through execution feedback, enabling both agents to diagnose failures and adapt behavior in new task instances. The method yields substantial performance gains on real-world hardware and simulation benchmarks compared to standard baselines.

## Key Takeaways
- Recursive Harness Distillation allows a strong agent to generate a "playbook" of intervention guidance for a light agent, which is iteratively refined using the light agent's execution feedback; this process accumulates reusable knowledge that improves failure recovery without requiring model fine-tuning or parameter updates.
- The approach significantly boosts manipulation success rates, increasing real-world performance from 37.3% to 64.0%, and on SimplerEnv Bridge, the light agent with the playbook achieves 66.7% success, outperforming both the GR00T-only baseline (41.7%) and the strong agent without a playbook.
- The distilled playbook demonstrates cross-agent utility by also improving the strong agent's performance to 79.2%, confirming that accumulated intervention knowledge can be effectively shared across different model capabilities to enhance overall manipulation robustness.

## Context
Vision-language-action models are pivotal for general-purpose robotics but often struggle with runtime adaptability, particularly when execution requires diagnosing failures and modifying behavior in dynamic environments. This research addresses a fundamental challenge in embodied AI by proposing a mechanism to externalize and refine policy knowledge through interaction, offering a solution that complements static model capabilities with dynamic, experience-based guidance.

## Implications
Practitioners can utilize this method to deploy computationally efficient agents that inherit robust intervention strategies from larger models, reducing the need for expensive online adaptation or frequent retraining cycles. For the robotics industry, recursive harness distillation enables a scalable continuous improvement loop where operational data is systematically distilled into reusable assets, allowing fleets of robots to benefit from accumulated expertise

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.33378v1)
