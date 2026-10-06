---
title: Mining Agent Skills from Production Traces
published: 2026-10-05T04:21:42Z
authors: Yue Ran Kang, Colton Mikolajczyk, Chhaya Methani, Hazel Mak, Sahil Bhatnagar, Susheel Suresh, Alejandro Gutierrez Munoz
url: http://arxiv.org/abs/2610.05777v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Mining Agent Skills from Production Traces

## Abstract
Agent skills that record procedural instructions are increasingly mined from execution traces rather than curated by hand. Skill-mining pipelines often use known task outcomes or feedback to guide skill construction. In production, reliable information on whether a run has succeeded may be unavailable. We study how the sampling of execution traces, access to success or failure information, and the form of the mined skills affect downstream task performance. Holding the mining pipeline fixed, we compare six combinations of mining evidence and skill forms. Mining evidence has three levels: successful trajectories only, successes and failures with their outcome labels, or the same mix with labels withheld. Skill form has two types: an ordered workflow plan, or a declarative ontology of entities, states, and policies. We evaluate the mined skills on two enterprise benchmarks, ThinkingBox-Bench and APEX-Agents. Analysis of task-level paired differences shows that the benefits of different configurations of mining evidence and skill forms depend on the enterprise domain. On ThinkingBox-Bench, paired differences show that workflows score better than ontology by 1.7 pp, Goldilocks beats success-only evidence type by 2.4 pp and Goldilocks blind simulating skills learnt without outcomes is worse by 3.1 pp. APEX-Agents shows a moderate preference for ontologies and no clear preference between evidence regimes. Within each domain, task structure related constraints drive uneven performance with mined skills. These findings motivate tailoring meta-skills to the demands of the target tasks rather than adopting a one-size-fits-all approach.

## Metadata
- **Published**: 2026-10-05T04:21:42Z
- **Authors**: Yue Ran Kang, Colton Mikolajczyk, Chhaya Methani, Hazel Mak, Sahil Bhatnagar, Susheel Suresh, Alejandro Gutierrez Munoz
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.05777v1)