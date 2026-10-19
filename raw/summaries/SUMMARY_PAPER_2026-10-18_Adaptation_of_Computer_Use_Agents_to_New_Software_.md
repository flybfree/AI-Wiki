---
title: Adaptation of Computer Use Agents to New Software with User Manuals
url: http://arxiv.org/abs/2610.23012v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-16_06-44-56Z_AdaptationofComputerUseAgentstoNewSoftwarewithUser.md
generated_at: 2026-10-18 20:42
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces MAGE (Manual-augmented computer use AGent Execution and learning), a framework that leverages software user manuals as a scalable source of procedural knowledge to improve both the inference-time execution and training of computer use agents (CUAs) operating on graphical user interfaces. The authors demonstrate that by retrieving task-relevant manual content for planning during execution and converting manuals into executable task-plan pairs for training, MAGE achieves improved task success rates across six applications compared to strong baselines, significantly reducing dependence on costly human-annotated training data.

## Key Takeaways
- MAGE addresses a critical bottleneck in computer use agents: the need for long-horizon procedural knowledge and application-specific operation patterns when encountering unseen software. Rather than relying solely on visual observation and natural language instructions, the framework retrieves relevant sections from user manuals and employs a planner to generate explicit procedural guidance, effectively bridging the gap between general multimodal model capabilities and application-specific task requirements.
- The framework handles discrepancies between manuals and actual GUI environments—such as version differences, user settings, or interface variations—by adapting the agent policy through direct environment interaction. This dual approach of manual-guided planning combined with policy adaptation ensures robustness when documentation does not perfectly match the live software state.
- For training, MAGE converts user manuals into executable task-plan pairs and uses those plans to guide environment rollouts toward task-relevant states, generating trajectories that optimize the policy without requiring human-authored demonstrations. This unified design treats manuals as a scalable, low-cost data source for both execution-time reasoning and training-time policy optimization, substantially reducing the annotation burden that currently limits CUA development.

## Context
Computer use agents represent a frontier in applied AI, aiming to enable autonomous interaction with real-world software through GUIs. While multimodal foundation models have advanced visual understanding and instruction-following capabilities, generalizing to unseen applications remains a persistent challenge because practical software tasks demand procedural knowledge that is rarely captured in training corpora. The field has been constrained by the high cost and limited scalability of human-annotated task trajectories, making manual-based knowledge extraction a promising alternative pathway for scaling agent capabilities across diverse software ecosystems.

## Implications
For practitioners building autonomous agents for software automation, MAGE offers a practical blueprint for reducing training costs by repurposing existing user documentation as a knowledge source, which is particularly valuable for enterprises deploying agents across proprietary or rapidly evolving software stacks. For the broader AI research community, the work highlights that structured procedural knowledge embedded in manuals can complement visual perception in agent systems, suggesting future directions where documentation-aware reasoning becomes a standard component of embodied and software-interacting agents. The open-source release of code and reproduction scripts further supports reproducibility and community-driven extension of manual-guided agent learning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.23012v1)
