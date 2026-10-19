---
title: SkillBrowser: Selective Skill Exposure for Scalable Skill-Using Agents
url: http://arxiv.org/abs/2610.23554v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-16_14-44-01Z_SkillBrowser_SelectiveSkillExposureforScalableSkil.md
generated_at: 2026-10-18 21:46
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
SkillBrowser introduces a Meta-Skill-managed framework for Selective Skill Exposure (SSE) in large language model agents, enabling agents to dynamically identify their current capability needs, formulate targeted queries, and load only the relevant procedural skills on demand during reasoning. Evaluated across six SRA-Bench subsets and five different LLMs, the framework improves aggregate accuracy over both static retrieval and LLM-based skill selection methods, including in multi-step tool-use scenarios, while also reducing accuracy degradation on tasks the agent could already solve without additional skills.

## Key Takeaways
- Existing skill-exposure paradigms have complementary shortcomings: progressive disclosure introduces context pollution as skill libraries grow, while retrieval-based approaches rely on static queries derived from the initial task prompt, which can be misaligned with capability needs that emerge dynamically during multi-step reasoning and may still inject unnecessary skills into the context window.
- SkillBrowser addresses these gaps through a Meta-Skill-managed architecture that allows the agent itself to identify what capabilities it currently lacks, formulate targeted queries mid-reasoning, and selectively load only the skills it actually needs, rather than relying on a fixed or pre-determined retrieval strategy.
- The empirical evaluation demonstrates that SkillBrowser outperforms static retrieval and LLM-based selection baselines across diverse benchmarks and model families, including complex multi-step tool-use tasks, and notably mitigates the accuracy degradation that occurs when irrelevant skills are injected into already-solvable instances. However, the authors acknowledge that benefits remain model- and task-dependent, with under-invocation of useful skills and additional inference latency identified as key practical limitations.

## Context
As LLM agents increasingly depend on external skill libraries to handle complex, multi-step tasks such as tool use, code generation, and domain-specific reasoning, the question of how to scale these libraries without degrading agent performance has become a central challenge in agent system design. SkillBrowser contributes to this growing research area by reframing skill access as a dynamic, agent-driven decision process rather than a static retrieval problem, aligning with broader efforts in the AI community to build agents that can manage their own context and capabilities adaptively.

## Implications
For practitioners building production agent systems, SkillBrowser offers a practical blueprint for managing large skill repositories without incurring the context pollution or misaligned retrieval costs that plague current approaches, potentially enabling agents to scale to thousands of skills while maintaining reasoning quality. For the broader field, the work validates the viability of Meta-Skill-managed SSE as a design principle for scalable agent architectures, though the acknowledged limitations around under-invocation and latency signal that further engineering and research are needed before these systems can be deployed at full production scale.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.23554v1)
