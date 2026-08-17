---
title: Who Speaks Matters: Authority-Aware Multi-View RAG over Italian Parliamentary Proceedings
url: http://arxiv.org/abs/2608.13410v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-13_16-07-23Z_WhoSpeaksMatters_Authority_AwareMulti_ViewRAGoverI.md
generated_at: 2026-08-16 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ParliamentRAG, a retrieval‑augmented generation system for Italian parliamentary transcripts that mitigates three common RAG pitfalls: speaker dominance, uneven weighting of experts, and citation errors. Evaluated against Google NotebookLM on 15 policy topics, the system outperforms NotebookLM in coverage across political groups, quotation faithfulness, and expert‑preference scores while retaining strong prose quality.

## Key Takeaways
- ParliamentRAG employs a topic‑dependent authority model that quantifies each speaker’s expertise using profession, education, and prior interventions to ensure balanced representation.  
- The system achieves perfect quotation faithfulness (1.00) compared with NotebookLM’s 0.95, preserving the exact wording of cited speech fragments.  
- Human experts consistently prefer ParliamentRAG for source‑related dimensions, indicating superior alignment with domain knowledge.

## Context
This work advances AI applications in public discourse by integrating interpretable authority signals into retrieval pipelines, a step toward more equitable and accurate information synthesis from legislative texts. It demonstrates that specialized models can outperform generic large language systems when evaluated on both automated metrics and expert judgment.

## Implications
For policymakers and journalists, ParliamentRAG offers a tool to surface diverse viewpoints without bias, enhancing transparency in democratic processes. Practitioners can adopt similar authority‑aware RAG frameworks to improve information retrieval across fragmented public records.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13410v1)
