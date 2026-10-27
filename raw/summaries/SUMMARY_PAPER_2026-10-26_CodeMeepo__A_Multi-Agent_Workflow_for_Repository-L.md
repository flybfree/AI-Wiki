---
title: CodeMeepo: A Multi-Agent Workflow for Repository-Level Code Migration and Optimization
url: http://arxiv.org/abs/2610.34633v1
type: paper-summary
date: 2026-10-26
source_paper: 2026-10-25_23-15-38Z_CodeMeepo_AMulti_AgentWorkflowforRepository_LevelC.md
generated_at: 2026-10-26 23:19
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
CodeMeepo is a multi-agent pipeline designed to perform complete and efficient repository-level code migration across programming languages while preserving observable behavior. The system addresses three core challenges in LLM-based code migration—self-referential test authoring, context window limitations for large repositories, and performance degradation in translated code—by introducing external oracles, ordered milestones, and a benchmark-guided optimization phase. On nine benchmark subjects spanning three language pairs, CodeMeepo achieves the highest pass rates and outperforms a state-of-the-art multi-agent baseline by 18% in test pass rate.

## Key Takeaways
- CodeMeepo separates the roles of translation and acceptance testing by evaluating each migration milestone against a fixed external oracle that the agents neither author nor modify. This prevents the critical failure mode where an agent writing both the translation and its tests overlooks the same requirements in both, leaving missing or incorrect behavior undetected. A separate parity assessment further compares source and target components in scope and feeds identified gaps back into the migration plan as required work.
- To handle repositories that exceed a model's context window, CodeMeepo uses ordered milestones that limit the scope of each individual task, combined with cumulative regression checks that guard against breaking already-migrated behavior. Eight specialized agent roles communicate through file artifacts, and a deterministic state machine governs repair, deferral, scope changes, and termination, ensuring systematic coverage rather than ad hoc task division.
- A benchmark-guided optimization phase addresses the problem that behaviorally correct translations may be slower than the original implementation. On a production daemon, this optimization phase improved half of the benchmarks by 25% on average, demonstrating that correctness alone is insufficient for production-grade migration and that performance must be explicitly targeted as a separate pipeline stage.

## Context
Repository-level code migration is a long-standing challenge in software engineering, and the emergence of large language model agents has made end-to-end automated migration newly feasible but still unreliable. Prior multi-agent approaches typically allow the same agent to both produce code and define its acceptance criteria, creating a blind spot that CodeMeepo explicitly eliminates through external oracles and parity assessments. This work sits at the intersection of multi-agent orchestration, software testing, and compiler/translation research, pushing the field toward provably complete behavioral preservation rather than partial or best-effort translation.

## Implications
For industry practitioners managing legacy codebases, CodeMeepo offers a structured, auditable pipeline that can migrate entire projects across language ecosystems—such as moving from C++ to Rust or Java to Kotlin—while maintaining behavioral guarantees and improving runtime performance. The deterministic state machine and role-based agent architecture provide a reproducible framework that could be adapted to other large-scale software transformation tasks, including dependency upgrades, framework migrations, and security hardening. The demonstrated 18% improvement over existing baselines signals that careful separation of concerns among agent roles is a more effective strategy than simply scaling a single agent's capabilities.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.34633v1)
