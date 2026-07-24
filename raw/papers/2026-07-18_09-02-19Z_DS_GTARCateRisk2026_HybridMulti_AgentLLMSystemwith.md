---
title: DS@GT ARC at eRisk 2026: Hybrid Multi-Agent LLM System with Structured Algorithmic Guidance for Conversational Depression Screening
published: 2026-07-18T09:02:19Z
authors: Victor Gong, David Guecha
url: http://arxiv.org/abs/2607.16712v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DS@GT ARC at eRisk 2026: Hybrid Multi-Agent LLM System with Structured Algorithmic Guidance for Conversational Depression Screening

## Abstract
We describe DS@GT's submission to the eRisk 2026 Task 1 challenge on conversational depression screening, in which systems interview LLM personas that simulate individuals with varying depression profiles and produce a Beck Depression Inventory II (BDI-II) score plus four key symptoms per persona, without directly asking sensitive mental health questions. Our pipeline evolved through three stages: a monolithic single-model prototype to start off, a baseline multi-agent architecture that separates conversational interviewing from BDI-II scoring under a coordinating orchestration layer, and a final hybrid configuration that replaces the paid GPT-5-nano interviewer with the open-source Gemma 27B. To offset the model's weaker reasoning and instruction-following, the hybrid adds three algorithmic components: a precomputed dialogue tree that standardizes interview openers and follow-ups, a reliability-weighted consensus aggregation inspired by the Weaver framework, and a cluster-based imputation step for unprobed symptoms. We submitted three fully automated runs across all 20 personas, with Run 1 from the paid baseline and Runs 2 and 3 from the hybrid. Hybrid Run 3 achieved an ADODL of 0.9063, ranking 3rd among all complete-submission runs and placing DS@GT 2nd among the 21 teams overall, while outperforming our paid baseline Run 1 (0.8841) at roughly one-quarter of the per-persona API cost. These results support our central hypothesis that with sufficient algorithmic supervision, a weaker open-source model can compete with a stronger proprietary model in the conversational interviewer role. Our source code is available at https://github.com/dsgt-arc/erisk-task1-2026.

## Metadata
- **Published**: 2026-07-18T09:02:19Z
- **Authors**: Victor Gong, David Guecha
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.16712v1)