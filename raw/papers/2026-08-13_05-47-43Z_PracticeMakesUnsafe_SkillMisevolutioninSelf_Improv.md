---
title: Practice Makes Unsafe: Skill Misevolution in Self-Improving LLM Agents
published: 2026-08-13T05:47:43Z
authors: Xutao Mao, Liangjie Zhao, Xiang Zheng, Cong Wang
url: http://arxiv.org/abs/2608.12851v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Practice Makes Unsafe: Skill Misevolution in Self-Improving LLM Agents

## Abstract
Self-improving LLM agents convert successful trajectories into persistent cross-task state. An unsafe success can thereby become reusable policy after its triggering input disappears. Skill evolution makes this failure measurable by distilling operational trajectories into executable, transferable, and inspectable procedures. Because evolution optimizes task outcomes rather than procedure safety, compromised experience can cause skill misevolution. Existing benchmarks measure current behavior or static artifacts but cannot attribute risk across authoring, retrieval, and later execution. To expose this lifecycle, we introduce SkillMisevo-Gym, a lifecycle-aware harness that versions skill state across agent frameworks, and SkillMisevo-Bench, a frozen design from malicious exposure to carryover tasks, with concept-aligned benign tasks and nine lifecycle metrics. We also introduce SafeEvolve, a wrapper that repairs unsafe content and governs subsequent reuse. Across 25 agent-method configurations, each covering 525 tasks in 25 episodes, all 21 evolved configurations author unsafe artifacts, while only fifteen lead to fresh-session harm. In the exposure sweep, three malicious tasks raise carryover ASR from 16.0% to 35.3%. Across representative skill evolution methods, SafeEvolve reduces unsafe retrieval and fresh-session harm by 26.7 and 17.3 percentage points, respectively, while mean benign utility changes by only 0.4 points. Together, persistent-adaptation safety must govern what updates write and what future executors reuse. Code is available at https://github.com/henrymao2004/misevolve.

## Metadata
- **Published**: 2026-08-13T05:47:43Z
- **Authors**: Xutao Mao, Liangjie Zhao, Xiang Zheng, Cong Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12851v1)