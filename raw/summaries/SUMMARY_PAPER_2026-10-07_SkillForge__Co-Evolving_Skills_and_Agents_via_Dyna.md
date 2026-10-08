---
title: SkillForge: Co-Evolving Skills and Agents via Dynamic Skill Lifecycles
url: http://arxiv.org/abs/2610.09832v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-07_10-52-15Z_SkillForge_Co_EvolvingSkillsandAgentsviaDynamicSki.md
generated_at: 2026-10-07 21:11
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
SkillForge introduces a fitness-driven skill lifecycle framework that co-evolves an agent's skill library alongside its policy during reinforcement learning training, preventing obsolete or harmful skills from accumulating as the model improves. The method achieves the highest aggregate success rate across multiple interactive agent benchmarks, delivering up to 7.8% relative improvement over the strongest baseline while maintaining a compact skill library throughout training.

## Key Takeaways
- SkillForge structures skill management through a four-state lifecycle—trial, active, stable, and retired—driven by fitness evaluations, ensuring that skills are selectively retired, stabilized, or mutated via LLM-guided operations at each RL iteration rather than being retained indiscriminately as the policy improves.
- A pre-RL evaluation phase leverages the base model's own rollouts to pre-retire low-fitness skills before supervised fine-tuning begins, producing a filtered library that seeds the initial checkpoint and prevents early training from being corrupted by poor-quality skill entries.
- The authors introduce SkillFurnace, a dataset of over 5,000 annotated records that bundles retirement-filtered SFT trajectories, evolved skill libraries with fitness annotations, and retirement events tagged with human-annotated failure categories, providing a dedicated resource for research on skill quality assessment and lifecycle management.

## Context
Memory-augmented reinforcement learning has emerged as a powerful paradigm for enabling LLM agents to tackle complex long-horizon tasks, with skills serving as a structured form of memory that pairs executable instructions with applicability conditions over task types. However, the field has struggled with the static retention of skills, where growing libraries introduce noise, redundancy, and misleading guidance as the underlying policy evolves. SkillForge addresses this gap by treating skill curation as a dynamic, fitness-driven process tightly coupled to policy optimization, bridging the disconnect between memory management and learning dynamics that has limited prior agentic RL systems.

## Implications
For practitioners building autonomous agents, SkillForge demonstrates that actively pruning and evolving a skill library during training—not just at deployment—yields both higher task success and smaller, more interpretable memory stores, which is critical for production systems where latency and context-window constraints matter. The introduction of SkillFurnace provides the community with a benchmark-quality resource for studying why skills fail and how to detect degradation, potentially accelerating the development of self-improving agent architectures. For the broader AI research community, the co-evolution paradigm suggests that future agent training pipelines should treat memory components as first-class trainable objects rather than static scaffolding, reshaping how reinforcement learning frameworks are designed for tool-using and multi-step reasoning agents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.09832v1)
