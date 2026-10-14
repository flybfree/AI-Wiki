---
title: Avoiding What Your Teacher Already Knows: Entity Familiarity for Deep-Search Distillation
url: http://arxiv.org/abs/2610.16251v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-12_06-25-07Z_AvoidingWhatYourTeacherAlreadyKnows_EntityFamiliar.md
generated_at: 2026-10-14 00:50
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper addresses a critical weakness in training deep-search agents through distillation from teacher models: when a teacher is already familiar with key entities in a question's underlying graph, it produces low-search-demand trajectories that provide weak supervision for the student. The authors introduce two entity familiarity estimation methods—Evidence-Verified Entity Familiarity (EVF) for validation and Self-Reported Entity Familiarity (SEF) as a practical gating mechanism—and demonstrate that filtering out entities the teacher already knows leads to richer search trajectories and substantially improved student performance, achieving state-of-the-art results among comparable-size models on multiple benchmarks.

## Key Takeaways
- The authors formalize "teacher-relative difficulty," showing that a question's structural complexity does not guarantee high search demand from a teacher who is already familiar with the entities involved. EVF estimates familiarity by verifying teacher-generated factual briefs against online evidence and correlates with teacher-relative difficulty at AUCs of 0.60–0.70, but its computational cost makes it impractical for large-scale graph construction.
- SEF is proposed as a lightweight alternative: it simply asks the teacher model whether it is familiar with a given entity before admitting that entity into the synthesis graph. Trajectories generated from SEF-gated graphs show measurably higher search demand and yield better downstream student accuracy than ungated synthesis, making it a practical filter for training data pipelines.
- Cross-teacher reuse is explored by screening graphs originally collected for other teachers using Kimi-K3's SEF judgments, producing 5,411 additional trajectories. Combined with 2,200 trajectories from newly constructed SEF-gated graphs, this data improves Qwen3.8-27B's accuracy from 44.10% to 66.41% on a BrowseComp subset and achieves state-of-the-art performance among models of comparable size on BrowseComp, SEAL-0, HLE-text, and xbench.

## Context
Deep-search agents that iteratively use retrieval tools to answer complex questions are increasingly trained via distillation from stronger teacher models, a paradigm that depends heavily on the quality and informativeness of the teacher's tool-use trajectories. Prior work has focused on question complexity and trajectory length as proxies for supervision quality, but has largely overlooked the teacher's own prior knowledge as a confounding variable. This paper fills that gap by treating entity familiarity as a first-class signal in data synthesis pipelines, bridging knowledge-graph construction with practical training-data filtering.

## Implications
For practitioners building deep-search agents, SEF offers a low-cost, model-agnostic gating mechanism that can be inserted into existing distillation pipelines to automatically discard supervision signals that a teacher can answer without genuine search, thereby raising the effective difficulty of training data without manual curation. For the broader field, the finding that cross-teacher graph reuse is viable when filtered by a single teacher's familiarity judgments suggests that large-scale entity graphs need not be rebuilt per teacher, reducing the cost and complexity of training-data infrastructure. The state-of-the-art results at 27B parameter scale also signal that data quality filtering, rather than model scale alone, can drive competitive performance on hard search benchmarks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.16251v1)
