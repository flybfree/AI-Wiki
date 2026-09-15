---
title: MUSE: A Theory-Harnessed Story Engine for Vibe Narrativizing
published: 2026-09-14T08:09:44Z
authors: Jianxiang Ma, Xiaocui Yang, Daling Wang, Yuesong Hou, Mingfu Zhang, Yichen Gao, Junzhao Huang
url: http://arxiv.org/abs/2609.15188v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MUSE: A Theory-Harnessed Story Engine for Vibe Narrativizing

## Abstract
LLMs can generate fluent prose. Story quality depends on how decisions about plot, character, and language work together across planning, drafting, and revision. Guiding these decisions presents two bottlenecks: the quality of story guidance and its sustained use. We formulate Vibe Narrativizing as the task of turning natural-language writing requirements into a finished story and present MUSE, a Theory-Harnessed Story Engine. MUSE organizes story knowledge as guidance for specific decisions and carries those decisions into subsequent creative work. Knowledge engineering develops Robert McKee's story theory through rule atomization, semantic consolidation, and mechanism abstraction; a single source of truth and layered disclosure organize the resulting guidance. Typical examples complement principles that depend on context and aesthetic judgment. An agent harness organizes design, character performance, scene composition, and revision through intermediate deliverables that preserve story decisions. Context engineering supplies each role with the relevant guidance and decisions, while a masterwork corpus provides inspiration and prose references. A worked example follows one requested object from its thematic role to the characters' climactic actions. Across four base models, MUSE improves WritingBench by 1.6-4.8 points over zero-shot generation and raises LongStoryEval by more than ten points on three. ConStory-Bench consistency error density remains in the low single digits for all four models, below every reproduced story-system baseline on three. Component ablations locate the largest quality contribution in structural design, voice-specific effects in the character path, and further gains in revision. Code is available at https://github.com/RoadtoAGI/MUSE.

## Metadata
- **Published**: 2026-09-14T08:09:44Z
- **Authors**: Jianxiang Ma, Xiaocui Yang, Daling Wang, Yuesong Hou, Mingfu Zhang, Yichen Gao, Junzhao Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.15188v1)