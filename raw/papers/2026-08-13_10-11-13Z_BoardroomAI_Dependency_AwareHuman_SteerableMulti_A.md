---
title: BoardroomAI: Dependency-Aware Human-Steerable Multi-Agent Deliberation through Evolving Decision Graphs
published: 2026-08-13T10:11:13Z
authors: Sanjeev Manivannan
url: http://arxiv.org/abs/2608.13046v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BoardroomAI: Dependency-Aware Human-Steerable Multi-Agent Deliberation through Evolving Decision Graphs

## Abstract
Organizational decisions are co-created while evidence, constraints, and human priorities continue to evolve. In conventional transcript-based multi-agent systems, humans typically provide an initial problem, agents deliberate internally, and the system returns a final response. BoardroomAI instead treats the human as a persistent participant who can intervene by challenging assumptions, modifying constraints, changing priorities, introducing evidence, or redirecting the decision process. We operationalize this human--agent coexistence through four components: (i) a typed decision graph representing evidence, assumptions, constraints, claims, objections, alternatives, risks, decisions, semantic dependencies, and specialist responsibility; (ii) an intervention compiler that converts confirmed human actions into explicit graph updates; (iii) dependency-aware propagation that identifies affected subgraphs, preserves unaffected artifacts, and selectively reactivates relevant specialists; and (iv) an evaluation framework measuring intervention impact, repair coverage, preservation, recomputation, and decision validity. Across 600 generated decision-DAG interventions, propagation matched exhaustive impact computation while inspecting only 14.59% of nodes. In a 12-case exploratory pilot, selective repair recomputed 62.11% of canonical nodes, preserved all gold-unaffected nodes, and produced valid updated decisions in six cases while abstaining in the remaining six. These abstentions show that correct intervention routing may still provide insufficient context for synthesis, motivating a \emph{decision-sufficient context closure} for human-steered multi-agent deliberation. All results are synthetic and prototype-level.

## Metadata
- **Published**: 2026-08-13T10:11:13Z
- **Authors**: Sanjeev Manivannan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13046v1)