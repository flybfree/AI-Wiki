---
title: DiagEvo: Diagnosis-Guided Self-Evolution via Hierarchical Error Memory
url: http://arxiv.org/abs/2609.00768v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_05-54-47Z_DiagEvo_Diagnosis_GuidedSelf_EvolutionviaHierarchi.md
generated_at: 2026-09-01 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
DiagEvo introduces a self‑evolving language model that learns to generate questions by diagnosing recurring reasoning errors from its own failure history, storing them in a hierarchical memory and using this knowledge to guide future question generation. The method outperforms all baselines across nine benchmarks for three 4B‑scale solvers, achieving the highest mean accuracy reported.

## Key Takeaways
- DiagEvo extracts recurring error causes from self‑play failures and groups them under skill nodes, marking each as Active or Mastered based on performance on targeted questions.  
- The challenger balances cause‑targeted generation with free exploration using recurrence counts stored in the memory.  
- Double‑confidence filtering ensures intermediate‑difficulty questions are kept only when the dominant answer is clear, improving curriculum quality.

## Context
Self‑play enables models to improve autonomously, yet many approaches rely on external signals that limit closed‑loop learning. DiagEvo demonstrates that internal diagnostic memory can replace these signals, offering a fully autonomous curriculum for model evolution without human input.

## Implications
This work shows that error analysis can be leveraged as a core component of self‑evolution pipelines, potentially reducing reliance on costly external resources and enabling continuous improvement in language models. Practitioners may adopt DiagEvo’s memory and filtering strategies to build more robust training loops for smaller models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00768v1)
