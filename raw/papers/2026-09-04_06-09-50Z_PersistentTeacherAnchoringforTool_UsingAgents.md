---
title: Persistent Teacher Anchoring for Tool-Using Agents
published: 2026-09-04T06:09:50Z
authors: Hyun Bin Park, Kyungho Song, Sangmin Lee, Du-Seong Chang
url: http://arxiv.org/abs/2609.04773v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Persistent Teacher Anchoring for Tool-Using Agents

## Abstract
Distillation is common in LLM post-training, where on-policy knowledge distillation (OPKD) uses student-generated trajectories to prepare the student for downstream RL. At each state, the student matches a next-token distribution supplied by the teacher. As the rollout enters states the teacher would not visit, the teacher-student distribution gap can accumulate. In tool use, this gap becomes consequential because student-written calls execute before supervision and their observations shape later prefixes. Proposer-verifier generation addresses this drift by letting the teacher decide which student-proposed text is retained during generation. Existing formulations govern text but leave tool execution outside their scope. We propose Persistent Teacher Anchoring (PTA), a student-induced but teacher-committed rollout construction. PTA retains chunk-level verification and adds turn-level commitment, allowing a call to reach the environment only after the teacher has verified the entire turn. Treating verified chunks as atomic generation units, we introduce persistent lookahead, which fills idle rollout capacity by advancing future samples and carrying unfinished ones across student updates under the fixed verifier. Across Search-R1-style retrieval and DeepEyes-style perception RL, applying PTA before downstream RL improves macro best@4 by 2.5 and 2.8 points over OPKD under the same downstream RL budget, while lookahead improves throughput by 24%.

## Metadata
- **Published**: 2026-09-04T06:09:50Z
- **Authors**: Hyun Bin Park, Kyungho Song, Sangmin Lee, Du-Seong Chang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04773v1)