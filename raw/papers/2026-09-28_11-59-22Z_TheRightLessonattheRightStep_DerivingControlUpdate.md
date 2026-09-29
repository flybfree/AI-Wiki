---
title: The Right Lesson at the Right Step: Deriving Control Updates for Self-Evolving Agents
published: 2026-09-28T11:59:22Z
authors: Yunhe Su, ZiYi Dong, Tong Yu, Weijian Deng, Hao Li, Bowen Jiang, Pengxu Wei
url: http://arxiv.org/abs/2609.34988v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Right Lesson at the Right Step: Deriving Control Updates for Self-Evolving Agents

## Abstract
Self-evolving agents improve future behavior by reusing past experience, typically as global prompts, memories, or reflections. Yet these mechanisms rarely control where experience takes effect. In long tool-use workflows, the same lesson may correct one decision but distract another, making experience reuse a problem of localized control rather than memory alone. We introduce EvoCUE (Evolution through Control Updates from Evidence), a framework for learning reusable control-program updates from completed agent executions. EvoCUE represents the agent as an explicit state-machine controller, whose nodes perform model or tool calls and whose edges define where control passes next. This makes the workflow editable at precise locations, so each learned update can specify what to add, where it acts, and when it applies. From completed trajectories, EvoCUE uses residual goals and observed execution traces to propose localized instruction or skill edits. Each candidate is evaluated at the point where it would act by resuming the parent and edited controllers from the same checkpoint and comparing their final outcomes. Accepted edits are compiled with applicability rules, confirmed on held-out tasks, and inherited by later executions. We evaluate EvoCUE on long tool-use environments where learned conventions must reach the right execution step. From a minimal AppWorld controller without benchmark-specific onboarding instructions, EvoCUE learns the missing task-completion convention and substantially improves success on Test-Normal and Test-Challenge. On PAST-Bench office workflows, EvoCUE transfers organizational requirements from prior episodes to later tasks, improving task-execution quality. These results show that self-evolving agents should place experience inside the control flow, rather than only store it as text.

## Metadata
- **Published**: 2026-09-28T11:59:22Z
- **Authors**: Yunhe Su, ZiYi Dong, Tong Yu, Weijian Deng, Hao Li, Bowen Jiang, Pengxu Wei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34988v1)