---
title: Acquire, Repair, Preserve: A Diagnosis-Guided Post-Training Recipe for Small-Model Dialogue Game Agents
url: http://arxiv.org/abs/2608.28458v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_15-47-47Z_Acquire_Repair_Preserve_ADiagnosis_GuidedPost_Trai.md
generated_at: 2026-08-30 20:10
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces a diagnosis‑guided post‑training recipe for small‑model dialogue game agents that addresses the limitations of static benchmarks. By combining broad supervised fine‑tuning with targeted turn‑local repairs, the model achieves large gains on the LM Playschool Challenge while keeping overall static performance stable.

## Key Takeaways  
- Broad SFT drives most of the improvement, yet turn‑local supervision is needed to fix specific failures such as repeated guesses and malformed actions within a particular dialogue family.  
- The model’s errors include feedback violations and invalid actions; repairing these locally yields measurable score lifts without harming general capabilities.  
- Out‑of‑domain performance stays low, with the largest gains observed in unseen variants of the targeted family.

## Context  
Static benchmarks often ignore the stateful nature of dialogue games, leaving small models under‑trained for such tasks. This work demonstrates that fine‑grained correction can boost narrow dialogue abilities while preserving broader language competence, offering a pragmatic path forward for limited‑resource agents.

## Implications  
For practitioners, the recipe provides an efficient way to enhance specialized chatbot performance with minimal overhead. In industry, it enables cost‑effective deployment of domain‑specific dialogue agents that excel in particular games without sacrificing general conversational ability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28458v1)
