---
title: SkillSpec: Consensus-Gated Agent Skill Evolution via Representation Specialization
published: 2026-09-30T20:52:00Z
authors: Huancheng Chen, Xiaodi Sun, Zhaoqiong Huang, Shenyang Huang Shreya Singhal, Jingwen Lu
url: http://arxiv.org/abs/2610.00704v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SkillSpec: Consensus-Gated Agent Skill Evolution via Representation Specialization

## Abstract
Natural-language skills are textual procedural memories through which large language model (LLM) agents retain reusable task knowledge without updating model weights. Existing methods typically treat skills as either static artifacts or monolithic documents optimized using aggregate validation scores as feedback. However, representing a skill as a monolithic document restricts optimization to its textual content, without explicitly modeling the structure through which procedural knowledge is retrieved and executed. We identify a key distinction between learning what knowledge to retain and determining how to organize it: textual updates should first be validated through execution evidence, after which the retained knowledge should be structured according to its procedural dependencies and retrieval requirements. To this end, we introduce SkillSpec, a two-phase framework comprising consensus-gated evolution and representation specialization. In the consensus-gated phase, complementary editing intents generate complete candidate skills. An update is committed only when paired evaluations reach consensus, requiring sufficient overall improvement and non-negative aggregate paired gain in every repeated evaluation. In the specialization phase, signals of process and redundancy sensitivity derived from the full optimization trajectory, including accepted and rejected candidates, guide the selection of a flat, graph, or hybrid representation.Across six benchmarks and three target language models, SkillSpec improves average success rate over SkillOpt by 6.89%, averaged across the three models. These results demonstrate that reliable skill evolution and representation specialization address complementary objectives: deciding what knowledge to retain and how to structure it for inference.

## Metadata
- **Published**: 2026-09-30T20:52:00Z
- **Authors**: Huancheng Chen, Xiaodi Sun, Zhaoqiong Huang, Shenyang Huang Shreya Singhal, Jingwen Lu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.00704v1)