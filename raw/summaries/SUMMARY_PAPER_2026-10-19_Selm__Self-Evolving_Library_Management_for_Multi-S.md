---
title: Selm: Self-Evolving Library Management for Multi-Skill Agent Optimization
url: http://arxiv.org/abs/2610.24630v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-17_11-07-02Z_Selm_Self_EvolvingLibraryManagementforMulti_SkillA.md
generated_at: 2026-10-19 20:48
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
SELM (Self-Evolving Library Management) is a framework that reformulates skill evolution in LLM agents as a library-level management problem, jointly handling skill retrieval, updating, and lifecycle management through confidence and utility signals. Evaluated across four agent benchmarks spanning diverse tasks and execution environments, SELM consistently outperforms prior methods in most settings, demonstrating that systematic skill library management enables agents to accumulate, reuse, and maintain useful skills across domains rather than treating each task in isolation.

## Key Takeaways
- Utility-aware retrieval is a core mechanism in SELM that selects skills based on their demonstrated usefulness rather than simple similarity matching. By maintaining skill confidence and utility signals, the framework ensures that agents retrieve only skills that have proven effective in prior tasks, reducing noise and improving task performance on subsequent queries.
- The Map-Reduce framework for skill updating generates targeted, task-specific modifications to existing skills from new task trajectories. Rather than wholesale replacement or uncontrolled accumulation, this approach produces focused updates that refine skills incrementally, allowing the library to incorporate new experience without degrading previously validated knowledge.
- Lifecycle controls govern the retention or removal of skills based on their ongoing effectiveness. This pruning mechanism prevents skill library bloat and degradation over time, ensuring that the library remains a curated, high-quality resource rather than an ever-growing collection of potentially obsolete or conflicting skills.

## Context
LLM agents increasingly rely on "skills" as lightweight, reusable units of task-specific knowledge acquired from execution trajectories. Prior work on skill evolution has focused on generating new skills from individual task experiences but has largely neglected the systematic management needed to make those skills reusable across domains. SELM addresses this gap by treating the skill collection as a managed library with retrieval, update, and lifecycle policies, bridging the divide between one-off skill generation and long-term, cross-domain knowledge accumulation in autonomous agents.

## Implications
For practitioners building multi-skill agent systems, SELM provides a principled blueprint for maintaining skill quality over time, which is critical for deploying agents in production environments where tasks span diverse domains and execution contexts. The framework's consistent benchmark improvements suggest that library-level management—not just skill generation—is the bottleneck in current agent systems, pointing industry toward investing in retrieval infrastructure, confidence tracking, and automated pruning pipelines as essential components of next-generation agent architectures.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.24630v1)
