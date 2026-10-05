---
title: MobiAgent: Dual-Loop Recursive Policy Self-Improvement for Long-Horizon Mobile Manipulation
url: http://arxiv.org/abs/2610.03476v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-02_15-48-23Z_MobiAgent_Dual_LoopRecursivePolicySelf_Improvement.md
generated_at: 2026-10-04 21:29
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
MobiAgent introduces a dual-loop agentic framework designed to tackle long-horizon mobile manipulation by decoupling high-level reasoning from low-level control through composable atomic skills and enabling continuous self-improvement without human annotation. The system demonstrates substantial performance gains, outperforming π₀.₅-TA by 22.5 percentage points on BEHAVIOR-1K and improving success rates from 7.50% to 27.50% on RoboCasa through autonomous data recycling.

## Key Takeaways
- The Inner Loop architecture separates high-level planning from low-level execution by using Vision-Language models for receding-horizon planning and visual reflection, dynamically composing atomic skills to recover from execution errors. These skills are executed by specialized flow-matching experts that share a unified VLM backbone, which maximizes skill reusability while mitigating capacity interference between locomotion and arm control.
- The Outer Loop enables automated lifelong learning by autonomously segmenting and verifying deployment rollouts, clustering them to discover new atomic skills, and continuously fine-tuning the skill library without any human annotations. This recursive self-improvement mechanism drives measurable performance gains over time, as evidenced by success rates improving from 32.5% to 57.5% on the Astribot S1 platform.
- The framework directly addresses three critical limitations of existing hierarchical agents: rigid sub-task mapping, inflexible replanning, and the absence of continuous learning. By combining composable skill libraries with dynamic replanning and autonomous data recycling, MobiAgent bridges the gap between robust deployment execution and recursive policy self-improvement.

## Context
Long-horizon mobile manipulation remains a frontier challenge in embodied AI because execution errors compound across multi-stage tasks and locomotion-arm control creates capacity interference that single-model approaches struggle to resolve. While Vision-Language-Action models have advanced short-horizon manipulation, the field lacks hierarchical reasoning architectures capable of multi-stage objectives with robust error recovery. MobiAgent represents a significant step toward closing this gap by integrating agentic planning with continuous self-improvement in a unified system.

## Implications
For robotics practitioners and embodied AI researchers, MobiAgent offers a practical blueprint for deploying manipulation systems that improve autonomously over time without requiring curated training data, reducing the annotation bottleneck that currently limits scalable robot learning. For industry applications in warehouse automation, household assistance, and manufacturing, the demonstrated ability to recover from execution failures and self-improve through deployment data recycling suggests a path toward more resilient and economically viable long-horizon robotic systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.03476v1)
