---
title: RoboFoundry: System-as-Policy Evolution for Self-Learning Embodied Agents
url: http://arxiv.org/abs/2609.32862v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-26_18-41-03Z_RoboFoundry_System_as_PolicyEvolutionforSelf_Learn.md
generated_at: 2026-09-28 22:58
model: qwen3.6-35b-a3b
---

## Summary
RoboFoundry introduces a novel embodied agentic framework that treats the supporting system itself as a unified policy, enabling self-evolving capabilities through the conversion of execution traces into validated system updates. The method addresses gaps in decision-making and memory management by evolving both context systems and hierarchical skill structures across heterogeneous robots via a shared semantic interface. Experiments demonstrate state-of-the-art performance on benchmarks like EmbodiedBench, RoboMemArena, and LIBERO-PRO, with significant improvements over existing baselines and strong zero-shot transfer capabilities in real-world deployments.

## Key Takeaways
- RoboFoundry shifts focus from optimizing isolated agent components to a "System-as-Policy" approach where execution experience is transformed into persistent, validated system changes, allowing the framework to diagnose capability gaps and promote recurring improvements to general system capabilities over time.
- Evolution operates across two complementary surfaces: a context system managing active internal context and persistent file-system memory, and a hierarchical skill system organizing atomic skills, compositions, and recovery mechanisms; a shared semantic interface decouples embodiment-invariant decisions from specific execution, enabling evolved capabilities to transfer seamlessly across heterogeneous robotic platforms.
- RoboFoundry achieves state-of-the-art results on EmbodiedBench, notably boosting GPT-5.5 by 27.8% and bringing Qwen3.7-Plus to near parity with GPT-5.5; it also dominates long-horizon memory tasks on RoboMemArena with gains of at least 39.0% over baselines and outperforms Cap-Agent0 by up to 679.7% on LIBERO-PRO, while demonstrating successful zero-shot transfer and online evolution in real-world scenarios.

## Context
Current embodied AI research often fragments the agent stack by optimizing individual modules like memory or skills in isolation, failing to leverage the system as a cohesive policy that can adapt based on interaction history. This paper addresses a critical limitation where mere interaction does not guarantee self-improvement without mechanisms to convert transient execution traces into durable, validated structural updates within the agent

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.32862v1)
