---
title: RSIPO: Recursive Self-Improving Policy Optimization for Agentic Reinforcement Learning via Skill-Policy Co-Evolution
url: http://arxiv.org/abs/2610.15772v1
type: paper-summary
date: 2026-10-13
source_paper: 2026-10-11_16-54-58Z_RSIPO_RecursiveSelf_ImprovingPolicyOptimizationfor.md
generated_at: 2026-10-13 21:49
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces RSIPO, a recursive self-improving policy optimization framework for agentic reinforcement learning that enables agentic skills and the policy model to co-evolve during training. Rather than relying on a static teacher model conditioned on fixed privileged context, RSIPO allows the policy itself to extract skills from completed trajectories and optimize its skill-generation capability through trajectory replay, while using empirical Bayes shrinkage to dynamically calibrate the student's trust in potentially unreliable teacher supervision. Experiments with Qwen-family models demonstrate substantial improvements, achieving a 98.6% average success rate on ALFWorld with Qwen2.5-7B, representing a 17.4% absolute improvement over standard GRPO.

## Key Takeaways
- RSIPO addresses a critical gap in existing agentic RL methods that combine RLVR with on-policy self-distillation: these methods typically treat agentic skills as static privileged context for a teacher model, ignoring the fact that skills should evolve on-policy alongside the student policy. RSIPO closes this gap by enabling the policy to extract and refine skills from its own completed trajectories, creating a recursive self-improvement loop.
- The framework introduces empirical Bayes shrinkage as a principled mechanism to dynamically calibrate how much the student policy should trust teacher-generated token scores. This acknowledges that skill-enhanced teacher guidance is not uniformly reliable, and blindly trusting it can degrade learning. The shrinkage approach adaptively weights teacher supervision based on empirical evidence of its reliability.
- On embodied interaction tasks (ALFWorld) and search-based agentic tasks, RSIPO outperforms all compared baselines. With Qwen2.5-7B, it achieves 98.6% average success on ALFWorld, surpassing the second-best baseline by 2.5% and standard GRPO by 17.4%, demonstrating that co-evolving skills and policy yields substantial gains in long-horizon credit assignment.

## Context
Agentic reinforcement learning has emerged as a critical paradigm for training language models to perform multi-step interactive tasks such as embodied navigation, tool use, and information retrieval. A major challenge in this domain is credit assignment across long trajectories, where reward signals are sparse and delayed. Recent methods like GRPO and RLVR combined with self-distillation attempt to address this by providing dense token-level supervision from a teacher model conditioned on privileged context. However, these approaches treat the teacher's skill-based guidance as fixed and assume its reliability, which limits their effectiveness as the student policy evolves. RSIPO represents a shift toward treating skill generation as a learnable, on-policy capability rather than a static input.

## Implications
For practitioners building agentic AI systems, RSIPO suggests that training pipelines should not separate skill acquisition from policy optimization but instead integrate them into a unified, recursive loop. This has practical implications for deploying smaller language models in complex interactive environments, as the 17.4% improvement over GRPO with a 7B-parameter model indicates that co-evolutionary training can extract substantially more capability from limited model capacity. For the broader field, the empirical Bayes shrinkage mechanism offers a transferable principle for any self-distillation or teacher-student training setup where teacher reliability is uncertain, potentially improving robustness across diverse RL and imitation learning applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.15772v1)
