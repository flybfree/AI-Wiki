---
title: From Execution to Capability: Scientific Experience Consolidation via Procedural Knowledge Synthesis
url: http://arxiv.org/abs/2607.24459v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_14-01-32Z_FromExecutiontoCapability_ScientificExperienceCons.md
generated_at: 2026-07-27 22:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SciConsolidate, a method for converting verified scientific‑computing experiences into transferable procedural knowledge that can be used to improve model performance across tasks. It shows that injecting runtime procedures into the training process boosts Qwen3.6-27B by several points but does not help smaller models, highlighting an abstraction‑execution gap.

## Key Takeaways
- Verified success and failure trajectories are contrasted to generate cross‑task computational procedures rather than source‑specific fixes.
- The method uses answer‑free query synthesis to expand consolidation data without needing pre‑existing reference answers, allowing the target model to learn abstract procedures.
- Procedure‑guided concretization improves Qwen3.6-27B by +3.85/+6.26 sub‑step and main‑problem points but yields little gain for Qwen3.5-9B, demonstrating the abstraction‑execution gap.

## Context
Large language models are being applied to scientific computing where each problem is solved independently, leading to fragmented knowledge that does not transfer between tasks. This work addresses the need for durable, reusable procedural knowledge that can be synthesized from runtime experience, a challenge central to building self‑improving AI assistants.

## Implications
For researchers, SciConsolidate offers a practical pathway to scale scientific assistance by turning isolated experiences into generalizable procedures. For industry practitioners, it suggests that integrating execution feedback into model training could yield measurable performance gains, especially for larger models, while smaller models benefit from guided abstraction rather than direct code supervision.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24459v1)
