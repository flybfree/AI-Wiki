---
title: Long SKILL Compliance as Logical Reasoning: Closure-Grounded Detection with Scaling-Guided On-Policy Distillation
published: 2026-08-08T14:10:51Z
authors: Shuaitao Zhao, Feng Ni, Lichao Ma, Jiaye Lin, Fei Han, Yang Wei, Lu Pan
url: http://arxiv.org/abs/2608.08146v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Long SKILL Compliance as Logical Reasoning: Closure-Grounded Detection with Scaling-Guided On-Policy Distillation

## Abstract
The increasing complexity of enterprise business scenarios has promoted the widespread adoption of long SKILL documents in agent systems, posing new challenges for compliance detection: large models incur substantial inference costs, while small models may fail to maintain detection accuracy. To address this gap, we propose SkillCDG, a graph-based framework for long SKILL compliance detection. SkillCDG represents complex business policies as a two-layer constraint dependency graph, where the upper layer indexes SKILL descriptions for scenario routing and the lower layer captures dependencies among atomic constraints within each SKILL. During inference, two-level retrieval followed by dependency closure supports compliance judgment and source traceability. We comprehensively evaluate the framework on three enterprise datasets and two controlled public benchmark variants. Experimental results demonstrate that SkillCDG outperforms baseline methods by up to 12.8 percentage points in detection F1 score, while reducing token consumption by a maximum 64.3\%. Moreover, we further investigate the inherent relationships among policy-graph complexity, model scale, and detection performance. Comparative experiments conducted on four checkpoints from a single model family validate a concise and effective scaling trend: end-to-end detection correctness exhibits a complexity-differentiated scaling pattern, and the complexity metric derived from the constraint dependency graph can effectively quantify instance difficulty and the performance improvement potential of models. Leveraging this insightful scaling trend, we conduct adaptive training sample selection and adopt on-policy distillation to efficiently enhance the compliance detection capability of small-scale models.

## Metadata
- **Published**: 2026-08-08T14:10:51Z
- **Authors**: Shuaitao Zhao, Feng Ni, Lichao Ma, Jiaye Lin, Fei Han, Yang Wei, Lu Pan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08146v1)