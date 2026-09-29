---
title: SkillFocus: Evolving Agent Skills via Capability Decomposition
url: http://arxiv.org/abs/2609.34397v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_06-11-08Z_SkillFocus_EvolvingAgentSkillsviaCapabilityDecompo.md
generated_at: 2026-09-28 23:09
model: qwen3.6-35b-a3b
---

## Summary
SkillFocus addresses limitations in agent skill evolution by decomposing recurring task requirements into a fixed capability space, effectively separating what tasks require from how the current skill behaves to guide iterative revisions. By mapping outcomes to this space to identify unresolved capabilities and selecting targeted evidence, the method achieves state-of-the-art accuracy across four benchmarks while reducing token consumption by 24% compared to strong baselines.

## Key Takeaways
- SkillFocus introduces a fixed capability space derived from recurring task requirements, decoupling task demands from the current skill's behavior; this separation prevents revisions from being tethered to transient behavioral patterns and ensures evolution targets remain consistent across iterations.
- The approach delivers superior performance on four heterogeneous benchmarks, outperforming the strongest competing result by an average of 5.7 points in held-out accuracy while utilizing 24% fewer evolution tokens than the closest iterative baseline, demonstrating significant gains in both effectiveness and efficiency.
- Ablation studies highlight that capabilities extracted from recurring requirements significantly outperform task-semantic or execution-derived alternatives, with matching evidence to selected capabilities boosting candidate gain by 4.4 points; randomizing task-capability assignments causes accuracy drops of up to 20.2 points, underscoring the importance of structured capability mapping.

## Context
As large language model agents tackle increasingly complex workflows, evolving reusable procedural skills is essential for maintaining performance and adaptability over time. Current evolution methods often rely on execution trajectories or feedback that leave recurring behavioral requirements implicit, creating inefficiencies and limiting generalization across tasks with shared underlying demands but different surface-level semantics.

## Implications
SkillFocus enables practitioners to build more efficient agent systems by lowering the computational cost of skill refinement while achieving higher accuracy, facilitating scalable deployment in production environments where resource optimization is critical. The capability decomposition framework offers a principled mechanism for diagnosing and improving agent limitations, potentially influencing future architectures that prioritize structured behavioral analysis over reactive feedback loops.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34397v1)
