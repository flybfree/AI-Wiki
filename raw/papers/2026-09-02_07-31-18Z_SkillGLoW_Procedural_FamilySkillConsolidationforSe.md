---
title: SkillGLoW: Procedural-Family Skill Consolidation for Self-Improving Agents on Long-Horizon Task Streams
published: 2026-09-02T07:31:18Z
authors: Ao Yan, Xin Zhang, Jiawei Du, Joey Tianyi Zhou
url: http://arxiv.org/abs/2609.02217v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SkillGLoW: Procedural-Family Skill Consolidation for Self-Improving Agents on Long-Horizon Task Streams

## Abstract
LLM agents increasingly self-improve by writing and reusing textual skills, kept either as one global document or as a flat pool of per-task entries, though most of the evidence comes from domains with structurally similar tasks. On long-horizon workloads where each task demands a different solution, the two forms fail in opposite ways: the document collapses into generic discipline, while the pool inflates and its entries stay bound to the instance that wrote them. We argue the missing unit of reuse is the solving procedure shared by a cluster of related tasks, and build SkillGLoW (Global-Local Weave) around it: the local skills a task writes from its own execution are aggregated into procedural families and compressed into de-instantiated global priors, while the instance detail they hold is regenerated per task rather than stored; a commit gate admits a prior only when real execution shows it does not degrade the deployed library. Across four benchmarks (mathematical reasoning, terminal automation, software repair, and embodied control) and three models, the priors gain 17.2 points (hard) over the no-skill baseline on average, with positive gains in all 12 continual-improvement runs, and 18.0 with local regeneration, while the library holds one prior per procedural family, 3.6x more compact than the per-task pool. Under the same protocol GLoW leads a published single-document optimizer on 15 of 21 cells. Unmodified, the library lifts success on unseen ALFWorld tasks from 73.9% to 83.9%, evidence that what transfers is procedure rather than task memory.

## Metadata
- **Published**: 2026-09-02T07:31:18Z
- **Authors**: Ao Yan, Xin Zhang, Jiawei Du, Joey Tianyi Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02217v1)