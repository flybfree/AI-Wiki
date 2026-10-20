---
title: When Retrieval Partially Conflicts with Skills: Understanding Procedural Hallucination in Language Models
published: 2026-10-19T05:43:27Z
authors: Guanqun Jiang, Pengfei Cao, Kang Liu, Jun Zhao
url: http://arxiv.org/abs/2610.25827v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Retrieval Partially Conflicts with Skills: Understanding Procedural Hallucination in Language Models

## Abstract
Language models increasingly use skills that provide reusable instructions and procedures for task execution. After a relevant skill has been selected, the model may need to apply its governing procedure together with retrieved task context. When the retrieved context is useful but contains cues that violate the skill, the model must retain compatible information while rejecting the conflicting cues. We study failures in which the model adopts such cues and produces a retrieval-supported but skill-invalid answer, which we call procedural hallucination. We introduce SourceClash, a matched benchmark with 1,271 bundles and 6,355 prompts across ten procedural domains. Each bundle fixes the task, skill specification, and answer space while varying the relation between the skill and retrieval. Across nine models, valid-answer rates average 25.7% under conflicting retrieval, compared with 78.2% and 72.8% under two supportive retrieval settings. Mechanistic analysis of open-weight models shows that the answer-preference difference typically reaches its maximum shortly after generation begins. Residual replacement moves the model toward valid answers, while attention decomposition attributes most of the repair to value vectors. Intervention at the identified value pathway also improves final answer validity. These results characterize how partly conflicting retrieval changes skill-guided generation.

## Metadata
- **Published**: 2026-10-19T05:43:27Z
- **Authors**: Guanqun Jiang, Pengfei Cao, Kang Liu, Jun Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.25827v1)