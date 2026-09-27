---
title: HEXIS: Compiling Skills into Extended Finite State Machines
url: http://arxiv.org/abs/2609.30123v1
type: paper-summary
date: 2026-09-27
source_paper: 2026-09-24_16-58-18Z_HEXIS_CompilingSkillsintoExtendedFiniteStateMachin.md
generated_at: 2026-09-27 16:15
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces HEXIS, a framework that compiles agent skills into Extended Finite State Machines to decouple task reasoning from control decisions, ensuring agents follow prescribed steps accurately while recording execution progress and intermediate results. By mapping skill clauses and tool interfaces to explicit state operations, local instructions, data bindings, and transition conditions, HEXIS prevents the omission or incorrect application of instructions that often plague inference-heavy approaches. The method achieves a 16.1 percentage point average improvement in success over Skill + ReAct across four benchmarks and reduces execution tokens by up to 88.9%.

## Key Takeaways
- HEXIS utilizes an incremental compiler to transform skill clauses and tool interfaces into structured state operations, local instructions that guide reasoning within states, data bindings, and explicit transition conditions, thereby separating knowledge from control flow logic.
- The system ensures reliability by aligning new development traces with existing states to identify missing operations or dependencies, accepting updates only after rigorous static checks and successful replay of both current and all previously accepted execution traces.
- Evaluations across four benchmarks and four executors demonstrate that HEXIS improves

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.30123v1)
