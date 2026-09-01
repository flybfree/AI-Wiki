---
title: EVAR: Evidence-Validated Hypothesis Admission for Budget-Aware Narrative Reasoning
published: 2026-08-30T15:07:27Z
authors: Peilin Liu, Zhiquan Ji, Jinglong Ping
url: http://arxiv.org/abs/2608.29835v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EVAR: Evidence-Validated Hypothesis Admission for Budget-Aware Narrative Reasoning

## Abstract
Large language models (LLMs) often produce fluent but weakly grounded conclusions when reasoning over non-interactive, long-form narratives. A central failure mode is that unsupported intermediate hypotheses can enter the reasoning trajectory and contaminate subsequent inference, especially when evidence is scattered across distant parts of the story. To address this problem, we propose EVAR, an evidence-validated hypothesis admission framework for budget-aware narrative reasoning. EVAR first compiles the narrative into an immutable evidence store of source-linked atomic claims and assigns an instance-specific inference budget from unresolved gaps and uncertainty signals. During refinement, EVAR directly proposes candidate hypotheses for unresolved gaps, constructs hypothesis-conditioned validation challenges, and verifies each candidate against the locked store before admission: supported hypotheses enter the answer-supporting state, unverifiable ones are quarantined, and contradictory ones are discarded. A sufficiency-based stopping mechanism further avoids unnecessary refinement. Experiments on NarraCrime and multiple public reasoning benchmarks show that EVAR improves both task performance and evidence faithfulness while maintaining controllable inference cost.

## Metadata
- **Published**: 2026-08-30T15:07:27Z
- **Authors**: Peilin Liu, Zhiquan Ji, Jinglong Ping
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29835v1)