---
title: SkillFocus: Evolving Agent Skills via Capability Decomposition
published: 2026-09-28T06:11:08Z
authors: Ning Wang, Zhiren Gong, Bingdong Li, Peng Yang, Aimin Zhou
url: http://arxiv.org/abs/2609.34397v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SkillFocus: Evolving Agent Skills via Capability Decomposition

## Abstract
Agent skill evolution seeks to improve reusable procedural guidance for large language model (LLM) agents through iterative revision. Existing methods base each revision mainly on execution trajectories or feedback, leaving recurring behavioral requirements across tasks implicit and tying revision to the behavior of the current skill. We introduce SkillFocus, which decomposes recurring task requirements into a capability space that remains fixed as the skill evolves, separating what tasks require from how the current skill behaves. SkillFocus maps current task outcomes to this space to identify the capability that leaves the most tasks unresolved, then uses that capability to determine what to revise and which evidence to use. Across four benchmarks spanning heterogeneous tasks, SkillFocus achieves the best held-out accuracy on all four, outperforming the strongest competing result by 5.7 points on average while using 24\% fewer evolution tokens on average than the closest iterative baseline. Controlled studies further show that capabilities derived from recurring task requirements outperform task-semantic and execution-derived alternatives, while randomizing task--capability assignments reduces final accuracy by up to 20.2 points. Matching evidence to the selected capability increases candidate gain by 4.4 points under prioritized revision.

## Metadata
- **Published**: 2026-09-28T06:11:08Z
- **Authors**: Ning Wang, Zhiren Gong, Bingdong Li, Peng Yang, Aimin Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34397v1)