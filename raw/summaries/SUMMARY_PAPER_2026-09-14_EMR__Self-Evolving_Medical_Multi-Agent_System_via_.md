---
title: EMR: Self-Evolving Medical Multi-Agent System via Experience Mining and Reuse
url: http://arxiv.org/abs/2609.15161v1
type: paper-summary
date: 2026-09-14
source_paper: 2026-09-14_07-41-56Z_EMR_Self_EvolvingMedicalMulti_AgentSystemviaExperi.md
generated_at: 2026-09-14 22:21
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
This paper introduces EMR, a self-evolving medical multi-agent system designed to overcome the static strategy limitations and lack of persistent memory in current large language model-driven clinical reasoning approaches. By implementing a hierarchical experience library and an automated mining process that extracts both successful diagnostic insights and failure warnings from agent interactions, EMR continuously refines its knowledge base. Experimental results demonstrate that this architecture consistently outperforms state-of-the-art medical multi-agent baselines while enabling cross-specialty generalization across different LLM backbones.

## Key Takeaways
- EMR organizes accumulated clinical knowledge into a hierarchical library comprising three distinct levels: foundational clinical principles, recurring diagnostic patterns, and representative case studies, which collectively structure the system's persistent memory.
- The inference pipeline emulates real-world multidisciplinary consultations by deploying a central planner agent that coordinates specialized department agents for domain-specific reasoning, followed by a summary agent that synthesizes their outputs into a cohesive final diagnosis.
- A critical innovation is EMR’s automatic experience mining mechanism, which continuously extracts correct diagnostic insights and failure-related warnings from multi-agent reasoning trajectories to incrementally update the experience library, enabling true self-evolution without manual intervention.

## Context
The rapid advancement of large language models has spurred significant interest in multi-agent architectures for complex decision-making tasks, particularly in high-stakes domains like healthcare. However, most existing systems rely on fixed prompting strategies and lack mechanisms to retain or build upon past interactions, limiting their adaptability and long-term reliability. This research addresses a critical gap by introducing persistent clinical memory into the agent workflow, aligning with broader AI trends that emphasize continuous learning and dynamic knowledge retention over static inference

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.15161v1)
