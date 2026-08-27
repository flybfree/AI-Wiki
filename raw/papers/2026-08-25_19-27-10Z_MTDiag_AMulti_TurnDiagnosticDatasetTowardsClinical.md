---
title: MTDiag: A Multi-Turn Diagnostic Dataset Towards Clinically Meaningful LLM Evaluation
published: 2026-08-25T19:27:10Z
authors: Pia Chouayfati, Alexander M. Fichtl, Miriam Anschütz, George Doumat, Georg Groh
url: http://arxiv.org/abs/2608.25085v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MTDiag: A Multi-Turn Diagnostic Dataset Towards Clinically Meaningful LLM Evaluation

## Abstract
Clinical diagnosis is fundamentally interactive and incremental, yet the dominant paradigm for evaluating Large Language Models (LLMs) in medicine remains static QA benchmarks or template-based dialogues. These benchmarks say little about whether a model can serve as a diagnostic agent in a dynamic clinical encounter, with LLMs showing significant accuracy and reliability degradation in multi-turn settings. To address this issue, we present MTDiag, a large multi-turn diagnostic dialogue dataset constructed from three heterogeneous sources: DDXPlus, MIMIC-IV, and published case reports (AJCR), covering common ED presentations as well as long-tail rare and atypical conditions. All cases are normalized into a canonical schema anchored in the most comprehensive and widely-adopted medical knowledge bases (UMLS concept identifiers, with ICD-10 diagnosis codes). We release the schema, a UserLM-8B-based utterance-generation pipeline, and the physician-validated dataset that converts structured clinical evidence into natural-language utterances. Importantly, we introduce and motivate clinical knowledge-grounded metrics for evaluating LLMs as diagnostic agents, beyond diagnostic accuracy, for the task of multi-turn differential diagnosis.

## Metadata
- **Published**: 2026-08-25T19:27:10Z
- **Authors**: Pia Chouayfati, Alexander M. Fichtl, Miriam Anschütz, George Doumat, Georg Groh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25085v1)