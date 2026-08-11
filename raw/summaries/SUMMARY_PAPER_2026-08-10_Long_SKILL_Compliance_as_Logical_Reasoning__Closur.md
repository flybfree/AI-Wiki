---
title: Long SKILL Compliance as Logical Reasoning: Closure-Grounded Detection with Scaling-Guided On-Policy Distillation
url: http://arxiv.org/abs/2608.08146v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_14-10-51Z_LongSKILLComplianceasLogicalReasoning_Closure_Grou.md
generated_at: 2026-08-10 22:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SkillCDG, a graph‑based framework for detecting compliance in long SKILL documents, and shows that it improves detection F1 scores by up to 12.8 points while cutting token usage by at most 64.3 %. The authors also reveal a scaling trend linking policy‑graph complexity, model size, and performance, enabling adaptive training and on‑policy distillation for small models.

## Key Takeaways
- SkillCDG encodes business policies as a two‑layer constraint dependency graph, allowing retrieval of SKILL descriptions and closure of atomic constraints to achieve compliance judgment.  
- The framework reduces token consumption by up to 64 % compared with baseline methods, demonstrating that inference can be both faster and more accurate.  
- A scaling trend is observed: end‑to‑end detection correctness varies predictably with the complexity metric derived from the constraint dependency graph.

## Context
Long SKILL documents are common in enterprise AI agents, yet their compliance detection remains costly for large models and inaccurate for small ones. This work addresses that tension by introducing a scalable, graph‑driven approach that balances accuracy and efficiency across model sizes.

## Implications
For practitioners, SkillCDG offers a practical way to deploy compliant agents without sacrificing performance on resource‑constrained hardware. The identified scaling relationship can guide model selection and training strategies, fostering more sustainable AI systems in real‑world business environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08146v1)
