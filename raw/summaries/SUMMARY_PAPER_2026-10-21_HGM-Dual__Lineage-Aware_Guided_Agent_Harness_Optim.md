---
title: HGM-Dual: Lineage-Aware Guided Agent Harness Optimization for Long-Horizon Planning
url: http://arxiv.org/abs/2610.30042v1
type: paper-summary
date: 2026-10-21
source_paper: 2026-10-21_17-02-28Z_HGM_Dual_Lineage_AwareGuidedAgentHarnessOptimizati.md
generated_at: 2026-10-21 23:06
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
HGM-Dual introduces a diagnostic-guided framework for budget-efficient harness optimization of planning agents built on frozen or closed-source LLMs. The paper identifies that existing recursive self-improvement approaches like the Huxley-Godel Machine fail on planning tasks because the competence needed to modify an agent no longer aligns with the competence being improved, leading to wasteful exploration. HGM-Dual addresses this by combining lineage-aware context tracking with error-conditioned dual-path child generation, achieving up to 14.45% relative improvement in case accuracy while using 2x-4x fewer evaluation budget than HGM variants.

## Key Takeaways
- Lineage-aware context representation is a core innovation: instead of maintaining an unstructured archive of past agent variants, HGM-Dual explicitly records what each ancestor modified, which behaviors improved or regressed, and which modifications proved ineffective. This gives the editor agent explicit edit-outcome attribution, enabling it to avoid repeating failed modifications and to build on proven improvements across generations.
- Error-conditioned dual-path child generation splits exploration into two targeted strategies: a general child that preserves open-ended exploration for broad harness improvement, and specialized children that specifically target the harness components (prompts, tools, workflows) most likely responsible for the parent agent's highest-ranked constraint violations. This dual-path approach prevents the open-ended search from repeatedly exploring ineffective changes that consume substantial evaluation budgets.
- Planning tasks fundamentally break the self-improvement alignment assumed by coding-focused harness optimizers. In coding, the ability to improve code is the same ability being improved. In planning, an agent must produce sequences of tool calls satisfying interacting constraints, so the meta-competence of editing a harness diverges from the task competence of satisfying constraints, making naive recursive self-modification inefficient and requiring structured diagnostic guidance.

## Context
This paper sits at the intersection of automated agent optimization, evolutionary search over software artifacts, and long-horizon planning with tool-using LLM agents. As organizations increasingly deploy agents built on closed-source or frozen foundation models where fine-tuning is unavailable, harness optimization—editing prompts, tool definitions, and workflow scaffolds—becomes the primary lever for improving agent performance. Prior work such as the Darwin-Godel Machine and Huxley-Godel Machine demonstrated recursive self-improvement for coding tasks, but their assumptions do not transfer to planning domains where constraint satisfaction across multi-step tool interactions is the core challenge. HGM-Dual extends the evolutionary harness optimization paradigm into this harder regime by introducing structured diagnostic feedback rather than relying on blind mutation and selection.

## Implications
For practitioners deploying planning agents on closed-source LLMs, HGM-Dual offers a practical path to improving agent reliability on multi-step, constraint-heavy tasks without access to model weights or fine-tuning infrastructure, while dramatically reducing the evaluation compute needed for optimization. The lineage-aware and error-conditioned mechanisms suggest a broader principle for automated system optimization: structured attribution of past edit outcomes and targeted repair of diagnosed failure modes can outperform open-ended evolutionary search in domains where the optimization objective and the search space are misaligned. This has implications for any field involving automated configuration search over complex software systems, including DevOps automation, workflow orchestration, and agentic tool-use pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.30042v1)
