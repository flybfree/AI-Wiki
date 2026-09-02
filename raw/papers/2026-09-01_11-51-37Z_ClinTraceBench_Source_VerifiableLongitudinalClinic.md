---
title: ClinTraceBench: Source-Verifiable Longitudinal Clinical Reasoning over EHR-Derived Dialogues
published: 2026-09-01T11:51:37Z
authors: Huimin Wang, Zhengyi Zhao, Yutian Zhao
url: http://arxiv.org/abs/2609.01111v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ClinTraceBench: Source-Verifiable Longitudinal Clinical Reasoning over EHR-Derived Dialogues

## Abstract
Clinical LLM assistants must reason over multi-visit patient trajectories, yet whether the compact history representations used to scale them---retrieval, structured timelines, LLM summaries, agentic memory---preserve the longitudinal signal clinical reasoning needs has not been measured. We introduce ClinTraceBench: 385 MIMIC-IV-derived verified dialogues with event-ID provenance, a nine-task taxonomy (T1--T9), and L0--L4 deterministic + L5 human-audit validation (98.92\% agreement). We evaluate eight history representation strategies---a no-context floor, \textit{last-visit-only}, \textit{full-context}, BGE-M3 \textit{dense-retrieval}, two compression schemes, and two agentic-memory systems (\textit{Mem0}, \textit{A-Mem})---across four backbones (DeepSeek-V3, GPT-4o-mini, Haiku~4.5, Sonnet~4.6) on 6{,}271 questions: 32 cells, 200{,}672 predictions. Four findings: (SP4) a controlled T3 injection probe isolates compression-induced \textit{relation} loss---with the attribution sentence present \textit{before} construction, \textit{Mem0}, \textit{A-Mem} and \textit{llm-summary} still recover only 0--5.3\% of the injected positives; (SP1) compressed strategies pay an aggregation tax on multi-visit trends and cross-patient comparisons; (SP2) the blind-to-full gap spans $+29.8$~pp (GPT-4o-mini) to $+62.7$~pp (Haiku); (SP3) abstention scales non-monotonically with context length. On the Pareto frontier Haiku dominates Sonnet under \textit{full-context} (\$25.76 vs.\ \$106.21), inverting the ``biggest backbone wins'' heuristic.

## Metadata
- **Published**: 2026-09-01T11:51:37Z
- **Authors**: Huimin Wang, Zhengyi Zhao, Yutian Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01111v1)