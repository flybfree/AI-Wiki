---
title: Reliable Memory from Unstable Growth: Curating Self-Written Agent Playbooks with Randomized Experiments
url: http://arxiv.org/abs/2610.18427v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_14-06-05Z_ReliableMemoryfromUnstableGrowth_CuratingSelf_Writ.md
generated_at: 2026-10-14 00:27
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Randomized Block Curation (RBC), a method for evaluating and selecting lessons in self-written agent playbooks by measuring their actual effect on task success through randomized experiments rather than relying on the agent's own judgment. The authors demonstrate that current memory-augmented agent systems like ACE and Dynamic Cheatsheet suffer from extreme performance instability—up to 69.6 points below baseline—when the agent decides which lessons to retain. RBC addresses this by grouping lessons into blocks, randomly including or excluding them across practice tasks, and empirically selecting only those blocks that measurably improve success, raising average performance to 66.9 across multiple models and benchmarks.

## Key Takeaways
- Self-written playbooks in persistent memory systems are inherently unstable: the same procedure can produce a playbook that helps or one that falls up to 69.6 points below having no playbook at all, making agent self-judgment an unreliable curation mechanism for deciding which lessons to keep.
- RBC works by grouping related lessons into blocks sized large enough to produce measurable effects on success rates, then running randomized inclusion/exclusion experiments on practice tasks so that the performance gap between tasks with and without a block provides an unbiased causal estimate of that block's contribution.
- Because a single curation procedure can yield either a helpful or harmful playbook, RBC grows multiple candidate playbooks and selects whichever curated, whole, or empty playbook scores best on fresh practice episodes, achieving 66.9 average success versus 55.5 (whole playbook), 54.1 (no playbook), and 53.8 (agent-judgment curation) across two memory systems, three models, and three benchmarks.

## Context
Persistent textual memory for language-model agents—where lessons are written after tasks and injected into future prompts—has emerged as a practical alternative to fine-tuning for improving multi-step task performance. Systems like ACE and Dynamic Cheatsheet pioneered this approach, but they delegate the critical curation decision to the agent itself, creating a reliability gap that limits deployment in safety-critical or production settings. This paper sits at the intersection of LLM agent design, experimental methodology, and prompt engineering, applying principles from randomized controlled trials to the problem of what an agent should remember.

## Implications
For practitioners building agentic systems that accumulate experience over time, RBC offers a principled, model-agnostic curation layer that can be bolted onto existing memory architectures without retraining, substantially reducing the risk of performance degradation from harmful self-generated lessons. For the broader field, the finding that agent self-assessment of lesson quality is worse than doing nothing (53.8 vs. 54.1) challenges a common design assumption and suggests that empirical validation loops should become standard practice in any system where agents write and reuse their own knowledge.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.18427v1)
