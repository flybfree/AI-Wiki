---
title: Cross-Dataset Stability of Expert-Informed Skill Prompting and Fine-Tuning for Chinese Metaphor Identification
url: http://arxiv.org/abs/2608.25579v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_09-40-10Z_Cross_DatasetStabilityofExpert_InformedSkillPrompt.md
generated_at: 2026-08-26 20:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates cross-dataset stability of expert-informed skill prompting versus fine-tuning for Chinese metaphor identification, comparing BERT-FT, LLM-FT, LLM-ZS, and Skill-ZS across CMRE Test, CCIME, CMC. Fine‑tuned methods dominate native performance while Skill‑ZS offers the most consistent scores.

## Key Takeaways
- Fine‑tuning remains strongest on the native test set with BERT‑FT achieving 91.76 Macro‑F1, indicating task‑specific adaptation still outperforms zero‑shot approaches in familiar data.
- LLM‑FT yields the highest external mean (83.52) but Skill‑ZS provides a higher floor (82.64) and smallest observed range across datasets, showing greater stability.
- Adding the Skill to zero‑shot prompting reduces false positives on CCIME but raises false negatives on CMRE Test and CMC, highlighting trade‑offs in expert guidance.

## Context
Chinese metaphor identification remains challenging due to varying annotation policies and text distributions across corpora. Prior work often assumes dataset homogeneity, yet real‑world deployment requires methods that generalize robustly without heavy fine‑tuning.

## Implications
Practitioners can adopt Skill‑ZS for consistent cross‑dataset performance with minimal resource cost, while reserving fine‑tuning for native data where higher accuracy is needed. This balances efficiency and stability in large‑scale Chinese NLP tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25579v1)
